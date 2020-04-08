import RPi.GPIO as GPIO
from time import sleep
import os.path

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

f = open('file.txt', 'w')
f.write('hello world')
f.close()

while not os.path.exists('stop.txt'):
    GPIO.output(8, GPIO.HIGH)
    print('on')
    sleep(1)
    GPIO.output(8, GPIO.LOW)
    print('off')
    sleep(1)

print('should stop blinking')
GPIO.cleanup()