import pyglet
import math

class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3, depth):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.flag = None
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
        self.right = Triangle(self.x3, self.y3,self.x2, self.y2,  xm, ym, self.depth+1)

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
        x3 = int(math.ceil(self.x3))
        y3 = int(math.ceil(self.y3))
        x1 = int(math.ceil(self.x1))
        y1 = int(math.ceil(self.y1))
        x2 = int(math.ceil(self.x2))
        y2 = int(math.ceil(self.y2))

        if (y3 > y1):
            aux = y1
            y1 = y3
            y3 = aux
        if (y3 > y2):
            aux = y2
            y2 = y3
            y3 = aux
        if (x3 > x2):
            aux = x2
            x2 = x3
            x3 = aux
        if (x3 > x1):
            aux = x1
            x1 = x3
            x3 = aux

        for x in range(x3, x2):
            for y in range(y3, y1):
                if (self.contains(x,y)):
                    index = y * imgWidth + x
                    intensidade = pixel_data[index]
                    sum += intensidade
                    nPixel +=1
                    if intensidade > eMax: eMax = intensidade
                    elif intensidade < eMin: eMin = intensidade

			# incrementa o contador de elevações do valor encontrado no pixel/amostra


        if (nPixel == 0):
            eMed = 0
        else:
            eMed = sum/nPixel
        if (abs(eMin - eMed) < flag):return True
        if (abs(eMax - eMed) < flag):return True
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



    

        