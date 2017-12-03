In joystick_write read the joystick using pyglet. Write the joystick position to shared memory using mmap.
In joystick_read read the position from shared memory to send to the robot.
Unable to send to the robot directly from the pyglet app as the call to the robot messes with the pyglet event loop and hangs the joystick read.
Using shared memory solves the problem.
