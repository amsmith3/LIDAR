import smbus
import time
import RPi.GPIO as GPIO

bus=smbus.SMBus(1)
addr=0x62

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

servoPIN = 17
continuous_servoPIN = 24


x = GPIO.PWM(continuous_servoPIN, 50)
y = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz

x.start(2.5) # Initialization
y.start(2.5)



################################################################
#UNDER 1.5ms for Clockwise
#1.5ms for STOP
#OVER 1.5ms for Counter-Clockwise
def HorizontalServo(degree, dir)
  millisecs = (speed_dir/1000)

  for x in range(0,length): #not sure on how long length needs to be to move a degree yet
    GPIO.output(continuous_servoPIN, HIGH) #create pulse for specific
    time.sleep(millisecs)                  #direction and speed
    GPIO.output(continuous_servoPIN, LOW)
    time.sleep(0.020) #20ms delay, required for continuous servo

################################################################
#MAX rotation angle(180º) = y.ChangeDutyCycle(12.5)
#Middle rotation angle(90º) = y.ChangeDutyCycle(7.5)
#MIN rotation angle(0º) = y.ChangeDutyCycle(2.5)
#1º steps from 0º - 90º = ±0.05556
#Example 5º = 2.5 + (5 x 0.05556) = 2.7778
#NOTE: only go to 89º (AKA 179º) vertical, rounding issues
def VerticalServo(position_deg):
  if(position_degree > 0):
    position = ((position_deg * 0.05556) + 2.5)
    y.ChangeDutyCycle(position)
    time.sleep(.5)

################################################################
def LIDAR():
    bus.write_byte_data(0x62,0x00, 0x04)   
    val_high=bus.read_byte_data(0x62,0x0f)   
    val_low=bus.read_byte_data(0x62,0x10)   
    dist_cm=val_high*256+val_low
    print(dist_cm)
    time.sleep(1)
    return(dist_cm)

################################################################
#LIDAR shpherical coordinates data (r, theta, phi)
#r: distance to object seen by LIDAR (radius for origin)
#theta: vertical degrees (0º - 90º from origin)
#phi: horizontal degrees(0º - 360º around origin)
def PackData(r,t,f)
  
################################################################  
while True:
  for i in range(0,90)
    for k in range(0,359)
      if(k > 359) r = LIDAR()
        time.sleep(.25)
        HorizontalServo(k, 1)
        time.sleep(.25)
        PackData(r,i,k)

      else
        HorizontalServo(359,0)

  VerticalServo(i)


  p.stop()
  GPIO.cleanup()











