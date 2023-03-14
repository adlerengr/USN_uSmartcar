from machine import Pin, PWM, I2C
import time
from uPy_APDS9900.apds9900LITE import APDS9900LITE


# Simple test forward
motor_tf_a=Pin(4,Pin.OUT) 		# Motor control test
motor_tf_b=Pin(3,Pin.OUT) 		# Motor control test
motor_tf_c=Pin(7,Pin.OUT) 		# Motor control test
motor_tf_d=Pin(6,Pin.OUT) 		# Motor control test
motor_speed_a = PWM(motor_tf_a)
motor_speed_b = PWM(motor_tf_c)
servo_pin = Pin(1, Pin.OUT)
servo_pwm = PWM(servo_pin)
servo_pwm.freq(50)

#Powersteps
motor_0 = 0						#Motor power, 0%
motor_25 = 15000				#Motor power, aprox. 25%
motor_50 = 30000				#Motor power, aprox. 50%
motor_75 = 45000				#Motor power, aprox. 75%
motor_100 = 65534				#Motor power, 100%

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
        raise ValueError("Angle must be within parameters")
    servo_pwm.duty_u16(pulse_width * 65535 // servo_pwm.freq())

#Servo test

servo_pwm.duty_u16(1000)
time.sleep(1)
servo_pwm.duty_u16(2000)
time.sleep(1)
servo_pwm.duty_u16(1500)



# create an I2C object for communicating with the sensors
i2c =  I2C(1, scl=Pin(19), sda=Pin(18), freq=100000)
i2c2 = I2C(0, scl=Pin(17), sda=Pin(16), freq=100000)

devices = i2c.scan()
devices2 = i2c2.scan()
print("I2C devices on bus 1:", devices)
print("I2C devices on bus 2:", devices2)


# create APDS9900Lite objects for both sensors
sensor1 = APDS9900LITE(i2c)
sensor1.prox.enableSensor() #Enables sensor 1

time.sleep(0.25)

sensor2 = APDS9900LITE(i2c2)
sensor2.prox.enableSensor() #Enables sensor 2

while True:
    # read proximity values from both sensors
    value1 = sensor1.prox.proximityLevel
    value2 = sensor2.prox.proximityLevel

    # check if both sensor readings are over 1000
    if value1 < 600 and value2 < 600:
        print('stop', value1, value2)
        break  # stop the while loop

    # calculate the absolute difference between the two values
    diff = abs(value1 - value2)

    # check if the difference is over 500
    if diff > 500:
        if value1 > value2:
            #set_servo_angle(-45)
            servo_pwm.duty_u16(1000)
            print('value1 > value2', value1, value2)
        else:
            #set_servo_angle(45)
            servo_pwm.duty_u16(2000)
            print('value1 < value2', value1, value2)
    # if the difference is not over 500, check if it's over 250
    elif diff > 250:
        if value1 > value2:
            #set_servo_angle(-25)
            servo_pwm.duty_u16(1250)
            print('value1 > value2 small', value1, value2)
        else:
            #set_servo_angle(25)
            servo_pwm.duty_u16(1750)
            print('value1 < value2 small', value1, value2)
    else:
        #set_servo_angle(0)
        servo_pwm.duty_u16(1500)
        print('value1 = value2', value1, value2)
        
    time.sleep(0.1)  # wait for a short time before reading the sensors again