import pyglet
import random

class Setor:
    def __init__(self, largura=0, altura=0, x=0, y=0):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.perimetro = self.calcPerimetro()
        self.area = self.calcArea()
        self.hasSobreposicao = False
        self.areaSobreposicao = 0
        
    def calcPerimetro(self):
        return (self.largura*2 + self.altura*2)

    def calcArea(self):
        return (self.altura*self.largura)
    
    def getPosition(self):
        return self.x,self.y
    
    def setPosition(self, x, y):
        self.x = x
        self.y = y

    def getSize(self):
        return self.largura, self.altura
    
    def setSize(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def getPerimetro(self):
        return self.calcPerimetro()
    
    def getArea(self):
        return self.calcArea()
    
    def contains(self, setor):

        d1 = (self.x, self.y)
        b1 = (self.x+self.largura, self.y+self.altura)
        b2 = (setor.x + setor.largura, setor.y + setor.altura)
        d2 = (setor.x, setor.y)

        return ((d1[0] < b2[0] and b1[0] > d2[0]) and
                (b1[1] > b2[1] and d1[1] < b2[1]))
    
    def makeShape(self, batch):
        return pyglet.shapes.Rectangle(self.x, self.y,self.largura, self.altura, color=(random.randint(0,255), random.randint(0,255), random.randint(0,255)), batch=batch)
    
    def getOverlapPoints(self, setor):
        d1 = (self.x, self.y)
        b1 = (self.x+self.largura, self.y+self.altura)
        b2 = (setor.x + setor.largura, setor.y + setor.altura)
        d2 = (setor.x, setor.y)

        x1 = max(d1[0], d2[0])
        y1 = max(d1[1], d2[1])
        x2 = min(b1[0], b2[0])
        y2 = min(b1[1], b2[1])

        return x1, y1, x2, y2
        
    def makeOverlapShapes(self, setor, batch):
        x1, y1, x2, y2 = self.getOverlapPoints(setor)
        self.hasSobreposicao = True
        width = x2-x1
        height = y2-y1
        self.areaSobreposicao = self.areaSobreposicao + width*height
        return pyglet.shapes.Rectangle(x1, y1, width, height, color=(255, 255, 255), batch=batch)
    
    def getOverlapArea(self):
        return self.areaSobreposicao
    
    def isOverlap(self):
        return self.hasSobreposicao
    
        

        
                
        

        
    
            

        

        
        




    