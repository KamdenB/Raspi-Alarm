import RPi.GPIO as GPIO

channnel = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(channnel, GPIO.OUT)

def light_on(pin):
    GPIO.output(pin, GPIO.HIGH)

def light_off(pin):
    GPIO.output(pin, GPIO.LOW)