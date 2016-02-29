from chipGPIO import *
import time

pinMode(7,OUTPUT)
pinMode(6,INPUT)

print "Toggling  XIO-P7 10 times..."
for i in range(0,10):
        digitalWrite(7,HIGH)
        time.sleep(0.1)
        digitalWrite(7,LOW)
        time.sleep(0.1)

state = digitalRead(6)
print "Watching state on XIO-P6: (Connect it to ground to see changes! Ctrl-C to end test.)"
while True:
        s = digitalRead(6)
        if s != state:
                state = s
                print "State of XIO-P6 (pullup) changed to: "+str(state)

print "END"
