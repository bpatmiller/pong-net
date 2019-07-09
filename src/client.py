import settings
import sys
import gamewindow as window
import pyglet

if __name__ == "__main__":
    if len(sys.argv) > 1:
        settings.SERVER_IP = sys.argv[1]
    if len(sys.argv) > 2:
        settings.SERVER_PORT = sys.argv[2]
    window.GameWindow(
        width=settings.WINDOW_WIDTH,
        height=settings.WINDOW_HEIGHT)
    pyglet.app.run()
