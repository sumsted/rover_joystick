'''
1. read shared memory for command and params(not used).
2. call service on robot using dragonbot
3. wait a quarter second and repeat
'''
import mmap
import contextlib
import time
from dragonbot import *

commands = [['Robot__left_speed', 'speed'],
            ['Robot__right_speed', 'speed'],
            ['Robot_stop'],
            ['Robot_forward', 'speed', 'seconds'],
            ['Robot_backward', 'speed', 'seconds'],
            ['Robot_right', 'speed', 'seconds'],
            ['Robot_left', 'speed', 'seconds'],
            ['Robot_left_glide', 'speed', 'seconds'],
            ['Robot_right_glide', 'speed', 'seconds']]

with open('joystick_position.txt', 'r') as f:
    with contextlib.closing(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)) as m:
        while (1):
            m.seek(0)
            print('\nreading...')
            c= ord(m.read(1))
            command = commands[c]
            print('command = %s'% command[0])
            for param in command[1:]:
                print('%s = %d'%(param, ord(m.read(1))))

            if c == 2:
                stop()
            elif c == 3:
                forward()
            elif c == 4:
                backward()
            elif c == 5:
                right()
            elif c == 6:
                left()
            elif c == 7:
                left()
            elif c == 8:
                right()

            time.sleep(.25)
