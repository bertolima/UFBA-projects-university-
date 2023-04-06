import pyglet
from cSetor import *
import random

class Screen:
    def __init__(self, nSetores=10):
        self.nSetores = nSetores
        self.window = pyglet.window.Window(1000, 1000)
        self.setores = []
        self.setoresShape = []
        self.setoresColisionShape = []
        self.batch = pyglet.graphics.Batch()
        self.initSetor()
        self.on_draw = self.window.event(self.on_draw)


    def on_draw(self):
        self.window.clear()
        self.batch.draw()
    
    def initSetor(self):
        for i in range(self.nSetores):
            setor1 = Setor(random.randint(100, 300), random.randint(100, 300), random.randint(100, 800), random.randint(100, 800))
            self.setores.append(setor1)
            self.setoresShape.append(setor1.makeShape(self.batch))
            if (i > 0):
                for setor in self.setores:
                    if (setor.contains(setor1)):
                        self.setoresColisionShape.append(setor.makeShapeSobreposta(setor1, self.batch))
    def preencherSetores(self):
        for i in range(self.nSetores):
            self.vetor.append(self.initSetor())


    def end(self):
        pyglet.app.run()

        

