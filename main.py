from machine import Pin, PWM, I2C
import utime
from lib.apds9900LITE import APDS9900LITE
from lib.servo import Servo

# Motor control pins
motor_signal1 = PWM(Pin(11, Pin.OUT))
motor_signal2 = PWM(Pin(12, Pin.OUT))

# Power steps
motor_steps = [0, 15000, 30000, 45000, 65534]

# Servo control pins
servo = Servo(1)

# Sensor differences
threshold_low = 50
threshold_high = 150
prox_max = 600

# Servo angles
servo_angles = {-2: 0, -1: 256, 0: 512, 1: 768, 2: 1024}

# Create I2C objects for communicating with the sensors
i2c = I2C(1, scl=Pin(19), sda=Pin(18))
i2c2 = I2C(0, scl=Pin(17), sda=Pin(16))

# Create APDS9900Lite objects for both sensors
sensor1 = APDS9900LITE(i2c)
sensor1.prox.enableSensor()
sensor2 = APDS9900LITE(i2c2)
sensor2.prox.enableSensor()

# Set the initial servo angle to 0 degrees
servo.goto(servo_angles[0])

# Start the timer when the while loop starts running
start_time = utime.ticks_ms()

while True:
    # Read proximity values from both sensors
    value1, value2 = sensor1.prox.proximityLevel, sensor2.prox.proximityLevel

    # Code to stop motors and stop the loop when crossing the finish line
    if value1 < prox_max and value2 < prox_max:
        motor_signal1.duty_u16(4)
        motor_signal2.duty_u16(4)
        break

    # Calculating difference between proximity sensor 1 and 2
    diff = abs(value1 - value2)

    # Adjusting servo angle depending on sensor difference
    if diff > threshold_high:
        angle = -2 if value1 < value2 else 2
        motor_power = motor_steps[1]
    elif diff > threshold_low:
        angle = -1 if value1 < value2 else 1
        motor_power = motor_steps[2]
    else:
        angle, motor_power = 0, motor_steps[4]

    servo.goto(servo_angles[angle])
    motor_signal1.duty_u16(motor_power)
    motor_signal2.duty_u16(0)

    utime.sleep_ms(100)

# Calculate the time delta (elapsed time)
end_time = utime.ticks_ms()
elapsed_time_ms = utime.ticks_diff(end_time, start_time)
elapsed_time_seconds = round(elapsed_time_ms / 1000, 2)

# Write the delta to a text file when the while loop is finished
with open('time_delta.txt', 'w') as file:
    file.write(f'Lap time: {elapsed_time_seconds:.2f} seconds')
