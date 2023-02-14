from machine import Pin,PWM
import time
from uPy_APDS9900.apds9900LITE import APDS9900LITE

#Simple test forward
motor_tf_a=Pin(3,Pin.OUT) 		# Motor control test.
motor_tf_b=Pin(4,Pin.OUT) 		# Motor control test.
motor_speed_a = PWM(motor_tf_a)
motor_speed_b = PWM(motor_tf_b)
#motor_tf_b.value (0);
servo_pin = machine.Pin(1, machine.Pin.OUT)
pwm = machine.PWM(servo_pin)

motor_0 = 0						#Motor power, 0%.
motor_25 = 15000				#Motor power, aprox. 25%.
motor_50 = 30000				#Motor power, aprox. 50%.
motor_75 = 45000				#Motor power, aprox. 75%.
motor_100 = 65534				#Motor power, 100%.


motor_speed_a.duty_u16(motor_25)

time.sleep(1)
motor_speed_a.duty_u16(motor_50)

time.sleep(1)
motor_speed_a.duty_u16(motor_75)

time.sleep(1)
motor_speed_a.duty_u16(motor_100)

time.sleep(1)
motor_speed_a.duty_u16(motor_0)


# Set up the servo parameters
freq = 50
duty_min = 1000
duty_max = 9000
duty_span = duty_max - duty_min

# Turn maximum one way
pwm.duty_u16(int(duty_max * 65535 / 255))
time.sleep(1)

# Turn maximum the other way
pwm.duty_u16(int(duty_min * 65535 / 255))
time.sleep(1)

# Center the servo
pwm.duty_u16(int((duty_min + duty_span / 2) * 65535 / 255))
time.sleep(1)

# Clean up the PWM signal
pwm.deinit()
servo_pin.value(0)
