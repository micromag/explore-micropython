from microbit import *
steps = 0
while True:
    display.scroll(steps)
    sleep(50)
    if accelerometer. is_gesture(‘shake’):
        steps += 1
