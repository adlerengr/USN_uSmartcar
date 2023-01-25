from machine import Pin,PWM
import time

#Lights.
led_f=Pin(16,Pin.OUT) 			# Front light.
led_r=Pin(1,Pin.OUT) 			# Rear light.

#Motors.
motor_fl=Pin(17,Pin.OUT) 		# Motor, front left.
motor_fr=Pin(14,Pin.OUT) 		# Motor, front right.
motor_rl=Pin(28,Pin.OUT) 		# Motor, rear left.
motor_rr=Pin(5,Pin.OUT) 		# Motor, rear right.

#Lights, PWM.
led_f_pwm = PWM(led_f)			#PWM modulation, front light.
led_r_pwm = PWM(led_r)			#PWM modulation, rear light.

#Motors, PWM.
motor_fl_pwm = PWM(motor_fl) 	#PWM modulation, front left motor.
motor_fr_pwm = PWM(motor_fr)	#PWM modulation, front right motor.
motor_rl_pwm = PWM(motor_rl)	#PWM modulation, rear left motor.
motor_rr_pwm = PWM(motor_rr)	#PWM modulation, rear right motor.

#Light intensity
led_low = 15000					#Light intensity, low setting, aprox. 25%
led_high = 50000				#Light intensity, high setting, aprox. 75%

#Motors, power modulation
motor_25 = 15000				#Motor power, aprox. 25%
motor_50 = 30000				#Motor power, aprox. 50%
motor_75 = 45000				#Motor power, aprox. 75%
motor_100 = 65534				#Motor power, 100%