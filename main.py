from machine import Pin, PWM, I2C
import time
from uPy_APDS9900.apds9900LITE import APDS9900LITE

# Motor control pins
motor_tf_a = Pin(4, Pin.OUT)
motor_speed_a = PWM(motor_tf_a)

# Power steps
motor_steps = [0, 15000, 30000, 45000, 65534] # Motor power steps, 0%, 25%, 50%, 75%, 100%

# Servo control pins
servo_pin = Pin(1, Pin.OUT)
servo_pwm = PWM(servo_pin)
servo_pwm.freq(50)

#Sensor differences
threshold_high = 250
threshold_low = 100
prox_max = 600

# Servo angles and pulse widths
angle_to_pulse_width = {-45: 2048, -25: 3072, 0: 5120, 25: 7168, 45: 8192}

# Create an I2C object for communicating with the sensors
i2c = I2C(1, scl=Pin(19), sda=Pin(18))
i2c2 = I2C(0, scl=Pin(17), sda=Pin(16))
devices = i2c.scan()
devices2 = i2c2.scan()
#print("I2C devices on bus 1:", devices) # Debug
#print("I2C devices on bus 2:", devices2) # Debug

# Create APDS9900Lite objects for both sensors
sensor1 = APDS9900LITE(i2c)
sensor1.prox.enableSensor()  # Enables sensor 1
sensor2 = APDS9900LITE(i2c2)
sensor2.prox.enableSensor()  # Enables sensor 2

# Set the initial servo angle to 0 degrees
servo_pwm.duty_u16(angle_to_pulse_width[0])

while True:
    # Read proximity values from both sensors
    value1 = sensor1.prox.proximityLevel
    value2 = sensor2.prox.proximityLevel

    # Check if both sensor readings are below 600
    if value1 < prox_max and value2 < prox_max:
        print('stop', value1, value2)
        break  # Stop the while loop

    # Calculate the absolute difference between the two values
    diff = abs(value1 - value2)

    # Determine the servo angle and motor power based on the proximity values
    if diff > threshold_high:
        angle = -45 if value1 < value2 else 45
        motor_power = motor_steps[1]
    elif diff > threshold_low:
        angle = -25 if value1 < value2 else 25
        motor_power = motor_steps[2]
    else:
        angle = 0
        motor_power = motor_steps[4]

    # Set the servo angle and motor speed
    pulse_width = angle_to_pulse_width[angle]
    servo_pwm.duty_u16(pulse_width)
    motor_speed_a.duty_u16(motor_power)

    print('Servo angle:', angle, 'Servo PWM', pulse_width, 'Motor power:', motor_power, 'Proximity values:', value1, value2)
    time.sleep(0.1)  # Wait for a short time before reading the sensors again
