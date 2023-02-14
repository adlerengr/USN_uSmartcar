from machine import Pin,PWM
import time

led=Pin(1,Pin.OUT)
led_r=Pin(5,Pin.OUT)
motor_f=Pin(2,Pin.OUT)
motor_r=Pin(3,Pin.OUT)
#motor_f_pwm = PWM(motor_f)
#motor_r_pwm = PWM(motor_r)

#motor_f_speed = PWM(motor_f)
#motor_r.value(0);

#duty=35000
#motor_f_speed.duty_u16(duty)

led.value(1);
led_r.value(0);
motor_f.value(1);
motor_r.value(0);

time.sleep(5)

led.value(1);
led_r.value(1);
motor_f.value(0);
motor_r.value(1);

time.sleep(5)

led.value(0);
led_r.value(0);
motor_f.value(0);
motor_r.value(0);

time.sleep(5)