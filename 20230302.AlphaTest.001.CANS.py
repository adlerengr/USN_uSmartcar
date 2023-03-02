from machine import Pin, PWM, I2C
import time
from uPy_APDS9900.apds9900LITE import APDS9900LITE


# Simple test forward
motor_tf_a=Pin(4,Pin.OUT) 		# Motor control test.
motor_tf_b=Pin(3,Pin.OUT) 		# Motor control test.
motor_tf_c=Pin(7,Pin.OUT) 		# Motor control test.
motor_tf_d=Pin(6,Pin.OUT) 		# Motor control test.
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
        pulse_width = 1000
    elif angle == -25:
        pulse_width = 1250
    elif angle == 0:
        pulse_width = 1500
    elif angle == 25:
        pulse_width = 1750
    elif angle == 45:
        pulse_width = 2000
    else:
        raise ValueError("Angle must be -45, 0, or 45 degrees")
    except Exception as e:
        print("Error setting servo angle:", e)


# create an I2C object for communicating with the sensors
i2c = I2C(1, scl=Pin(5), sda=Pin(4), freq=100000)

# create APDS9900Lite objects for both sensors
sensor1 = apds9900LITE(i2c, 0x39)
sensor2 = apds9900LITE(i2c, 0x49)

while True:
    # read proximity values from both sensors
    value1 = sensor1.proximity()
    value2 = sensor2.proximity()

    # check if both sensor readings are over 1000
    if value1 > 1000 and value2 > 1000:
        break  # stop the while loop

    # calculate the absolute difference between the two values
    diff = abs(value1 - value2)

    # print the appropriate message based on the difference
    if diff > 500:
        if value1 > value2:
            set_servo_angle(-45)
        else:
            set_servo_angle(45)
    else:
        set_servo_angle(0)

    time.sleep(0.1)  # wait for a short time before reading the sensors again
