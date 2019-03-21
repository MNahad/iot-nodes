# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import secrets
import webrepl
webrepl.start()

import machine
import network

import esp
esp.osdebug(0)

import gc
gc.collect()

try:
  import usocket as socket
except:
  import socket

ssid = secrets.ssid
passwd = secrets.psk
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=passwd, authmode=3)

led = machine.Pin(2, machine.Pin.OUT)
