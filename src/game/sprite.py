import pyglet

class Sprite(pyglet.sprite.Sprite):
    image = None
    
    def __init__(self, image, x=0, y=0, blend_src=770, blend_dest=771, batch=None, group=None, usage='dynamic'):
        """ create pyglet sprite with default options
        """
        pyglet.sprite.Sprite.__init__(self, image, x, y, blend_src, blend_dest, batch, group, usage)
        self.image = image

    @property
    def left_bounds(self):
        return self.x

    @property
    def right_bounds(self):
        return self.x + self.width

    @property
    def bottom_bounds(self):
        return self.y

    @property
    def top_bounds(self):
        return self.y + self.height

    def move(self, x, y)
        self.set_position(self.x + x, self.y + y)

    def check_collision(self, candidates):
        for sprite in candidates:
            if (self.bottom_bounds <= sprite.top_bounds and self.top_bounds>=sprite.bottom_bounds and self.right_bounds>=sprite.left_bounds and self.left_bounds<=self.right_bounds):
                return sprite
                
    def check_oob(self, window_height):
        if self.top_bounds > window_height or self.bottom_bounds < 0:
            return True