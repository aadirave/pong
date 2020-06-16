import pygame as pg

# constants

WIDTH = 1200
HEIGHT = 600
BORDER = 20
VELOCITY = 1

# my colours

bg_colour = pg.color.Color('black')  # background colour
fg_colour = pg.color.Color('green')  # foreground colour
ball_colour = pg.color.Color('green')  # ball colour
paddle_colour = pg.color.Color('green')  # paddle colour

# temp variables
running = True

# screen for the game
screen = pg.display.set_mode((WIDTH, HEIGHT))

# refresh function and function to ask for retry
def refresh():
    pg.display.flip()

# classes

class Ball:

    # radius of the ball
    RADIUS = 20

    # positions
    X = 0
    Y = 0

    # velocities
    velX = 0
    velY = 0

    # overloaded constructor
    def __init__(self):
        pass
    def __init__(self, x, y, velX_ = 1, velY_ = 1):

        # positions

        self.X = x
        self.Y = y

        # velocities

        self.velX = velX_
        self.velY = velY_

    def show(self, surface = screen, colour = ball_colour):
        global screen
        pg.draw.circle(screen, colour, (self.X, self.Y), Ball.RADIUS)

    def update(self):
        newX = self.X + self.velX
        newY = self.Y + self.velY

        # checks if paddle has hit ball
        if newX > WIDTH - BORDER and paddle.Y < newY < paddle.Y + paddle.HEIGHT:
            self.velX = -self.velX
        else:
            pass

        # collisions with walls

        if newX < BORDER + self.RADIUS:
            self.velX = -self.velX
        elif newY < BORDER + self.RADIUS or newY > HEIGHT - BORDER - self.RADIUS:
            self.velY = -self.velY
        else:
            self.show(colour = bg_colour)

            self.X += self.velX
            self.Y += self.velY

            self.show(colour = ball_colour)


class Paddle:

    # dimensions

    WIDTH = 20
    HEIGHT = 200

    # positions

    Y = 0

    def __init__(self):
        pass
    def __init__(self, y):
        self.Y = y

    def show(self, surface = screen, colour = paddle_colour):
        pg.draw.rect(screen, colour, pg.Rect((WIDTH - self.WIDTH, self.Y), ((self.HEIGHT // 2), self.HEIGHT)))

    def update(self):
        self.show(colour = bg_colour)
        self.Y = pg.mouse.get_pos()[1]
        self.show(colour = paddle_colour)


# objects

ball = Ball(WIDTH - Ball.RADIUS, HEIGHT // 2, -VELOCITY, -VELOCITY)
paddle = Paddle(HEIGHT // 2)

# main

pg.draw.rect(screen, fg_colour, pg.Rect((0, 0), (WIDTH, BORDER)))
pg.draw.rect(screen, fg_colour, pg.Rect((0, 0), (BORDER, HEIGHT)))
pg.draw.rect(screen, fg_colour, pg.Rect((0, HEIGHT - BORDER), (WIDTH, BORDER)))

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    ball.update()
    paddle.update()

    refresh()

pg.quit()
