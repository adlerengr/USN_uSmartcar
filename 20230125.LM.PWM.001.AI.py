from machine import Pin, PWM
import time

# Lights and motors
pins = [Pin(16, Pin.OUT), Pin(1, Pin.OUT), Pin(17, Pin.OUT), Pin(14, Pin.OUT), Pin(28, Pin.OUT), Pin(5, Pin.OUT)]
pwms = [PWM(pin) for pin in pins]

# Light intensity
led_low = 15000
led_high = 50000

# Motors power
motor_0 = 0
motor_25 = 15000
motor_50 = 30000
motor_75 = 45000
motor_100 = 65534

# Set power for all motors
def set_motor_power(power):
    for pwm in pwms[2:]:
        pwm.duty_u16(power)

# Movement tests:
# Forward
set_motor_power(motor_25)
time.sleep(5)
set_motor_power(motor_0)

# Turning
pwms[2].duty_u16(motor_25)
pwms[3].duty_u16(motor_25)
time.sleep(2.5)
set_motor_power(motor_0)
time.sleep(2.5)
pwms[4].duty_u16(motor_25)
pwms[5].duty_u16(motor_25)
time.sleep(2.5)
set_motor_power(motor_0)
