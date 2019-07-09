import socket
import pyglet
import settings
import sys
import simplejson as json
from paddle import Paddle
from ball import Ball


def connect():
    try:
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.connect((settings.SERVER_IP, settings.SERVER_PORT))
        me = str(connection.getsockname()[1])
        print("client connected to", settings.SERVER_IP, "with id", me)
        return [me, connection]
    except socket.error:
        print("error: client could not connect to socket")
        sys.exit(1)


class Game(pyglet.window.Window):
    paddle_left = None
    paddle_right = None
    my_paddle = None
    score = None
    multi = True
    running = False
    master_client = False

    def __init__(self):
        self.load_sprites()
        if self.multi:
            self.me, self.connection = connect()

    def run(self):
        if not self.running:
            pyglet.clock.schedule_interval(self.ball.onmove, 0.005)
            self.running = True

    def collision(self):
        has_scored = self.ball.check_score()
        if has_scored == 1:
            self.paddle_left.score += 1
        elif has_scored == -1:
            self.paddle_right.score += 1

        player = self.ball.check_collision(
            [self.paddle_left, self.paddle_right])
        if player:
            self.ball.collide_paddle()
        if self.ball.check_oob(settings.WINDOW_HEIGHT):
            self.ball.collide_wall()

    def draw(self):
        if self.multi:
            self.draw_multi()
        else:
            self.draw_single()

    def draw_single(self):
        self.run()
        self.collision()

    def load_sprites(self):
        self.score = pyglet.text.Label(
            '',
            font_size=12,
            x=settings.WINDOW_WIDTH / 2,
            y=settings.WINDOW_HEIGHT / 2,
            anchor_x='center',
            anchor_y='center')
        self.ball = Ball(pyglet.resource.image(settings.BALL_IMG))
        self.ball.center()
        self.paddle_left = Paddle(pyglet.resource.image(settings.PADDLE_IMG))
        self.paddle_left.center_y()
        self.paddle_right = Paddle(pyglet.resource.image(settings.PADDLE_IMG))
        self.paddle_right.center_y()
        self.paddle_right.x = settings.WINDOW_WIDTH - self.paddle_right.width
        self.my_paddle = self.paddle_left

    def order_players(self, server_response):
        if self.me == sorted(server_response.keys())[0]:
            self.master_client = True
            self.my_paddle = self.paddle_left
            self.enem_paddle = self.paddle_right
            self.score.text = '%i - master - %i' % (self.paddle_left.score, self.paddle_right.score)
        else:
            self.my_paddle = self.paddle_right
            self.enem_paddle = self.paddle_left
            self.score.text = '%i - slave - %i' % (self.paddle_left.score, self.paddle_right.score)

    def update_server(self):
        data = {
            "ball": {"x": self.ball.x, "y": self.ball.y, },
            "paddle": {"x": self.my_paddle.x, "y": self.my_paddle.y, },
            "score": {"left": self.paddle_left.score, "right": self.paddle_right.score, }
        }
        self.connection.send(json.dumps(data).encode())
        return json.loads(self.connection.recv(2000))

    def update_multi_positions(self, data):
        for pid in data.keys():
            try:
                if pid != self.me:
                    self.enem_paddle.y = data[pid]['paddle']['y']
                    if not self.master_client:
                        self.ball.x = data[pid]['ball']['x']
                        self.ball.y = data[pid]['ball']['y']
                        self.paddle_left.score = data[pid]["score"]["left"]
                        self.paddle_right.score = data[pid]["score"]["right"]
            except BaseException:
                pass

    def draw_multi(self):
        data = self.update_server()
        self.order_players(data)
        self.run()

        if self.master_client:
            self.collision()

        self.update_multi_positions(data)
