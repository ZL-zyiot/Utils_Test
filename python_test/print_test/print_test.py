#!/usr/bin/python
#coding=UTF-8
import serial

print("this is a python test")
serial = serial.Serial('COM7', 115200)
print(serial)
if serial.isOpen():
    print("open serial sucess")
else:
    print("open serial failed")

try:
    while True:
        count = serial.inWaiting()
        if count > 0:
            data = serial.read(count)
            print("receive:", data)
            
            serial.write(data)

except KeyboardInterrupt:
    if serial != None:
        serial.close()