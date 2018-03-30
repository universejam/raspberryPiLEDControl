import argparse
import time
import pigpio
from threading import Thread

# LED strip configuration:
from neopixel import Color

from ArduinoController import ArduinoController
from LEDStrip import LEDStrip


class RaspGPIOController:
    strip1 = None
    strip2 = None
    strip3 = None
    arduinoController=None
    LED_Strips=[]

    def __init__(self):
        print("Starting LEDController")
        from neopixel import Adafruit_NeoPixel
        from neopixel import Color

     #   self.setUpButtons()

        # Process arguments
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
        args = parser.parse_args()

        self.arduinoController=ArduinoController()

     #   S1, H332, X100, Y146, Z128, R255, G255, B255


r=RaspGPIOController()
##    def setUpButtons(self):
##        import RPi.GPIO as GPIO
##
##        GPIO.setmode(GPIO.BCM)
##        GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
##        GPIO.add_event_detect(21, GPIO.FALLING, callback=self.buttonGreenCallback, bouncetime=300)
##
##    def buttonGreenCallback(self, channel):
##        print("Green button pressed")

