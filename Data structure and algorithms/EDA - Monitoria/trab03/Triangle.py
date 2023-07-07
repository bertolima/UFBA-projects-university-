import pyglet
import math

def swap(x,y):
    aux = x
    x = y
    y = aux

def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2.0)

class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3, depth):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.depth = depth
        self.left = None
        self.right = None
    
    def getx1(self):
        return self.x1
    
    def gety1(self):
        return self.y1
    
    def getx2(self):
        return self.x2
    
    def gety2(self):
        return self.y2
    
    def getx3(self):
        return self.x3
    
    def gety3(self):
        return self.y3
    
    def divide(self, depth):
        if (self.depth > depth): return
        xm = (self.x1+self.x2)/2
        ym = (self.y1+self.y2)/2

        self.left = Triangle(self.x1, self.y1, self.x3, self.y3, xm, ym, self.depth+1)
        self.right = Triangle(self.x3, self.y3, self.x2, self.y2, xm, ym, self.depth+1)

        self.left.divide(depth)
        self.right.divide(depth)
    
    def contains(self, x, y):
        orientacao1 = (self.x2 - self.x1) * (y - self.y1) - (x - self.x1) * (self.y2 - self.y1)
        orientacao2 = (self.x3 - self.x2) * (y - self.y2) - (x - self.x2) * (self.y3 - self.y2)
        orientacao3 = (self.x1 - self.x3) * (y - self.y3) - (x - self.x3) * (self.y1 - self.y3)

        if (orientacao1 >= 0 and orientacao2 >= 0 and orientacao3 >= 0) or (orientacao1 <= 0 and orientacao2 <= 0 and orientacao3 <= 0):
            return True
        return False

    def calcularIntensidadeMedia(self, pixel_data, imgWidth, imgHeight, flag):
        eMin = 256
        eMax = 0
        sum = 0
        nPixel = 0
        elements = []
    

        x3 = int(min(self.x1, self.x2, self.x3))
        x2 = int(max(self.x1, self.x2, self.x3))
        y3 = int(min(self.y1, self.y2, self.y3))
        y1 = int(max(self.y1, self.y2, self.y3))

        for x in range(x3+1, x2):
            for y in range(y3+1, y1):
                if (self.contains(x,y)):
                    index = y * imgWidth + x
                    intensidade = pixel_data[index]
                    sum += intensidade
                    nPixel +=1
                    elements.append(intensidade)
                    if intensidade > eMax: eMax = intensidade
                    elif intensidade < eMin: eMin = intensidade


        if (nPixel == 0):
            eMed = 0
        else:
            eMed = sum/nPixel

        desvio = 0
        for i in range(len(elements)):
            desvio += math.pow(intensidade-eMed, 2)
        
        desvio /= len(elements)
        desvio = math.sqrt(desvio)

        if (desvio < 5): return True
        return False
    



    
    def drawFull(self, maxDepth, shapes, batch):
        if (self.depth > maxDepth): return
        if(self.depth == 0):
            shapes.append(pyglet.shapes.Line(self.x1,self.y1,self.x2,self.y2, color =(100, 100, 100), batch=batch))
        else:
            shapes.append(pyglet.shapes.Line(self.x1,self.y1,self.x3,self.y3, color =(100, 100, 100), batch=batch))
    
        self.left.drawFull(maxDepth, shapes, batch)
        self.right.drawFull(maxDepth, shapes, batch)

    def drawLevel(self, maxDepth, shapes, batch, pixelList, imgWidth, imgHeight, flag):
        if (self.depth > maxDepth): return
        if (self.calcularIntensidadeMedia(pixelList, imgWidth, imgHeight, flag)): return
        shapes.append(pyglet.shapes.Line(self.x1,self.y1,self.x2,self.y2, color =(100, 100, 100), batch=batch))
        shapes.append(pyglet.shapes.Line(self.x1,self.y1,self.x3,self.y3, color =(100, 100, 100), batch=batch))
        shapes.append(pyglet.shapes.Line(self.x2,self.y2,self.x3,self.y3, color =(100, 100, 100), batch=batch))
        
        self.left.drawLevel(maxDepth, shapes, batch, pixelList, imgWidth, imgHeight, flag)
        self.right.drawLevel(maxDepth, shapes, batch, pixelList, imgWidth, imgHeight, flag)
    
    def addLevel(self):
        if (self.left != None):
            self.left.addLevel()
        else:
            xm = (self.x1+self.x2)/2
            ym = (self.y1+self.y2)/2

            self.left = Triangle(self.x1, self.y1, self.x3, self.y3, xm, ym, self.depth+1)
            self.right = Triangle(self.x3, self.y3, self.x2, self.y2, xm, ym, self.depth+1)
            return

        if (self.right != None):
            self.right.addLevel()
        else:
            xm = (self.x1+self.x2)/2
            ym = (self.y1+self.y2)/2

            self.left = Triangle(self.x1, self.y1, self.x3, self.y3, xm, ym, self.depth+1)
            self.right = Triangle(self.x3, self.y3, self.x2, self.y2, xm, ym, self.depth+1)
            return
        


            
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right



    

        