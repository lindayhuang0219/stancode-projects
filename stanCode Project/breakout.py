"""
File: breakout.py
Name: Linda
----------------------------------
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

It's a game regarding to remove the bricks. If you remove all bricks, you win!
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120    # 120 frames per second.
NUM_LIVES = 3              # number of lives


def main():
    """
    You have the three lives in this game.
    You only can enter the game when you click the mouse at the first time.
    When the paddle doesn't catch the ball, you will lose one life, reset the place of the ball and the mouse data.
    When the ball collides the the boundaries, it will change the speed.
    When the bricks are removed over, the game is in the end and you win!
    When the number of lives reaches zero, the game is over and you lose!
    """
    graphics = BreakoutGraphics()
    life = NUM_LIVES
    while True:
        if life > 0 or graphics.how_many_bricks > 0:
            if graphics.count == 1:
                graphics.set_ball_velocity()
                while True:
                    graphics.ball.move(graphics.get_x_velocity(), graphics.get_y_velocity())
                    graphics.collision_and_bounce()
                    if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                        graphics.set_x_velocity()
                    if graphics.ball.y <= 0 or graphics.ball.y + graphics.ball.height >= graphics.window.height:
                        graphics.set_y_velocity()
                    if graphics.ball.y >= graphics.window.height - graphics.ball.height:
                        graphics.remove_ball()
                        life -= 1
                        graphics.window.add(graphics.ball, x=graphics.get_ball_start_x(), y=graphics.get_ball_start_y())
                        graphics.count = 0
                        break
                    if graphics.how_many_bricks == 0:
                        break
                    pause(FRAME_RATE)
                if graphics.how_many_bricks ==0:
                    break
                if life == 0:
                    break
        else:
            break
        pause(FRAME_RATE)
    graphics.window.add(graphics.ball, x=graphics.get_ball_start_x(), y=graphics.get_ball_start_y())

    # Add animation loop here!


if __name__ == '__main__':
    main()
