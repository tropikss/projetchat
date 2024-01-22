

m = grove_i2c_motor_driver.motor_driver(address = 0x0f)

def forward():
	print("Forward")
	m.MotorSpeedSetAB(100,100)	#defines the speed of motor 1 and motor 2;
	m.MotorDirectionSet(0b1010)	#"0b1010" defines the output polarity, "10" means the M+ is "positive" while the M- is "negtive"
	time.sleep(2)

def back():
	print("Back")
	m.MotorSpeedSetAB(100,100)
	m.MotorDirectionSet(0b0101)	#0b0101  Rotating in the opposite direction
	time.sleep(2)

def stop():
	print("Stop")
	m.MotorSpeedSetAB(0,0)
	time.sleep(1)