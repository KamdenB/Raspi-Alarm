import RPi.GPIO as GPIO

class LightControl(channel):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.OUT)

    def on(pin):
        GPIO.output(pin, GPIO.HIGH)

    def off(pin):
        GPIO.output(pin, GPIO.LOW)