from machine import Pin, PWM
import time
from uPy_APDS9900.apds9900LITE import APDS9900LITE

# Simple test forward
motor_tf_a=Pin(3,Pin.OUT) 		# Motor control test.
motor_tf_b=Pin(4,Pin.OUT) 		# Motor control test.
motor_tf_c=Pin(6,Pin.OUT) 		# Motor control test.
motor_tf_d=Pin(7,Pin.OUT) 		# Motor control test.
motor_speed_a = PWM(motor_tf_a)
motor_speed_b = PWM(motor_tf_c)
servo_pin = Pin(1, Pin.OUT)
servo_pwm = PWM(servo_pin)
servo_pwm.freq(50)

#Powersteps
motor_0 = 0						#Motor power, 0%.
motor_25 = 15000				#Motor power, aprox. 25%.
motor_50 = 30000				#Motor power, aprox. 50%.
motor_75 = 45000				#Motor power, aprox. 75%.
motor_100 = 65534				#Motor power, 100%.

def set_servo_angle(angle):
    if angle == -45:
        pulse_width = 500
    elif angle == 0:
        pulse_width = 1500
    elif angle == 45:
        pulse_width = 2500
    else:
        raise ValueError("Angle must be -45, 0, or 45 degrees")

    try:
        servo_pwm.duty_ns(pulse_width * 1000)
    except Exception as e:
        print("Error setting servo angle:", e)

# Set servo to -45 degrees
motor_speed_a.duty_u16(motor_100)
motor_speed_b.duty_u16(motor_100)
set_servo_angle(-45)
time.sleep(1)

# Set servo to 0 degrees
motor_speed_a.duty_u16(motor_100)
motor_speed_b.duty_u16(motor_100)
set_servo_angle(0)
time.sleep(1)

# Set servo to 45 degrees
motor_speed_a.duty_u16(motor_100)
motor_speed_b.duty_u16(motor_100)
set_servo_angle(45)
time.sleep(1)

# Set servo to 0 degrees
motor_speed_a.duty_u16(motor_100)
motor_speed_b.duty_u16(motor_100)
set_servo_angle(0)
time.sleep(1)


motor_speed_a.duty_u16(motor_0)
motor_speed_b.duty_u16(motor_0)