from microbit import *
while True:
  if pin0.is_touched():
    display.scroll(“You touched Pin 0!”)
  elif pin1.is_touched():
    display.scroll(“You touched Pin 1!”)
  elif pin2.is_touched():
    display.scroll(“You touched Pin 2!”)
