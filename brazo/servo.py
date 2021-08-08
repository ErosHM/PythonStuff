import Adafruit_PCA9685	# Import the library used to communicate with PCA9685
import time

pwm = Adafruit_PCA9685.PCA9685()	# Instantiate the object used to control the PWM
pwm.set_pwm_freq(50)	# Set the frequency of the PWM signal

# Make the servo connected to the No. 3 servo port on the RobotHAT drive board reciprocate
while 1:
	for i in range(95,530,5):
		pwm.set_pwm(7, 0, i)
		time.sleep(0.02)
	for i in range(530,95,-5):
		pwm.set_pwm(7, 0, i)
		time.sleep(0.02)

