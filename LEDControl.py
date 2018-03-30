import time

import os

from DuetGrabber import DuetGrabber
from RaspGPIOController import RaspGPIOController


class LEDController:
    raspGPIOController = None
    duetGrabber = None
    ledController = None
    amOnRaspberry = False

    def __init__(self):
        self.detectIfOnRaspberry()
        if self.amOnRaspberry:
            self.raspGPIOController = RaspGPIOController()
        self.duetGrabber = DuetGrabber()
        time.sleep(7)
        oldZPosition = self.duetGrabber.duetProperties.zHeight
        while True:
            try:
                if oldZPosition!=self.duetGrabber.duetProperties.zHeight:
                    oldZPosition = self.duetGrabber.duetProperties.zHeight
                    self.raspGPIOController.LED_Strips[1].blue+=20
                    print("setting LEDS to blue")
            except Exception as e:
                continue

    def detectIfOnRaspberry(self):
        self.amOnRaspberry = False
        try:
            import RPi.GPIO as gpio
            self.amOnRaspberry = True
            print("On a Rasbperry!")
        except Exception as e:
            print("Not on a Raspberry")

    def getRaspberryCoreTemp(self):
        coreTemp=os.system("/opt/vc/bin/vcgencmd measure_temp")
        print("CPU Temperature: " + str(coreTemp))
        return coreTemp