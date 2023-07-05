import pyglet

class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3, batch, depth):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.erro = 0
        self.c1 = pyglet.shapes.Line(x1,y1,x2,y2, color =(100, 100, 100), batch=batch)
        self.c2 = pyglet.shapes.Line(x2,y2,x3,y3, color =(100, 100, 100), batch=batch)
        self.c3 = pyglet.shapes.Line(x1,y2,x3,y3, color =(100, 100, 100), batch=batch)
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
    
    def divide(self, batch, img):
        if (self.calcularIntensidadeMedia(img) < 10):
            return
        xm = (self.x1+self.x2)/2
        ym = (self.y1+self.y2)/2

        self.left = Triangle(self.x1, self.y1, self.x3, self.y3, xm, ym, batch, self.depth+1)
        self.right = Triangle(self.x3, self.y3, self.x2, self.y2, xm, ym, batch, self.depth+1)

        self.left.divide(batch, img)
        self.right.divide(batch, img)

    def calcularIntensidadeMedia(self, img):

        img_data = img.get_image_data()

        pixel_data = img_data.get_data('L', img_data.width)

        #calculo de ponto medio
        x1 = (self.x3 + self.x1)/2
        y1 = (self.y3 + self.y1)/2
        x2 = (self.x3 + self.x2)/2
        y2 = (self.y3 + self.y2)/2
        x3 = (self.x1 + self.x2)/2
        y3 = (self.y1 + self.y2)/2

        xCentro = (x1 + x2 + x3) / 3
        yCentro = (y1 + y2 + y3) / 3

        indexCentro = int(yCentro * img.width + xCentro)
        intensidadeCentro = pixel_data[indexCentro]

        #calculo de intensidade nos 3 pontos que formam o triangulo
        total = (img.width * img.height) -1
        index1 = min(max(int(self.x1 * img.width + self.y1) -1, 0), total)
        index2 = min(max(int(self.x2 * img.width + self.y2) -1, 0), total)
        index3 = min(max(int(self.x3 * img.width + self.y3) -1, 0), total)
        intensidade1 = pixel_data[index1]
        intensidade2 = pixel_data[index2]
        intensidade3 = pixel_data[index3]

        media_intensidades = (intensidade1 + intensidade2 + intensidade3) // 3

        # Calcular o erro médio do triângulo
        erroMedio = media_intensidades - intensidadeCentro
        erroMedio = int(abs(erroMedio))
        print("O erro medio é:", erroMedio)
        return erroMedio
        
    
        

    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right



    

        