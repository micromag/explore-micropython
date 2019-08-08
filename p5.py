from microbit import *
import random
while True:
    if button_a.is_pressed():
        if random.choice([True, False]):
            display.show(Image.HAPPY)
        else:
            display.show(Image.SAD)
