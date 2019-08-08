from microbit import *
import radio
radio.on()
while True:
    if button_a.is_pressed():
        radio.send(“Hello World”)
    incoming = radio.receive()
    if incoming = “Hello World”:
        display.scroll(“Hello World”)
