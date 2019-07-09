import simplejson as json
import game.gamewindow as window
import pyglet

if __name__ == "__main__":
    with open('settings.json') as sj:
        config = json.load(sj)
    window.MainWindow(
        width=config["WINDOW_WIDTH"],
        height=config["WINDOW_HEIGHT"])
    pyglet.app.run()
