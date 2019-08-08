from microbit import *
seconds = 0
while True:
    if button_a.is_pressed:
        if seconds < 20:
            seconds += 1
            display.scroll(seconds)
    if button_b.is_pressed:
        for i in range (seconds):
            display.scroll(seconds)
            sleep(1000)
            seconds -= 1
        display.show(Image.NO)
