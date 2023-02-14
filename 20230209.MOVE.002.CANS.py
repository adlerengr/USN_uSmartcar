from machine import Pin,PWM
import time


#Simple test forward
motor_tf_a=Pin(3,Pin.OUT) 		# Motor control test.
motor_tf_b=Pin(4,Pin.OUT) 		# Motor control test.
motor_tf_c=Pin(6,Pin.OUT) 		# Motor control test.
motor_tf_d=Pin(7,Pin.OUT) 		# Motor control test.
motor_speed_a = PWM(motor_tf_a)
motor_speed_b = PWM(motor_tf_c)
#motor_tf_b.value (0);


motor_0 = 0						#Motor power, 0%.
motor_25 = 15000				#Motor power, aprox. 25%.
motor_50 = 30000				#Motor power, aprox. 50%.
motor_75 = 45000				#Motor power, aprox. 75%.
motor_100 = 65534				#Motor power, 100%.


time.sleep(5)

motor_speed_a.duty_u16(motor_25)
motor_speed_b.duty_u16(motor_25)

time.sleep(1)
motor_speed_a.duty_u16(motor_50)
motor_speed_b.duty_u16(motor_50)

time.sleep(1)
motor_speed_a.duty_u16(motor_75)
motor_speed_b.duty_u16(motor_75)

time.sleep(1)
motor_speed_a.duty_u16(motor_100)
motor_speed_b.duty_u16(motor_100)

time.sleep(1)
motor_speed_a.duty_u16(motor_0)
motor_speed_b.duty_u16(motor_0)
