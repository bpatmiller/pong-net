import pyglet

class GameWindow(pyglet.window.Window):
    width = 640
    height = 480

    def __init__(self, *args, **kwargs):
        pyglet.window.Window
        self.game = game.Game(multi=True)
        self.keys = pyglet.window.key.KeyStateHandler()
        self.input_handler(self.keys)
    
    def parse_input(self):
        if self.keys[pyglet.window.key.UP] and self.game.paddle.y < height:
            self.game.my_paddle.move(1)
        if self.keys[pyglet.window.key.DOWN] and self.game.paddle.y > 0:
            self.game.my_paddle.move(-1)

    def draw(self):
        self.clear()
        self.parse_input()
        self.game.draw()