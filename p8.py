from microbit import *
while True:
    if accelerometer.is_gesture(‘shake’):
        temp = temperature()
        display.scroll(temp)
