import gui.settings as settings
import gui.gamewindow as window
import pyglet

if __name__ == "__main__":
    window.GameWindow(
        settings.WINDOW_WIDTH,
        settings.WINDOW_HEIGHT)
    pyglet.app.run()
