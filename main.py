from machine import Pin, PWM, I2C
import utime
from lib.apds9900LITE import APDS9900LITE
from lib.servo import Servo

# Motor control pins
motor_signalf1 = PWM(Pin(11, Pin.OUT))
motor_signalf2 = PWM(Pin(10, Pin.OUT))
motor_signalr1 = PWM(Pin(9, Pin.OUT))
motor_signalr2 = PWM(Pin(8, Pin.OUT))

# Power steps
motor_steps = [0, 10000, 15000, 20000, 25000, 31250, 45000, 65534]

# Servo control pins
servo = Servo(1)

# Sensor differences
threshold_l = 250
threshold_m = 450
threshold_h = 550
threshold_max = 650
prox_max = 600

# Servo angles
servo_angles = {-4: 0, -3: 128, -2: 256, -1: 384, 0: 512, 1: 640, 2: 768, 3: 896, 4: 1024}

# Create I2C objects for communicating with the sensors
i2c2 = I2C(1, scl=Pin(19), sda=Pin(18))
i2c = I2C(0, scl=Pin(17), sda=Pin(16))

# Create APDS9900Lite objects for both sensors
sensor1 = APDS9900LITE(i2c)
sensor1.prox.enableSensor()
sensor2 = APDS9900LITE(i2c2)
sensor2.prox.enableSensor()

# Set the initial servo angle to 0 degrees
servo.goto(servo_angles[0])

# Get the current time and date
current_time = utime.localtime()

# Format the time and date as a string
time_str = "{}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(
    current_time[0], current_time[1], current_time[2], current_time[3], current_time[4], current_time[5])

# Write the time and date to the file
with open('sensor_logs.txt', 'a') as file:
    file.write(time_str + '\n')

# Small pause before starting the run
utime.sleep_ms(1500)   

# Start the timer when the while loop starts running
start_time = utime.ticks_ms()

# LAUNCH CONTROL
#start_time = utime.ticks_ms()
#while utime.ticks_ms() - start_time < 500:
#    motor_signalf1.duty_u16(7)
#    motor_signalf2.duty_u16(0)
#    motor_signalr1.duty_u16(7)
#    motor_signalr2.duty_u16(0) 

# Line following variables
hold_angle = 0
last_angle = 0
lost_line_count = 0
max_lost_line_count = 3
line_detected = True

while True:
    # Read proximity values from both sensors
    value1, value2 = sensor1.prox.proximityLevel, sensor2.prox.proximityLevel

    # Code to stop motors and stop the loop when crossing the finish line
    if value1 < prox_max and value2 < prox_max:
        motor_signalf1.duty_u16(7)
        motor_signalf2.duty_u16(7)
        motor_signalr1.duty_u16(7)
        motor_signalr2.duty_u16(7)
        break

    # Calculating difference between proximity sensor 1 and 2
    diff = abs(value1 - value2)

    if diff > threshold_l:
        if not line_detected:  # Reverse the direction of hold_angle when the line is detected again
            hold_angle = -hold_angle
            line_detected = True
        lost_line_count = 0
        angle = -4 if diff > threshold_max else -3 if diff > threshold_h else -2 if diff > threshold_m else -1
        angle *= (1 if value1 < value2 else -1)
    else:
        lost_line_count += 1
        if lost_line_count > max_lost_line_count:
            # Take corrective action when the line is lost
            angle = hold_angle
            line_detected = False  # Set line_detected to False when the line is lost
        else:
            angle = 0

    motor_power = motor_steps[2]

    # Update the last_angle and hold_angle variables if the angle has changed
    if last_angle != angle:
        if angle != 0:
            hold_angle = angle
        last_angle = angle  # Update last_angle after updating hold_angle

    # Set the servo angle to the last_angle
    servo.goto(servo_angles[last_angle])
    motor_signalf1.duty_u16(motor_power)
    motor_signalf2.duty_u16(0)
    motor_signalr1.duty_u16(motor_power)
    motor_signalr2.duty_u16(0)

    # Write sensor logs to a text file while the loop is running (Only use for debug. SLOW!!)
#    with open('sensor_logs.txt', 'a') as file:
#        file.write(f'Servo angle: {angle} Proximity values: {value1} {value2} Lost counter: {lost_line_count}\n')

    utime.sleep_ms(100)

# Calculate the time delta (elapsed time)
end_time = utime.ticks_ms()
elapsed_time_ms = utime.ticks_diff(end_time, start_time)
elapsed_time_seconds = round(elapsed_time_ms / 1000, 2)

# Write the delta to a text file when the while loop is finished
with open('time_delta.txt', 'a') as file:
    file.write('\n' + time_str + '\n' + f'Lap time: {elapsed_time_seconds:.2f} seconds' + '\n')
