from chipGPIO import *
import time

pinMode(7,OUTPUT)
pinMode(6,INPUT)

print "Setting XIO-P7 HIGH..."
digitalWrite(7,HIGH)
time.sleep(1)

print "Setting XIO-P7 LOW..."
digitalWrite(7,LOW)
time.sleep(1)

print "State of XIO-P6 is: "+str(digitalRead(6))+" (pullup)"
