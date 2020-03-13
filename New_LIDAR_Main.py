from adafruit_servokit import ServoKit
import smbus
import time
import RPi.GPIO as GPIO

bus=smbus.SMBus(1)
addr=0x62

###########################################################################
#PWM board initialization
kit = ServoKit(channels=16)
kit.servo[0].set_pulse_width_range(500,2500) #hitec servo PWM for full range,180 deg
kit.servo[6].set_pulse_width_range(500,2500) #  " 90 deg
kit.servo[12].set_pulse_width_range(500,2400) #parallax servo for full range,180 deg
###########################################################################
#variables
angle180 = 0.
angle180_1 = 0.
angle90 = 0.
LIDAR_sto = 0.
LIDAR_sto1 = 0.
incr = 0.
data_out = [] 
###########################################################################
#LIDAR function
def LIDAR():
    bus.write_byte_data(0x62,0x00, 0x04)  
    val_high=bus.read_byte_data(0x62,0x0f)  
    val_low=bus.read_byte_data(0x62,0x10)  
    dist_cm=val_high*256+val_low
    print(dist_cm)
    time.sleep(1)
    return(dist_cm)
###########################################################################
#LIDAR shpherical coordinates data (r, theta, phi)
#r: distance to object seen by LIDAR (radius for origin)
#theta: vertical degrees (0º - 90º from origin)
#phi: horizontal degrees(0º - 360º around origin)
def PackData(r,t,f)
	elem = str(r) + " " + str(t) + " " + str(f) #output string
	list.insert(incr, elem)
	elem = "".
	incr = incr + 1

###########################################################################
#main
def main(start_command):

	for y in range(0,90):

		for x in range(0,179):
			kit.servo[0].angle = angle180
			time.sleep(0.25)
			LIDAR_sto = LIDAR()
			time.sleep(0.25)
			PackData(LIDAR_sto, y, x)
			x = x + 1
			angle180 = angle180 + 1

		for x1 in rang(180,360):
			kit.servo[12].angle = angle180_1
			time.sleep(0.25)
			LIDAR_sto1 = LIDAR()
			time.sleep(0.25)
			PackData(LIDAR_sto, y, x1)
			x1 = x1 + 1
			angle180_1 = angle180_1 + 1 

	kit.servo[6].angle = angle90
	y = y + 1

return(end_command)











