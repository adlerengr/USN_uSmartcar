import machine
import time
from uPy_APDS9900.apds9900LITE import APDS9900LITE
from machine import Pin, PWM

# Initialize I2C bus on RP2040
i2c = machine.I2C(0, scl=machine.Pin(17), sda=machine.Pin(16))

# Initialize the proximity sensor
apds9900 = APDS9900LITE(i2c)
apds9900.prox.enableSensor()

# Initialize motor control pins
motor_tf_a = Pin(3, Pin.OUT)
motor_tf_b = Pin(4, Pin.OUT)
motor_speed = PWM(motor_tf_a)
motor_tf_b.value(0)

# Set motor power levels
motor_0 = 0
motor_25 = 15000
motor_50 = 30000
motor_75 = 45000
motor_100 = 65534

# Initialize PWM signal for servo motor
pwm = PWM(Pin(1))
pwm.freq(50)

while True:
    apds9900.prox.readProx()
    proximity = apds9900.prox.proximityLevel
    if proximity > 1000:
        print('Turn')
        pwm.duty_u16(motor_25)
        time.sleep(0.5)
    else:
        print('Run')
        for position in range(1000, 5000, 50):
            pwm.duty_u16(position)
            time.sleep(0.01)
        for position in range(5000, 1000, -50):
            pwm.duty_u16(position)
            time.sleep(0.01)
