from cSetor import *
import random

window_width = 1000

class Screen:
    def __init__(self, nSetores):
        self.nSetores = nSetores
        self.window = pyglet.window.Window(window_width, window_width)
        self.setores = []
        self.setoresShape = []
        self.setoresColisionShape = []
        self.batch = pyglet.graphics.Batch()
        self.initSetor()
        self.initSetorShapes()
        self.initSetoresColisao()
        self.estatisticas()
        self.on_draw = self.window.event(self.on_draw)


    def on_draw(self):
        self.window.clear()
        self.batch.draw()
    
    def initSetor(self):
        for i in range(self.nSetores): 
            self.setores.append(Setor(random.randint(50, 150), random.randint(50, 150), random.randint(100, 800), random.randint(100, 800)))

    def initSetorShapes(self):
        for setor in self.setores:
            self.setoresShape.append(setor.makeShape(self.batch))
    def initSetoresColisao(self):
        for setor1 in self.setores:
            for setor2 in self.setores:
                if (setor2 == setor1):
                    continue
                if (setor1.contains(setor2)):
                    self.setoresColisionShape.append(setor1.makeShapeSobreposta(setor2, self.batch))
    
    def getSetores(self):
        return self.setores

    def end(self):
        pyglet.app.run()

    def estatisticas(self):
        areaTotal = 0
        areaSobreposicao = 0
        nSetores = 0
        setoreswithSob = 0

        for setor in self.setores:
            if (setor.isSobreposto()):
                setoreswithSob = setoreswithSob + 1
            nSetores += 1
            areaTotal = areaTotal + setor.getArea()
            areaSobreposicao = areaSobreposicao + setor.getSobreposta()

        print("Porcentagem de setores que tem sobreposição: ", round((setoreswithSob/nSetores*100), 2), "%", sep="")
        print("Porcentual médio da área de sobreposição: ", round((areaSobreposicao/areaTotal*100),2), "%", sep="")


        

