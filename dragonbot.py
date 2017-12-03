import Robot_client

__author__ = 'scottumsted'
import time

robot_debug = False
robot_speed = 100

LONG_DURATION = 1.0
SHORT_DURATION = 0.25
MEDIUM_DURATION = 0.5


def pause(t=MEDIUM_DURATION, sleep=False):
    if t > 5.0:
        duration = 5.0
    elif t < .2:
        duration = .2
    else:
        duration = t
    if sleep:
        time.sleep(duration)
    return duration


def forward(duration=LONG_DURATION):
    print('robot_controller, forward, robot_debug =', robot_debug)
    if not robot_debug:
        seconds = pause(duration)
        Robot_client.Robot_forward(robot_speed, seconds)


def backward(duration=LONG_DURATION):
    print('robot_controller, backward, robot_debug =', robot_debug)
    if not robot_debug:
        seconds = pause(duration)
        Robot_client.Robot_backward(robot_speed, seconds)


def left(duration=SHORT_DURATION):
    print('robot_controller, left, robot_debug =', robot_debug)
    if not robot_debug:
        seconds = pause(duration)
        Robot_client.Robot_left_glide(robot_speed, seconds)


def left_rot(duration=SHORT_DURATION):
    print('robot_controller, left_rot, robot_debug =', robot_debug)
    if not robot_debug:
        seconds = pause(duration)
        Robot_client.Robot_left(robot_speed, seconds)


def right(duration=SHORT_DURATION):
    print('robot_controller, right, robot_debug =', robot_debug)
    if not robot_debug:
        seconds = pause(duration)
        Robot_client.Robot_right_glide(robot_speed, seconds)


def right_rot(duration=SHORT_DURATION):
    print('robot_controller, right_rot, robot_debug =', robot_debug)
    if not robot_debug:
        seconds = pause(duration)
        Robot_client.Robot_right(robot_speed, seconds)


def stop(duration=MEDIUM_DURATION):
    print('robot_controller, stop, robot_debug =', robot_debug)
    if not robot_debug:
        Robot_client.Robot_stop()
        pause(duration, True)


def set_speed(speed):
    robot_speed = speed
    if not robot_debug:
        Robot_client.Robot__left_speed(speed)
        Robot_client.Robot__right_speed(speed)


def bwd():
    backward()


def fwd():
    forward()


def distance():
    d = 0
    return d


def blink(times=5):
    pass


def volt():
    v = 0
    return v


def servo(position):
    pass


if __name__ == '__main__':
    robot_debug = False
    # left(.5)
    # right(1)
    # forward(2)
    # stop()
    # backward(10)
    # distance()
    quit = False
    while not quit:
        direction = raw_input("WASD with X=stop : ")
        if direction.upper() == 'W':
            forward(1)
        elif direction.upper() == 'S':
            backward(1)
        elif direction.upper() == 'A':
            left(1)
        elif direction.upper() == 'D':
            right(1)
        elif direction.upper() == 'X':
            stop()
