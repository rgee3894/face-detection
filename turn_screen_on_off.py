import keyboard as kb
import ctypes

def screen_off():
  return ctypes.windll.user32.SendMessageW(65535, 274, 61808,2)

def screen_on():
  return ctypes.windll.user32.SendMessageW(65535, 274, 61808,-1)

'''
is_on = True

while True:
  if kb.is_pressed('o') and not is_on:
    print('on')
    is_on = True
    screen_on()
  elif kb.is_pressed('f') and is_on:
    print('off')
    screen_off()
    is_on = False
'''