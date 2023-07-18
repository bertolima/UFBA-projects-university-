from Screen import Screen
import pyglet


if __name__ == '__main__':

    img = pyglet.image.load("./DEMs/Terreno0.5k.jpg")
    screen = Screen(img)
    pyglet.app.run()