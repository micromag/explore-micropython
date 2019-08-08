from microbit import *
import random
display.scroll("Shake Me")
while True:
    if accelerometer.was_gesture('shake'):
        shake = random.randint(1, 5)
        if shake == 1:
            display.show(1)
        if shake == 2:
            display.show(2)
        if shake == 3:
            display.show(3)
        if shake == 4:
            display.show(4)
        if shake == 5:
            display.show(5)
