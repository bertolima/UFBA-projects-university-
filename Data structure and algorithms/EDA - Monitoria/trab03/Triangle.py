import pyglet

class Triangle:
    def __init__(self, x1:float, y1:float, x2:float, y2:float, x3:float, y3:float, depth:int):
        #pontos que formam os vertices do triangulo
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.xm = None
        self.ym = None

        #pointer pra Null
        self.erro = None

        #profundidade do nó atual
        self.depth = depth

        #pointer pros filhos direito e esquerdo
        self.left = None
        self.right = None
    
    #divide o triangulo de forma recursiva
    def divide(self, depth):
        # se a profundidade atual for maior que a profundidade desejada paramos de dividir
        if (self.depth >= depth): return

        #o vertice correspondente ao angulo de 90 graus dos triangulos filhos é obtido dividindo a hipotenusa do triangulo atual por 2
        self.xm = (self.x1+self.x2)/2
        self.ym = (self.y1+self.y2)/2

        #criando os filhos
        self.left = Triangle(self.x1, self.y1, self.x3, self.y3, self.xm, self.ym, self.depth+1)
        self.right = Triangle(self.x3, self.y3, self.x2, self.y2, self.xm, self.ym, self.depth+1)

        #dando continuidade ao processo de subdivisao de forma recursiva
        self.left.divide(depth)
        self.right.divide(depth)
        
    def subdivide(self):
        self.xm = (self.x1+self.x2)/2
        self.ym = (self.y1+self.y2)/2

        #criando os filhos
        self.left = Triangle(self.x1, self.y1, self.x3, self.y3, self.xm, self.ym, self.depth+1)
        self.right = Triangle(self.x2, self.y2, self.x3, self.y3, self.xm, self.ym, self.depth+1)
    
    
    #essa função serve pra verificar se um ponto está contido dentro do triangulo
    def contains(self, x, y):
        orientacao1 = (self.x2 - self.x1) * (y - self.y1) - (x - self.x1) * (self.y2 - self.y1)
        orientacao2 = (self.x3 - self.x2) * (y - self.y2) - (x - self.x2) * (self.y3 - self.y2)
        orientacao3 = (self.x1 - self.x3) * (y - self.y3) - (x - self.x3) * (self.y1 - self.y3)

        if (orientacao1 >= 0 and orientacao2 >= 0 and orientacao3 >= 0) or (orientacao1 <= 0 and orientacao2 <= 0 and orientacao3 <= 0):
            return True
        return False

    #de forma resumida, calcula o desvio padrao dos pixels do triangulo, se o desvio padrao for alto continuamos a dividir, se for baixo paramos
    def calcularIntensidadeMedia(self, pixel_data, imgWidth):
        eMin = 256
        eMax = 0
        sum = 0
        nPixel = 0

        x3 = int(min(self.x1, self.x2, self.x3))
        x2 = int(max(self.x1, self.x2, self.x3))
        y3 = int(min(self.y1, self.y2, self.y3))
        y1 = int(max(self.y1, self.y2, self.y3))

        #loop que faz o calculo do numero de pixels percorridos e o valor total da intensidade desses pixels
        for x in range(x3+1, x2, 2):
            for y in range(y3+1, y1, 2):
                if (self.contains(x,y)):
                    index = y * imgWidth + x
                    intensidade = pixel_data[index]
                    sum += intensidade
                    nPixel +=1
                    if intensidade > eMax: eMax = intensidade
                    elif intensidade < eMin: eMin = intensidade

        #calculo da media da intensidade de pixel do triangulo
        if (nPixel == 0):
            eMed = 0
        else:
            eMed = sum/nPixel

        self.erro = max(abs(eMin - eMed), abs(eMax - eMed))
    
    #desenha a arvore toda
    def drawFull(self, maxDepth, shapes, batch):
        if (self.depth == maxDepth): return
        if(self.depth == 0):
            shapes.append(pyglet.shapes.Line(0,abs(self.x1-self.x3),abs(self.x1-self.x3),0, color =(255, 100,100,255), batch=batch))
        else:
            shapes.append(pyglet.shapes.Line(self.xm,self.ym,self.x3,self.y3, color =(255, 100, 100), batch=batch))
        self.left.drawFull(maxDepth, shapes, batch)
        self.right.drawFull(maxDepth, shapes, batch)



    #desenha a arvore por aproximação
    def drawLevel(self, maxDepth, shapes, batch, pixelList, imgWidth, imgHeight, flag):
        if (self.depth > maxDepth): return
        if (self.erro < flag): return
        if(self.depth == 0):
            shapes.append(pyglet.shapes.Line(self.x1,self.y1,self.x2,self.y2, color =(255, 100, 100), batch=batch))
        else:
            shapes.append(pyglet.shapes.Line(self.x1,self.y1,self.x3,self.y3, color =(255, 100, 100), batch=batch))
        
        self.left.drawLevel(maxDepth, shapes, batch, pixelList, imgWidth, imgHeight, flag)
        self.right.drawLevel(maxDepth, shapes, batch, pixelList, imgWidth, imgHeight, flag)
    
    #aumenta a profundidade da arvore em 1
    def addLevel(self):
        #enquanto o filho esquerdo for diferente de None eu continuo buscando um filho esquerdo que seja None
        if (self.left != None):
            self.left.addLevel()
        #quando eu acho um filho esquerdo igual a None, eu crio um filho esquerdo e um filho direito(como a profundidade é igual pra toda arvore n tem problema fazer isso)
        else:
            xm = (self.x1+self.x2)/2
            ym = (self.y1+self.y2)/2

            self.left = Triangle(self.x1, self.y1, self.x3, self.y3, xm, ym, self.depth+1)
            self.right = Triangle(self.x3, self.y3, self.x2, self.y2, xm, ym, self.depth+1)
            return

        #msm coisa da parte de cima, porém pro filho direito.
        if (self.right != None):
            self.right.addLevel()
        else:
            xm = (self.x1+self.x2)/2
            ym = (self.y1+self.y2)/2

            self.left = Triangle(self.x1, self.y1, self.x3, self.y3, xm, ym, self.depth+1)
            self.right = Triangle(self.x3, self.y3, self.x2, self.y2, xm, ym, self.depth+1)
            return
        
    def createShape(self, batch):
       return pyglet.shapes.Line(self.xm,self.ym,self.x3,self.y3, color =(255, 255,255,255), batch=batch)
        
    def getErro(self):
        return self.erro
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def getDepth(self):
        return self.depth

    def getSide(self):
        return self.side




    

        