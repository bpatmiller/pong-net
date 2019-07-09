import socket, pyglet
import settings
from paddle import Paddle
from ball import Ball

class Game(pyglet.window.Window):
    paddle_left = None
    paddle_right = None
    my_paddle = None
    score = None
    multi = False
    running = False

    def __init__(self, multi=False):
        self.multi = multi
        self.load_sprites()
        #if self.multi:
        #    self.me, self.other = connect()

    def run(self):
        if not self.running:
            pyglet.clock.schedule_interval(self.ball.onmove, 0.005)
            self.running = True

    def collision(self):
        has_scored = self.ball.check_score()
        if has_scored == 1:
            self.paddle_left.score += 1
        elif has_scored == -1:
            self.paddle_right.score +=1

        player = self.ball.check_collision([self.paddle_left, self.paddle_left])
        if player:
            self.ball.collide_paddle()
        if self.ball.check_oob(settings.WINDOW_HEIGHT):
            self.ball.collide_wall()

    def draw(self):
        # if self.multi:
            # self.draw_multi()
        # else:
        self.draw_single()

    def draw_single(self):
        self.run()
        self.collision()

    def load_sprites(self):
        self.score = pyglet.text.Label('', font_size=12, x=settings.WINDOW_WIDTH/2, y=settings.WINDOW_WIDTH/2, anchor_x='center', anchor_y='center')
        self.ball = Ball(pyglet.resource.image(settings.BALL_IMG))
        self.ball.center()
        self.paddle_left = Paddle(pyglet.resource.image(settings.PADDLE_IMG))
        self.paddle_left.center_y()
        self.paddle_right = Paddle(pyglet.resource.image(settings.PADDLE_IMG))
        self.paddle_right.center_y()
        self.paddle_right.x = settings.WINDOW_WIDTH - self.paddle_right.width
        self.my_paddle = self.paddle_left

    