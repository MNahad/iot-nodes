# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import secrets # Import secret data
import webrepl
webrepl.start() # Start the webREPL interface

import network

import esp
esp.osdebug(0) # Debug messages

import gc
gc.collect() # Garbage collection

# Set ssid and psk
ssid = secrets.ssid
passwd = secrets.psk
# Start Access Point
ap = network.WLAN(network.AP_IF)
ap.active(True)
# Configure AP with ssid, psk and WPA2 auth
ap.config(essid=ssid, password=passwd, authmode=3)
