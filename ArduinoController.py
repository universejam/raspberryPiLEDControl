import time

import serial
from threading import Thread

#// S1, H332, X179, Y146, Z128, R255, G255, B255

class ArduinoController:
    stripNumber=None
    totalHeight=None
    xPosition=None
    yPositon=None
    zPosition=None
    message = None

    def __init__(self):
        arduino = None
        lastReturnMessage = None
        self.arduino = serial.Serial('COM14', 9600, timeout=.1)
        time.sleep(1)  # give the connection a second to settle
        arduinoThread=Thread(target=self.updateNewValues,args=[])

    def updateNewValues(self):
        if self.message != None:
            self.arduino.write(self.message.encode())
            print("Message sent: " + self.message)
            self.message=None

    def monitorSerialComm(self):
        while True:
            data = self.arduino.readline().decode().strip('\r\n')
            if data:
                print("Response received: "+data)
                self.lastReturnMessage = data
