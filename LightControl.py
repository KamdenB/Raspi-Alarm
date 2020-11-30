import time
import platform
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

# if(platform.architecture()[0] == "32bit"):

class LightControl:
    def __init__(self, channel):
        self.channel = channel 
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.channel, GPIO.OUT)

    def on(self):
        GPIO.output(self.channel, GPIO.HIGH)

    def off(self):  
        GPIO.output(self.channel, GPIO.LOW)

    def flash(self, time, count):
        # if(not self.notPi)
        for i in range(count):
            try:
                self.on()
                time.sleep(time*100)
                self.off()
                time.sleep(time*100)
            except:
                print("GPIO Error")
            finally:
                i+=1
                GPIO.cleanup()
        self.off()
        GPIO.cleanup()