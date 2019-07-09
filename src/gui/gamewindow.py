import pyglet
import game

class GameWindow(pyglet.window.Window):
    game = None
    keys = None

    def __init__(self, *args, **kwargs):
        pyglet.window.Window.__init__(self, *args, **kwargs)
        self.game = game.Game()
        self.keys = pyglet.window.key.KeyStateHandler()
        self.push_handlers(self.keys)
    
    def parse_input(self):
        if self.keys[pyglet.window.key.UP]: #and self.game.paddle.y < height:
            print("move up")
            self.game.my_paddle.move(0, 1)
        if self.keys[pyglet.window.key.DOWN] and self.game.paddle.y > 0:
            print("move down")
            self.game.my_paddle.move(0, -1)

    def on_draw(self):
        self.clear()
        self.parse_input()
        self.game.draw()
        self.game.ball.draw()
        self.game.score.draw()
        self.game.paddle_left.draw()
        self.game.paddle_right.draw()