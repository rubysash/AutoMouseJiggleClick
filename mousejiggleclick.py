#!/usr/bin/env python
import pyautogui, sys           # need for click
import time                     # need for sleep
import random                   # randomizing
from datetime import datetime   # telling us the time

"""
Wiggles the mouse and clicks
Designed for stupid game that required mindless clicks

only tested on windows 10
install modules:
pip3 install pyautogui
"""
 
# basic config, min max in seconds
min_ = 8
max_ = 12

# starting count at 1, used for modulus
cnt = 1

print('Press Ctrl-C to quit or wiggle between min/max variables.')

def clicker(n):
    # generate random timer to sleep
    somerand = random.randint(min_,max_)
    time.sleep(somerand)
    
    # what is our xy position?
    x, y = pyautogui.position()

    # click right here
    pyautogui.click()

    # wouldn't release or move to next loop without this
    pyautogui.press('esc') 

    # notify user/log
    print("x: ", x, "\ty:", y, "\tt: ", datetime.now(), "\t(+" + str(somerand) + "s)")
    
    # wiggle mouse a bit
    pyautogui.moveTo(x+n,y+n)


# try/except so we can capture a ctrl+c without error
try:
    while(cnt):
        # looping and going to 1 and 2
        # so we can wiggle mouse to keep screen up
        # passes wiggle based on modulus
        cnt += 1
        if cnt % 2 == 0:
            clicker(2)
        else:
            clicker(-2)

        # not sure if this is required.
        #sys.stdout.flush()

except KeyboardInterrupt:
    print('\n')



 