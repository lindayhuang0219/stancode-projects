"""
File: breakoutgraphics.py
Name: Linda
----------------------------------
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

It's a game regarding to remove the bricks. If you remove all bricks, you win!
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

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x = (self.window.width-paddle_width)/2,
                        y = self.window.height-paddle_offset-paddle_height)


        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, self.window.width*1/2-ball_radius*2, self.window.height*1/2-ball_radius*2)
        self.ball_start_x = self.window.width*1/2-ball_radius*2
        self.ball_start_y = self.window.height*1/2-ball_radius*2

        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners.
        self.count = 0

        onmouseclicked(self.click)
        onmousemoved(self.paddle_move)

        # Draw bricks.
        for i in range(brick_rows):
            for j in range(brick_cols):

                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True

                fill_the_color(self.brick, i)
                self.window.add(self.brick, x=0+(brick_width+BRICK_SPACING)*j,
                                y=BRICK_OFFSET+(brick_height+BRICK_SPACING)*i)

        self.how_many_bricks = brick_rows*brick_cols

    def click(self, mouse):
        """
        int, how many times the user clicks the mouse
        :param mouse: the information which the coder get when the user clicks the mouse
        """
        self.count += 1

    def paddle_move(self, k):
        """
        int, the place of the paddle and set the boundaries of the paddle can move
        :param k: the place where the paddle is
        """
        self.paddle.x = k.x - PADDLE_WIDTH / 2
        self.paddle.y = self.window.height - PADDLE_OFFSET - PADDLE_HEIGHT

        if self.paddle.x >= self.window.width - PADDLE_WIDTH:
            self.paddle.x = self.window.width - PADDLE_WIDTH
        if self.paddle.x <= 0:
            self.paddle.x = 0

    def set_ball_velocity(self):
        """
        int, the velocity of the ball and change the horizontal speed randomly
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED

        if random.random( ) > 0.5:
            self.__dx = -self.__dx

    def collision_and_bounce(self):
        """
        check the object that the ball collides.
        If the ball collides the paddle, it will change the vertical speed.
        If the ball collides the brick, it will change the vertical speed and remove the brick.
        """
        ball_upperleft = self.window.get_object_at(self.ball.x, self.ball.y)
        ball_upperright = self.window.get_object_at(self.ball.x + 2*BALL_RADIUS, self.ball.y)
        ball_lowerleft = self.window.get_object_at(self.ball.x ,self.ball.y+2*BALL_RADIUS)
        ball_lowerright = self.window.get_object_at(self.ball.x + 2*BALL_RADIUS,self.ball.y+2*BALL_RADIUS)

        if ball_upperleft is not None:
            if ball_upperleft is not self.paddle:
                self.__dy *= -1
                self.window.remove(ball_upperleft)
                self.how_many_bricks -= 1
                print(self.how_many_bricks)
            if ball_upperleft is self.paddle:
                self.__dy = -INITIAL_Y_SPEED

        elif ball_upperright is not None:
            if ball_upperright is not self.paddle:
                self.__dy *= -1
                self.window.remove(ball_upperright)
                self.how_many_bricks -= 1
                print(self.how_many_bricks)
            if ball_upperright is self.paddle.x:
                self.__dy = -INITIAL_Y_SPEED

        elif ball_lowerleft is not None:
            if ball_lowerleft is not self.paddle:
                self.__dy *= -1
                self.window.remove(ball_lowerleft)
                self.how_many_bricks -= 1
                print(self.how_many_bricks)
            if ball_lowerleft is self.paddle:
                self.__dy = -INITIAL_Y_SPEED

        elif ball_lowerright is not None:
            if ball_lowerright is not self.paddle:
                self.__dy *= -1
                self.window.remove(ball_lowerright)
                self.how_many_bricks -= 1
                print(self.how_many_bricks)
            if ball_lowerright is self.paddle:
                self.__dy = -INITIAL_Y_SPEED

    def get_x_velocity(self):
        """
        :return: int, the horizontal speed for the ball
        """
        return self.__dx

    def get_y_velocity(self):
        """
        :return: int, the vertical speed for the ball
        """
        return self.__dy

    def set_x_velocity(self):
        """
        int, change the horizontal speed for the ball
        """
        self.__dx *= -1

    def set_y_velocity(self):
        """
        int, change the vertical speed for the ball
        """
        self.__dy *= -1

    def get_ball_start_x(self):
        """
        :return: int, the initial horizontal place of the ball
        """
        return self.ball_start_x

    def get_ball_start_y(self):
        """
        :return: int, the initial vertical place of the ball
        """
        return self.ball_start_y

    def remove_ball(self):
        """
        remove the ball from the window
        """
        self.window.remove(self.ball)


def fill_the_color(brick, i):
    """
    fill the color of the bricks
    :param brick: one of the GRect that will be removed when the ball collides
    :param i: number of rows of bricks
    """
    if i == 0 or i == 1:
        brick.fill_color = 'red'
        brick.color = 'red'
    elif i == 2 or i == 3:
        brick.fill_color = 'orange'
        brick.color = 'orange'
    elif i == 4 or i == 5:
        brick.fill_color = 'yellow'
        brick.color = 'yellow'
    elif i == 6 or i == 7:
        brick.fill_color = 'green'
        brick.color = 'green'
    elif i == 8 or i == 9:
        brick.fill_color = 'blue'
        brick.color = 'blue'



