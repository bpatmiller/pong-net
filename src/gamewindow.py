import pyglet
import game
import settings

class GameWindow(pyglet.window.Window):
    game = None
    keys = None

    def __init__(self, *args, **kwargs):
        pyglet.window.Window.__init__(self, *args, **kwargs)
        self.game = game.Game(multi=False)
        self.keys = pyglet.window.key.KeyStateHandler()
        self.push_handlers(self.keys)
    
    def parse_input(self):
        if self.keys[pyglet.window.key.UP] and self.game.my_paddle.top_bounds < settings.WINDOW_HEIGHT:
            self.game.my_paddle.move(0, 5)
        if self.keys[pyglet.window.key.DOWN] and self.game.my_paddle.y > 0:
            self.game.my_paddle.move(0, -5)

    def on_draw(self):
        self.clear()
        self.parse_input()
        self.game.draw()
        self.game.ball.draw()
        self.game.score.draw()
        self.game.paddle_left.draw()
        self.game.paddle_right.draw()