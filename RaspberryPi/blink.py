import RPi.GPIO as GPIO
from time import sleep
import os.path
from Network.tcp_send import TCP_send

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

f = open('file.txt', 'w')
f.write('hello world')
f.close()
finished_flag = 0

while not os.path.exists('stop.txt') and finished_flag != 5:
    GPIO.output(8, GPIO.HIGH)
    print('on')
    sleep(1)
    GPIO.output(8, GPIO.LOW)
    print('off')
    sleep(1)
    finished_flag = finished_flag + 1
    print(finished_flag)

print('should stop blinking')

TCP_send.send_file()



GPIO.cleanup()
