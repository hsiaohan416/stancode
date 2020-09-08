"""
File: bouncing_ball
Name:Sharon
-------------------------
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
times = 0
vy = 0
started = False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global started
    ball.filled = True
    window.add(ball, START_X, START_Y)
    while True:
        pause(DELAY)
        if started is False:
            onmouseclicked(bounce)
            started = True


def bounce(event):
    global times, vy, started
    while times < 3 and started is True:
        vy = vy + GRAVITY
        ball.move(VX, vy)
        if ball.y + SIZE >= window.height:
            """
            When the ball drops to the floor, it will bounce back with opposite
            direction and the velocity will reduce.
            """
            vy = -vy * REDUCE
            if vy > 0:
                vy = -vy
        if ball.x + SIZE >= window.width:
            """
            When the ball reaches the right-side bound, it means one round has been done.
            The ball will be put back to the starting place, 
            and the button will be removed to detect the further clicks.
            """
            ball.x = START_X
            ball.y = START_Y
            times += 1
            vy = 0
            started = False
        pause(DELAY)








if __name__ == "__main__":
    main()
