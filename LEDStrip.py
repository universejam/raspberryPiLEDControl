import time
from threading import Thread

from neopixel import Color


class LEDStrip:
    axis = None

    green = None
    red = None
    blue = None

    neopixel_Object = None
    LED_COUNT = 38  # Number of LED pixels.
    LED_PIN = None  # GPIO pin connected to the pixels (18 uses PWM!).
    LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
    LED_DMA = 10  # DMA channel to use for generating signal (try 10)
    LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
    LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
    LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53
    limitHeight = LED_COUNT

    def __init__(self, axis, GPIO_Pin, LED_COUNT=38, LED_FREQ_HZ=800000, LED_DMA=10, LED_BRIGHTNESS=255,
                 LED_INVERT=False, LED_CHANNEL=0):
        print("Initializing LED Strip on GPIO Pin " + str(GPIO_Pin))
        from neopixel import Adafruit_NeoPixel
        self.LED_COUNT = LED_COUNT
        self.LED_PIN = GPIO_Pin
        self.LED_FREQ_HZ = LED_FREQ_HZ
        self.LED_DMA = LED_DMA
        self.LED_BRIGHTNESS = LED_BRIGHTNESS
        self.LED_INVERT = LED_INVERT
        self.LED_CHANNEL = LED_CHANNEL
        self.green = 0
        self.red = 0
        self.blue = 0
        self.neopixel_Object = Adafruit_NeoPixel(self.LED_COUNT, self.LED_PIN, self.LED_FREQ_HZ, self.LED_DMA,
                                                 self.LED_INVERT, self.LED_BRIGHTNESS,
                                                 self.LED_CHANNEL)
        self.neopixel_Object.begin()
        updateColorsThread = Thread(target=self.updateColors)
        updateColorsThread.start()
        print("Started updateColors Thread")

    def updateColors(self):
        oldGreen = self.green
        oldRed = self.red
        oldBlue = self.blue
        limit = 40
        while True:
            if self.green != oldGreen or self.red != oldRed or self.blue != oldBlue:
                oldGreen = self.green
                oldRed = self.red
                oldBlue = self.blue
                print("Green: " + "{:>3}".format(str(self.green)) + ", Red: " + "{:>3}".format(
                    str(self.red)) + ", Blue: " + "{:>3}".format(str(self.blue)) + "\n")
                color = Color(self.green, self.red, self.blue)
                for i in range(self.neopixel_Object.numPixels()):
                    if i < self.limitHeight:
                        self.neopixel_Object.setPixelColor(i, color)
                self.neopixel_Object.show()
                time.sleep(50 / 1000.0)
