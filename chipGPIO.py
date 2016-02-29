import os
import sys

INPUT = "in"
OUTPUT = "out"
LOW = 0
HIGH = 1

def pinMode(pin,mode):
        pinMapped = str(pin+408)
        os.system("sudo sh -c 'echo "+pinMapped+" > /sys/class/gpio/export' > /dev/null 2>&1")
        os.system("sudo sh -c 'echo "+mode+" > /sys/class/gpio/gpio"+pinMapped+"/direction'")
        sys.stdout.write("XIO-P"+str(pin)+" set to "+str(mode)+".\n")

def digitalWrite(pin,state):
        pinMapped = str(pin+408)
        os.system("sudo sh -c 'echo "+str(state)+" > /sys/class/gpio/gpio"+pinMapped+"/value'")

def digitalRead(pin):
        pinMapped = str(pin+408)
        value = os.popen("cat /sys/class/gpio/gpio"+pinMapped+"/value").read()
        return int(value)
