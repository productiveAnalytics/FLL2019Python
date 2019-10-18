#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_C, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds

# Add code here
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

# drive in a turn for 5 rotations of the outer motor
# the first two parameters can be unit classes or percentages.
tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 10)

# drive in a different turn for 3 seconds
# tank_drive.on_for_seconds(SpeedPercent(60), SpeedPercent(60)
