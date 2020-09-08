"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

name: Sharon
file name: breakout
"""

from campy.gui.events.timer import pause
from campy.graphics.gobjects import GLabel
from breakoutgraphics import BreakoutGraphics


FRAME_RATE = 1000 / 120  # 120 frames per second.
NUM_LIVES = 3


def main():
    graphics = BreakoutGraphics()
    life = NUM_LIVES
    dx = graphics.get_x_speed()
    dy = graphics.get_y_speed()
    life_label = ''
    for i in range(life):
        life_label += '♥︎'
    graphics.life_board.text = 'LIFE ' + life_label
    while True:
        pause(100)
        if graphics.check_start is True:
            life_label = ''
            while True:
                # Every time the ball moves, it will check whether touching any object or not.
                graphics.check_collision()
                if graphics.obj_brick is True:
                    dy = -dy
                if graphics.obj_paddle is True:
                    dy = -dy
                    if dy > 0:
                        dy = -dy

                # Let the ball bounce back when they are at the edges.
                if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width - graphics.ball.width:
                    dx = -dx
                if graphics.ball.y <= 0:
                    dy = -dy

                # When the ball fall down to the bottom,
                # the life will minus 1 and the ball will be moved back to the center.
                if graphics.ball.y >= graphics.window.height - graphics.ball.height:
                    life -= 1
                    for i in range(life):
                        life_label += '♥︎'
                    graphics.life_board.text = 'LIFE ' + life_label
                    graphics.reset_ball()
                    graphics.check_start = False
                    break

                # When all the bricks are removed:
                if graphics.score == graphics.brick_num:
                    graphics.reset_ball()
                    graphics.check_start = False
                    win_label = GLabel('YOU WIN :)')
                    win_label.font = '-25-bold'
                    graphics.window.add(win_label, x=(graphics.window_width - win_label.width) / 2,
                                        y=graphics.window_height / 2)
                    break

                graphics.ball.move(dx, dy)
                pause(FRAME_RATE)

            # When no life left, the game ends up.
            if life <= 0:
                game_over = GLabel('GAME OVER X_X')
                game_over.font = '-30-bold'
                graphics.window.add(game_over, x=(graphics.window_width-game_over.width)/2, y=graphics.window_height/1.5)
                break

            # When no bricks left, the game ends up.
            if graphics.score == graphics.brick_num:
                break










if __name__ == '__main__':
    main()
