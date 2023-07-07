import pyglet
from binaryTree import binaryTree


def lerImagem(arq):
        img = pyglet.image.load(arq)
        return img



class Screen:
    
    def __init__(self):

        self.img = pyglet.image.load("./DEMs/Terreno1K.png")

        self.width = self.img.width
        self.height = self.img.height

        self.pixel_data = self.img.get_image_data().get_data('I', self.width)

        self.drawFull = False
        self.drawLevel = False

        self.tree = None

        self.shapes = []

        self.depth = 10
        self.aproxLimit = 20
        
        
        window = pyglet.window.Window(self.width, self.height)
        self.Full = pyglet.graphics.Batch()
        self.Level = pyglet.graphics.Batch()
        
        def pressG():
             self.shapes.clear()
             if self.drawFull:
                  self.drawFull = False
                  self.shapes.clear()
             elif self.drawLevel:
                  self.drawLevel = False
                  self.drawFull = True
                  self.tree.drawFull(self.depth, self.shapes, self.Full)
             else:
                  self.drawFull = True
                  self.tree.drawFull(self.depth, self.shapes, self.Full)
        def pressK():
             self.shapes.clear()
             if self.drawLevel:
                  self.drawLevel = False
             elif self.drawFull:
                  self.drawFull = False
                  self.drawLevel = True
                  self.tree.drawLevel(self.depth, self.shapes, self.Level, self.pixel_data, self.width, self.height, self.aproxLimit)
             else:
                  self.drawLevel = True
                  self.tree.drawLevel(self.depth, self.shapes, self.Level, self.pixel_data, self.width, self.height, self.aproxLimit)
        def pressRight():
             if (self.drawFull):
                  if (self.depth < 20):
                    self.shapes.clear()
                    self.depth += 1
                    if(self.tree.getDepth() >= self.depth):
                         self.tree.drawFull(self.depth, self.shapes, self.Full)
                    else:
                         self.tree.addNivel()
                         self.tree.drawFull(self.depth, self.shapes, self.Full)
                         
                    
             elif(self.drawLevel):
                  if (self.aproxLimit < 100):
                    self.shapes.clear()
                    self.aproxLimit += 2
                    self.tree.drawLevel(self.depth, self.shapes, self.Level, self.pixel_data, self.width, self.height, self.aproxLimit)

        def pressLeft():
             
             if (self.drawFull):
                    self.shapes.clear()
                    self.depth -= 1
                    self.tree.drawFull(self.depth, self.shapes, self.Full)
             elif(self.drawLevel):
                  if (self.aproxLimit > 0):
                    self.shapes.clear()
                    self.aproxLimit -= 2
                    self.tree.drawLevel(self.depth, self.shapes, self.Level, self.pixel_data, self.width, self.height, self.aproxLimit)
                  
	
        def initTree():
               self.tree = binaryTree(self.width, self.height)
               self.tree.subdivide(self.depth)

        def on_key_press(key, modifiers):
             if (key == pyglet.window.key.G):
                  pressG()
             elif(key == pyglet.window.key.K):
                  pressK()
             elif(key == pyglet.window.key.X):
                  pressRight()
             elif(key == pyglet.window.key.Z):
                  pressLeft()     
        
        @window.event
        def on_draw():
            window.clear()
            if (self.drawFull): 
                self.Full.draw()
            if (self.drawLevel):
                self.Level.draw()
        
        initTree()
        window.push_handlers(on_draw)
        window.push_handlers(on_key_press)
        
        pyglet.app.run()
        
screen = Screen()