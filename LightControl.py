import time
import platform
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

# if(platform.architecture()[0] == "32bit"):

class LightControl:
    def __init__(self, channel, pin):
        self.channel = channel 
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.channel, GPIO.OUT)

    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def off(self):  
        GPIO.output(self.pin, GPIO.LOW)

    def flash(self, time, count):
        # if(not self.notPi)
        for i in range(count):
            self.on()
            time.sleep(time*100)
            self.off()
            time.sleep(time*100)
            i+=1
        self.off()