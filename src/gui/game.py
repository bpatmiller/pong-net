import socket, pyglet
import gui.settings as settings
from gui.paddle import Paddle
from gui.ball import Ball

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
            pyglet.clock.schedule_interval(self.ball.move, 0.005)
            self.running = True

    def draw(self):
        # if self.multi:
            # self.draw_multi()
        # else:
        self.draw_single()

    def draw_single():
        pass

    def load_sprites(self):
        self.score = pyglet.text.Label('', font_size=12, x=settings.WINDOW_WIDTH/2, y=settings.WINDOW_WIDTH/2, anchor_x='center', anchor_y='center')
        self.ball = Ball(pyglet.resource.image(settings.BALL_IMG))
        self.paddle_left = Paddle(pyglet.resource.image(settings.PADDLE_IMG))
        self.paddle_right = Paddle(pyglet.resource.image(settings.PADDLE_IMG))
        self.paddle_right.x = settings.WINDOW_WIDTH - self.paddle_right.width
        self.my_paddle = self.paddle_left

    