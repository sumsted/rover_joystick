import requests

host = 'http://192.168.42.1:8080'

# host = 'http://127.0.0.1:8091'



def g(action, *args):
    url = host+'/'+action
    for arg in args:
        url += '/'+str(arg)
    r = requests.get(url)
    return r.json()


def Robot___init__(addr, left_id, right_id, left_trim, right_trim, stop_at_exit):
    return g('Robot___init__', addr, left_id, right_id, left_trim, right_trim, stop_at_exit)['return_value']


def Robot__left_speed(speed):
    return g('Robot__left_speed', speed)['return_value']


def Robot__right_speed(speed):
    return g('Robot__right_speed', speed)['return_value']


def Robot_stop():
    return g('Robot_stop', )['return_value']


def Robot_forward(speed, seconds):
    return g('Robot_forward', speed, seconds)['return_value']


def Robot_backward(speed, seconds):
    return g('Robot_backward', speed, seconds)['return_value']


def Robot_right(speed, seconds):
    return g('Robot_right', speed, seconds)['return_value']


def Robot_left(speed, seconds):
    return g('Robot_left', speed, seconds)['return_value']


def Robot_left_glide(speed, seconds):
    return g('Robot_left_glide', speed, seconds)['return_value']


def Robot_right_glide(speed, seconds):
    return g('Robot_right_glide', speed, seconds)['return_value']


if __name__ == '__main__':
    pass
