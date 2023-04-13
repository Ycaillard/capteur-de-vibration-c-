""" Install librairy package if necessary : pip3 install apa102-pi"""

from apa102_pi.driver import apa102
import time

"""Here we instantiate the apa102 library to our “strip” object. 
Into this, we pass in a couple of variables.
"""
strip = apa102.APA102(num_led=64, order='rgb')

"""Here we call the “strip” objects, “clear_strip()” function. 
This function will turn off all the LEDs in the strip and leave it completely blank.
"""
strip.clear_strip()

"""Next, we utilize the “strip” objects, “set_pixel_rgb()” function so that 
we can define the color to set for individual LEDs. These objects are pushed into a buffer.
"""
for i in range(64):
	strip.set_pixel_rgb(i, 0x00FF00)  # Green


"""#This function tells the APA102 library that it should now push the buffer 
we set with the “set_pixel_rgb()” function to the LED strip. 
This function is what will light up the LED strip.
"""
strip.show()

"""This function cleans up all the connections and prepares it 
so that we can easily talk with the APA102 again.
"""
time.sleep(0.1)
strip.cleanup()
