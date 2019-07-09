import gui.sprite as sprite

class Ball(sprite.Sprite):
    horiz_speed = 1.0
    vert_speed = 0.75

    def collide_paddle(self):
        self.horiz_speed = - self.horiz_speed

    def collide_wall(self):
        self.vert_speed = -self.vert_speed

    def move(self):
        self.move(self.horiz_speed, self.vert_speed)