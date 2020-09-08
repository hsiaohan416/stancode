"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

name: Sharon
file name: breakoutgraphics
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        self.window_width = window_width
        self.window_height = window_height
        self.paddle_width = paddle_width
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.color = 'grey'
        self.paddle.fill_color = 'grey'
        self.window.add(self.paddle, x=(self.window_width-self.paddle_width)/2, y=self.window_height-paddle_offset)
        onmousemoved(self.paddle_move)

        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window_width-ball_radius)/2, y=(window_height-ball_radius)/2)
        self.ball.color = 'darkgrey'
        self.ball.fill_color = 'darkgrey'

        # Starting label
        self.start_label = GLabel('-CLICK TO START-')
        self.start_label.color = 'darkgrey'
        self.start_label.font ='-30-bold'
        self.window.add(self.start_label, x=(self.window_width-self.start_label.width)/2, y=window_height/2+100)

        # Draw bricks.
        for i in range(brick_cols):
            for j in range(brick_rows):
                brick = GRect(brick_width, brick_height)
                self.window.add(brick, x=(brick_width + brick_spacing) * i,
                                y=brick_offset + (brick_height + brick_spacing) * j)
                if j / 2 < 1:
                    brick.color = 'lightpink'
                    brick.fill_color = 'lightpink'
                elif 1 <= j/2 < 2:
                    brick.color = 'gold'
                    brick.fill_color = 'gold'
                elif 2 <= j/2 < 3:
                    brick.color = 'darksalmon'
                    brick.fill_color = 'darksalmon'
                elif 3 <= j/2 < 4:
                    brick.color = 'gold'
                    brick.fill_color = 'lemonchiffon'
                else:
                    brick.color = 'rosybrown'
                    brick.fill_color = 'rosybrown'
        self.brick_num = BRICK_ROWS * BRICK_COLS

        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = 0
        self.ball_velocity()
        self.check_start = False

        # Score & life boards.
        self.score = 0
        self.score_board = GLabel(f'SCORE  {self.score}')
        self.score_board.color = 'orangered'
        self.score_board.font = '-20-bold'
        self.window.add(self.score_board, x=0, y=self.score_board.height+10)
        self.life_board = GLabel('Life ')
        self.life_board.color = 'orangered'
        self.life_board.font = '-20'
        self.window.add(self.life_board, x=self.window_width - self.life_board.width-70, y=self.life_board.height+10)

        # Initialize our mouse listeners.
        onmouseclicked(self.start)
        self.obj_brick = False
        self.obj_paddle = False
        self.check = None

    def paddle_move(self, event):
        self.paddle.x = event.x - self.paddle_width / 2
        if self.paddle.x <= 0:
            self.paddle.x = 0
        elif self.paddle.x + self.paddle_width >= self.window_width:
            self.paddle.x = self.window_width - self.paddle_width

    def ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = - self.__dx
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dy = - self.__dy

    def start(self, event):
        self.window.remove(self.start_label)
        self.check_start = True

    def get_x_speed(self):
        return self.__dx

    def get_y_speed(self):
        return self.__dy

    """
    Every time the ball moves, it will check whether touching any object or not.
    Three kinds of object presents in the window: paddle, score boards and bricks. 
    And we use two variables to decide: obj_paddle and obj_brick.
    When hitting the brick, the ball will remove it and the score will plus 1.
    """
    def check_collision(self):
        for i in range(int(self.ball.x), int(self.ball.x + self.ball.width + 1), int(self.ball.width)):
            for j in range(int(self.ball.y), int(self.ball.y + self.ball.height) + 1, int(self.ball.height)):
                self.check = self.window.get_object_at(i, j)
                if self.check is not None:
                    if self.check == self.paddle:
                        self.obj_paddle = True
                    elif self.check == self.score_board or self.check == self.life_board:
                        pass
                    else:
                        self.obj_brick = True
                        self.window.remove(self.check)
                        self.score += 1
                        self.score_board.text = 'SCORE  ' + str(self.score)
                    return self.obj_brick, self.obj_paddle
                else:
                    self.obj_brick = False
                    self.obj_paddle = False

    def reset_ball(self):
        self.window.add(self.ball, x=(self.window_width - self.ball.width)/2, y=(self.window_height - self.ball.height)/2)
        self.__dx = 0
        self.__dy = 0

