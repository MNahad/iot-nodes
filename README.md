# manc-iot-nodes

## This repository contains the source code for the University of Manchester DigiLab Bicycle Power Analyser project.

The PCB design consists of:

+ An ESP32 DevKit-C running MicroPython
+ An Adafruit INA219 DC Current Sensor
+ Micro-usb for source (bicycle generator) and USB-A for load (smartphone battery)
+ USB-C to power the PCB components
+ Carrier board with headers for future sensor interfaces (e.g. tachometer / IR sensor / quad encoder)

The code starts up a Wi-Fi Access Point and HTTP server that listens for incoming connections. Upon a successful request, the server returns the latest power and energy data back to the client.

The code utilises the Adafruit CircuitPython INA219 driver modified to run with MicroPython.

https://medium.com/uom-digilab/pedal-power-the-charging-bike-1feb51d9afbf

### PCB Design

![PCB](https://github.com/MNahad/manc-iot-nodes/blob/master/IMG_20190613_174211.jpg "PCB and components")
