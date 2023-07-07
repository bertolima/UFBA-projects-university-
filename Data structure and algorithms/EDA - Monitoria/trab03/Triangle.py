import pyglet

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

    def calcularIntensidadeMedia(self, pixel_data, imgWidth, imgHeight, flag):

        #calculo de ponto medio
        x1 = (self.x3 + self.x1)/2
        y1 = (self.y3 + self.y1)/2
        x2 = (self.x3 + self.x2)/2
        y2 = (self.y3 + self.y2)/2
        x3 = (self.x1 + self.x2)/2
        y3 = (self.y1 + self.y2)/2

        xCentro = (x1 + x2 + x3) / 3
        yCentro = (y1 + y2 + y3) / 3

        indexCentro = int(yCentro * imgWidth + xCentro)
        intensidadeCentro = pixel_data[indexCentro]

        #calculo de intensidade nos 3 pontos que formam o triangulo
        total = imgWidth*imgHeight-1
        index1 = int(self.y1 * imgWidth + self.x1)
        index2 = int(self.y2 * imgWidth + self.x2)
        index3 = int(self.y3 * imgWidth + self.x3)
    
        print(index1)
        intensidade1 = pixel_data[index1]
        intensidade2 = pixel_data[index2]
        intensidade3 = pixel_data[index3]
        

        media_intensidades = (intensidade1 + intensidade2 + intensidade3) // 3

        # Calcular o erro médio do triângulo
        erroMedio = int(abs(media_intensidades - intensidadeCentro))
        if(abs(intensidade1-intensidade2) > flag or abs(intensidade1-intensidade3) > flag or abs(intensidade2-intensidade3) > flag): self.flag =  False
        else: self.flag = True
    
    def drawFull(self, maxDepth, shapes, batch):
        if (self.depth > maxDepth): return
        if(self.depth == 0):
            shapes.append(pyglet.shapes.Line(self.x1,self.y1,self.x2,self.y2, color =(100, 100, 100), batch=batch))
        else:
            shapes.append(pyglet.shapes.Line(self.x1,self.y1,self.x3,self.y3, color =(100, 100, 100), batch=batch))
    
        self.left.drawFull(maxDepth, shapes, batch)
        self.right.drawFull(maxDepth, shapes, batch)

    def drawLevel(self, maxDepth, shapes, batch, pixelList, imgWidth, imgHeight, flag):
        self.calcularIntensidadeMedia(pixelList, imgWidth, imgHeight, flag)
        if (self.depth > maxDepth): return
        if (self.flag): return
        if(self.depth == 0):
            shapes.append(pyglet.shapes.Line(self.x1,self.y1,self.x2,self.y2, color =(100, 100, 100), batch=batch))
        else:
            shapes.append(pyglet.shapes.Line(self.x1,self.y1,self.x2,self.y2, color =(100, 100, 100), batch=batch))
        
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



    

        