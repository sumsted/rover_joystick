'''
Use pyglet for joystick reads.
Write joystick position to shared memory using mmap.
'''
import pyglet
from pyglet.gl import *
from pprint import pprint
import mmap
import contextlib


joysticks = pyglet.input.get_joysticks()
assert joysticks, 'No joystick device is connected'
joystick = joysticks[0]
joystick.open()
direction_threshold = .8
window = pyglet.window.Window()


@window.event
def on_draw():
    robot_direction(joystick.x, joystick.y, joystick.rz)
    pprint(vars(joystick))


def mm_write(x=0,y=0,z=0):
    mm.seek(0)
    mm[0] = chr(x)
    mm[1] = chr(y)
    mm[2] = chr(z)
    mm.flush()


def robot_direction(left_right_axis, fwd_bwd_axis, dead_switch=-1.0):
    print("left_right_axis: %f, fwd_bwd_axis: %f" %
          (left_right_axis, fwd_bwd_axis))

    if dead_switch > direction_threshold:
        if fwd_bwd_axis > -direction_threshold and fwd_bwd_axis < direction_threshold and left_right_axis < -direction_threshold:
            mm_write(7,0,0)
        elif fwd_bwd_axis > -direction_threshold and fwd_bwd_axis < direction_threshold and left_right_axis > direction_threshold:
            mm_write(8,0,0)
        elif fwd_bwd_axis < -direction_threshold and left_right_axis < direction_threshold and left_right_axis > -direction_threshold:
            mm_write(3,0,0)
        elif fwd_bwd_axis > direction_threshold and left_right_axis < direction_threshold and left_right_axis > -direction_threshold:
            mm_write(4,0,0)
        else:
            mm_write(2,0,0)
    else:
        print('stop')
        mm_write(2,0,0)


if __name__=='__main__':

    with open('joystick_position.txt', 'r+') as fp:
        with contextlib.closing(mmap.mmap(fp.fileno(), 0)) as mm:
            pyglet.clock.schedule_interval(lambda dt: None, .25)
            pyglet.app.run()
