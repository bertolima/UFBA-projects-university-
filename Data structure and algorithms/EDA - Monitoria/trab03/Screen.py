import pyglet
from binaryTree import binaryTree
import time


class Screen:
    
    def __init__(self, img):

        self.img = img

        self.width = self.img.width
        self.height = self.img.height

        self.pixel_data = self.img.get_image_data().get_data('I', self.width)

        self.drawFull = False
        self.drawLevel = False
        self.drawImg = True

        self.tree = None

        self.shapes = []

        self.depth = 1
        self.aproxLimit = 5
        
        
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
                  self.tree.drawFullIter(self.depth, self.shapes, self.Full)

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
                  self.tree.drawLevelIter(self.depth, self.shapes, self.Level, self.pixel_data, self.width, self.height, self.aproxLimit)
        def pressQ():
             if self.drawImg:
                  self.drawImg = False
             else:
                  self.drawImg = True

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
               self.tree.subdivideIter(self.depth)

        def on_key_press(key, modifiers):
             if (key == pyglet.window.key.G):
                  pressG()
             elif(key == pyglet.window.key.K):
                  pressK()
             elif(key == pyglet.window.key.MOTION_RIGHT):
                  pressRight()
             elif(key == pyglet.window.key.MOTION_LEFT):
                  pressLeft()
             elif(key == pyglet.window.key.Q):
                  pressQ()     
        
        @window.event
        def on_draw():
            window.clear()
            if (self.drawFull): 
                self.Full.draw()
            if (self.drawLevel):
                self.Level.draw()
            if (self.drawImg):
                 self.img.blit(0,0,0)
        
        initTree()
        window.push_handlers(on_draw)
        window.push_handlers(on_key_press)
        
        pyglet.app.run()
        