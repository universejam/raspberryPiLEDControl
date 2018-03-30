import json
import telnetlib
import time
from threading import Thread

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from DuetProperties import DuetProperties


class DuetGrabber:
    duetProperties = None
    LEDController = None
    IP = None
    tn=None
    def __init__(self):
        print("Starting DuetGrabber")
        self.duetProperties = DuetProperties()
        self.IP = "192.168.1.31"

        self.tn = telnetlib.Telnet(host=self.IP, port=23)
       # self.tn.interact()
        print("Telnet OK")
        self.getCurrentStatus_Telnet()


    def getCurrentStatus_Telnet(self):

        self.tn.write("M408".encode())
        print("Written to telnet")
        print(self.tn.read_lazy())
        print("Telnet done")

    def getCurrentStatus_WebInterface(self):

        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Firefox(firefox_options=options)
        print("Connecting to " + self.IP + " with Firefox headless")
        driver.get("http://" + self.IP + "/")
        gCodeConsoleButton = driver.find_element_by_xpath("/html/body/main/div/div[2]/div[1]/ul[3]/li[1]/a")
        gCodeConsoleButton.click()

        updateThread = Thread(target=self.updatePositions, args=[driver])
        updateThread.start()

    def updatePositions(self, driver):
        print("Started updatePositions thread")

        while True:
            gCodeField = driver.find_element_by_xpath(
                "/html/body/main/div/div[2]/div[2]/div[4]/div[1]/form/div[1]/div/input")
            # print("Sending M408")
            gCodeField.send_keys("M408")
            sendButton = driver.find_element_by_xpath(
                "/html/body/main/div/div[2]/div[2]/div[4]/div[1]/form/div[2]/div/div/button")
            sendButton.click()
            statusMessage = driver.find_element_by_xpath(
                "/html/body/main/div/div[2]/div[2]/div[4]/div[2]/div/div/div[1]/div[2]").text
            if "M408\n" in statusMessage:
                statusMessage = statusMessage.split("\n", 1)[1]
                if "\n" in statusMessage:
                    statusMessage = statusMessage.split("\n", 1)[0]
            try:
                statusMessageJSON = json.loads(statusMessage)
                # print(statusMessageJSON)
                self.duetProperties.xPosition = statusMessageJSON['pos'][0]
                self.duetProperties.yPosition = statusMessageJSON['pos'][1]
                self.duetProperties.zHeight = statusMessageJSON['pos'][2]
                print("xPosition: " + str(self.duetProperties.xPosition) + ", yPosition: " + str(
                    self.duetProperties.yPosition) + ", zHeight: " + str(self.duetProperties.zHeight))
                time.sleep(3)
            except Exception as e:
                time.sleep(4)
                continue


d=DuetGrabber()