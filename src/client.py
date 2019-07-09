import settings
import gamewindow as window
import pyglet

if __name__ == "__main__":
    window.GameWindow(
        width=settings.WINDOW_WIDTH,
        height=settings.WINDOW_HEIGHT)
    pyglet.app.run()
    print("end")
