
import grove_i2c_motor_driver
m = grove_i2c_motor_driver.motor_driver(address = 0x0f)
import time

def forward(n):
	print("Forward")
	m.MotorSpeedSetAB(100,100)	#defines the speed of motor 1 and motor 2
	m.MotorDirectionSet(0b1010)	#"0b1010" defines the output polarity, "10" means the M+ is "positive" while the M- is "negtive"
	time.sleep(n)

def back(n):
	print("Back")
	m.MotorSpeedSetAB(100,100)
	m.MotorDirectionSet(0b0101)	#0b0101  Rotating in the opposite direction
	time.sleep(n)

def stop():
	print("Stop")
	m.MotorSpeedSetAB(0,0)
	time.sleep(1)