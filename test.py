import RPi.GPIO as GPIO
import time
channel = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

def on(pin):
    GPIO.output(pin, GPIO.HIGH)

def off(pin):
    GPIO.outpout(pin, GPIO.LOW)

if __name__ == '__main__':
    try:
        on(channel)
        time.sleep(1)
        off(channel)
        time.sleep(1)
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()
        pass