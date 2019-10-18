#!/usr/bin/env python3

from ev3dev2.button import Button
from ev3dev2.display import Display
from ev3dev2.motor import LargeMotor, MediumMotor, MoveSteering, MoveTank
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor, GyroSensor
import time

# Set up motors
tank = MoveTank(OUTPUT_B, OUTPUT_C)
steerer = MoveSteering(OUTPUT_B, OUTPUT_C)
back_attachment = MediumMotor(OUTPUT_A)
front_attachment = MediumMotor(OUTPUT_D)

# Set up sensors
gyro = GyroSensor(INPUT_1)
front_color = ColorSensor(INPUT_2)
mid_color = ColorSensor(INPUT_3)
ultrasonic = UltrasonicSensor(INPUT_4)

# Set up buttons
buttons = Button()

# Set up screen
lcd = Display()


def display_ev3(messages):
    lcd.clear()
    height = 0
    font = 'helvB18'
    for message in messages:
        lcd.text_pixels(message, False, 0, height, 'black', font)
        height = height + 19
    lcd.update()


def print_and_wait(message):
    # Print the message.
    display_ev3([message, '', '', '', 'Press Enter'])
    while not buttons.any():
        time.sleep(0.01)


# Do a tank move test.
print_and_wait('Test Tank')
tank.on_for_rotations(-50, 50, 2)

# Do a steering test
print_and_wait('Test Steering')
steerer.on_for_rotations(25, 50, 2)

# Spin the front motor.
print_and_wait('Test Front motor')
front_attachment.on_for_seconds(50, 2)

# Spin the back motor.
print_and_wait('Test Back motor')
back_attachment.on_for_seconds(50, 2)

'''
# Get reflected light intensity from the front color sensor.
while not buttons.any():
    display_ev3(['Front Color', 'Reflected', str(front_color.reflected_light_intensity), '', 'Press Enter'])

# Get color name from the front color sensor.
while not buttons.any():
    display_ev3(['Front Color', 'Reflected', front_color.color_name, '', 'Press Enter'])

# Get reflected light intensity from the mid color sensor.
while not buttons.any():
    display_ev3(['Mid Color', 'Reflected', str(mid_color.reflected_light_intensity), '', 'Press Enter'])

# Get color name from the mid color sensor.
while not buttons.any():
    display_ev3(['Mid Color', 'Reflected', str(mid_color.color_name), '', 'Press Enter'])

# Get angle from the Gyro sensor.
# gyro.reset()
while not buttons.any():
    display_ev3(['Gyro', 'Angle', str(gyro.angle), '', 'Press Enter'])

# Get rate from the Gyro sensor.
# gyro.reset()
while not buttons.any():
    display_ev3(['Gyro', 'Reset', str(gyro.rate), '', 'Press Enter'])

'''
# Get ultrasonic from the Ultrasonic Sensor
while not buttons.any():
    display_ev3(['Ultrasonic', 'CM', str(ultrasonic.distance_centimeters), '', 'Press Enter'])

