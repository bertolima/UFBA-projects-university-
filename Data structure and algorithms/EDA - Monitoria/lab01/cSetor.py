import pyglet
from pyglet import shapes
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
        minX = self.x
        maxX = self.x+self.largura
        minY = self.y 
        maxY = self.y+self.altura

        a = (setor.x, setor.y + setor.altura)
        b = (setor.x + setor.largura, setor.y + setor.altura)
        c = (setor.x + setor.largura, setor.y)
        d = (setor.x, setor.y)

        if (((minX < a[0] < maxX) and (minY < a[1] < maxY)) or
            ((minX < b[0] < maxX) and (minY < b[1] < maxY)) or
            ((minX < c[0] < maxX) and (minY < c[1] < maxY)) or
            ((minX < d[0] < maxX) and (minY < d[1] < maxY))):
            self.hasSobreposicao = True
            return True
        return False
    
    def makeShape(self, batch):
        return pyglet.shapes.Rectangle(self.x, self.y,self.largura, self.altura, color=(random.randint(0,255), random.randint(0,255), random.randint(0,255)), batch=batch)
    
    def getAreaSobreposta(self, setor):
        minX = self.x
        maxX = self.x+self.largura
        minY = self.y 
        maxY = self.y+self.altura

        a = (setor.x, setor.y + setor.altura)
        b = (setor.x + setor.largura, setor.y + setor.altura)
        c = (setor.x + setor.largura, setor.y)
        d = (setor.x, setor.y)

        if (((minX < a[0] < maxX) and (minY < a[1] < maxY)) and 
            ((minX < d[0] < maxX) and (minY < d[1] < maxY)) and
            ((minX < b[0] < maxX) and (minY < b[1] < maxY)) and
            ((minX < c[0] < maxX) and (minY < c[1] < maxY))):
            return a[0], a[1], c[0], c[1]
        
        if (((minX < a[0] < maxX) and (minY < a[1] < maxY)) and
            ((minX < d[0] < maxX) and (minY < d[1] < maxY))):
            return d[0], d[1], maxX, b[1]
        
        if (((minX < b[0] < maxX) and (minY < b[1] < maxY)) and
            ((minX < c[0] < maxX) and (minY < c[1] < maxY))):
            return minX, d[1], b[0], b[1]
        
        if (((minX < a[0] < maxX) and (minY < a[1] < maxY)) and
            ((minX < b[0] < maxX) and (minY < b[1] < maxY))):
            return a[0], minY, b[0], b[1]
         
        if (((minX < d[0] < maxX) and (minY < d[1] < maxY)) and
            ((minX < c[0] < maxX) and (minY < c[1] < maxY))):
            return d[0], d[1], b[0], maxY
                    
        if ((minX < a[0] < maxX) and (minY < a[1] < maxY)):
            return a[0], minY, maxX, b[1]
        
        if ((minX < b[0] < maxX) and (minY < b[1] < maxY)):
            return minX, minY, b[0], b[1]
        
        
        if ((minX < c[0] < maxX) and (minY < c[1] < maxY)):
            return minX, d[1], b[0], maxY
        
        if ((minX < d[0] < maxX) and (minY < d[1] < maxY)):
            return d[0], d[1], maxX, maxY
        
        
    def makeShapeSobreposta(self, setor, batch):
        x1, y1, x2, y2 = self.getAreaSobreposta(setor)
        width = x2-x1
        height = y2-y1
        self.areaSobreposicao = self.areaSobreposicao + width*height
        return pyglet.shapes.Rectangle(x1, y1, width, height, color=(255, 255, 255), batch=batch)
    
        

        
                
        

        
    
            

        

        
        




    