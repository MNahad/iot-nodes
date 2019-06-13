import ina219 # Modified ina219 driver
import usocket as socket
import ujson as json
import utime as time

start = time.ticks_ms() # Start measuring time delta
sensor = ina219.INA219(scl_pin=26, sda_pin=27) # Create sensor obj
energy = 0 # Initialise energy counter


def res():
""" Function to return REST API response """
    data = {
        "current(A)": current,
        "voltage(V)": voltage,
        "power(W)": power,
        "totalEnergy(J)": energy,
    }
    return json.dumps(data)


# Store server address data
addr = socket.getaddrinfo('192.168.4.1', 80)[0][-1]
# Create websocket obj
sock = socket.socket()
# Set socket timeout
sock.settimeout(0.01)
# Bind to server
sock.bind(addr)
# Start listening
sock.listen(1)

# The following is in a continuous loop
while True:
    # Calculate power and energy
    current = sensor.current / 1000
    voltage = sensor.bus_voltage + sensor.shunt_voltage
    end = time.ticks_ms() # Store delta end time
    power = voltage * current
    energy += power * (time.ticks_diff(end,start)) / 1000
    start = end # Start new time delta
    try:
        # Accept client connection and read API req
        cl, addr = sock.accept()
        req = cl.makefile('rwb', 0)
        while True:
            line = req.readline()
            if not line or line == b'\r\n':
                break
        # Send API res and close connection
        cl.send('HTTP/1.1 200 OK\r\n')
        cl.send('Content-Type: application/json\r\n\r\n')
        cl.send(res())
        cl.close()
    except:
        print("Comms error with client")
    time.sleep_ms(500) # Time delay
