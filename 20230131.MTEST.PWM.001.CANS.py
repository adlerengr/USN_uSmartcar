from machine import Pin,PWM
import time


#Simple test forward
motor_tf_a=Pin(3,Pin.OUT) 		# Motor control test.
motor_tf_b=Pin(4,Pin.OUT) 		# Motor control test.
motor_speed = PWM(motor_tf_a)
motor_tf_b.value (0);


motor_0 = 0						#Motor power, 0%.
motor_25 = 15000				#Motor power, aprox. 25%.
motor_50 = 30000				#Motor power, aprox. 50%.
motor_75 = 45000				#Motor power, aprox. 75%.
motor_100 = 65534				#Motor power, 100%.


motor_speed.duty_u16(motor_25)

time.sleep(2.5)
motor_speed.duty_u16(motor_50)

time.sleep(2.5)
motor_speed.duty_u16(motor_75)

time.sleep(2.5)
motor_speed.duty_u16(motor_100)

time.sleep(2.5)
motor_speed.duty_u16(motor_0)