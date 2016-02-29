# chipGPIO
Easy GPIO access in Python for the NTC Chip Computer!

# How to use:
Place chipGPIO.py in the same directory as your script, then include this import in your own script:

    from chipGPIO import *

You then have Arduino-style control of the GPIO pins XIO-0 through 8, addressed simply as 0-8.

*For example:*
Setting a pin's direction:

    pinMode(7,OUTPUT)

Setting a pin's state:

    digitalWrite(7,HIGH)

Reading a pin's state:

    digitalRead(7) // returns 0 or 1

# Speed
This is purely Python, no acceleration from C yet. So this means it's only good for basic GPIO read and write tasks - precisely timed actions are still better for a microcontroller. ;)

# TODO
- PWM Control
