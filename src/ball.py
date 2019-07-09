import msprite
import settings


class Ball(msprite.MSprite):
    horiz_speed = 2.0
    vert_speed = 1.5

    def collide_paddle(self):
        self.horiz_speed = - self.horiz_speed

    def collide_wall(self):
        self.vert_speed = -self.vert_speed

    def check_score(self):
        if self.x < 0:
            self.center()
            self.horiz_speed = - self.horiz_speed
            self.vert_speed = - self.vert_speed
            print("right player scored")
            return -1
        if self.x > settings.WINDOW_WIDTH:
            self.center()
            self.horiz_speed = - self.horiz_speed
            self.vert_speed = - self.vert_speed
            print("left player scored")
            return 1
        return 0

    def onmove(self, clock):
        self.move(self.horiz_speed, self.vert_speed)
