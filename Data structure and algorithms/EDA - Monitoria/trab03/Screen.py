import pyglet
from binaryTree import binaryTree

class Screen(pyglet.window.Window):

     def __init__(self, img):

          self.img = img
          self.pixel_data = self.img.get_image_data().get_data('I', img.width)

          self.drawFull = False
          self.drawLevel = False
          self.drawImg = True
          self.iterativeMode = True

          self.tree:binaryTree = None
          self.shapes:list[pyglet.shapes.Line] = []

          self.depth = 0
          self.aproxLimit = 5
          super().__init__(img.width, img.height)
          self.Full = pyglet.graphics.Batch()
          self.Level = pyglet.graphics.Batch()
          self.initTree()

     def pressM(self):
          if(self.iterativeMode):
               self.iterativeMode = False
               print("MODO RECURSIVO")
          else:
               self.iterativeMode = True
               print("MODO ITERATIVO")

     def pressUp(self):
          if(self.iterativeMode):
               if (self.drawFull):
                    if (self.depth < 20):
                         self.shapes.clear()
                         self.depth += 1
                         if(self.tree.getDepth() >= self.depth):
                              self.tree.iterativeDrawFull(self.depth, self.shapes, self.Full)
                         else:
                              self.tree.iterativeAddLevel()
                              self.tree.iterativeDrawFull(self.depth, self.shapes, self.Full)
               elif(self.drawLevel):
                    if (self.aproxLimit < 100):
                         self.shapes.clear()
                         self.aproxLimit += 2
                         self.tree.iterativeDrawLevel(self.depth, self.shapes, self.Level, self.pixel_data, self.width, self.height, self.aproxLimit)
          else:
               if (self.drawFull):
                    if (self.depth < 20):
                         self.shapes.clear()
                         self.depth += 1
                         if(self.tree.getDepth() >= self.depth):
                              self.tree.recusirveDrawFull(self.depth, self.shapes, self.Full)
                         else:
                              self.tree.recursiveAddLevel()
                              self.tree.recursiveDrawFull(self.depth, self.shapes, self.Full)
               elif(self.drawLevel):
                    if (self.aproxLimit < 100):
                         self.shapes.clear()
                         self.aproxLimit += 2
                         self.tree.iterativeDrawLevel(self.depth, self.shapes, self.Level, self.pixel_data, self.width, self.height, self.aproxLimit)


     def pressDown(self):
          if(self.iterativeMode):
               if (self.drawFull):
                    self.shapes.clear()
                    self.depth -= 1
                    self.tree.iterativeDrawFull(self.depth, self.shapes, self.Full)
               elif(self.drawLevel):
                    if (self.aproxLimit > 0):
                         self.shapes.clear()
                         self.aproxLimit -= 2
                         self.tree.iterativeDrawLevel(self.depth, self.shapes, self.Level, self.pixel_data, self.width, self.height, self.aproxLimit)
          else:
               if (self.drawFull):
                    self.shapes.clear()
                    self.depth -= 1
                    self.tree.recursiveDrawFull(self.depth, self.shapes, self.Full)
               elif(self.drawLevel):
                    if (self.aproxLimit > 0):
                         self.shapes.clear()
                         self.aproxLimit -= 2
                         self.tree.recusirveDrawLevel(self.depth, self.shapes, self.Level, self.pixel_data, self.width, self.height, self.aproxLimit)

     def pressRight(self):
          if(self.iterativeMode):
               if(self.drawImg):
                    self.drawImg = False
                    self.drawFull = True
                    self.tree.iterativeDrawFull(self.depth, self.shapes, self.Full)
               elif(self.drawFull):
                    self.drawFull = False
                    self.drawLevel = True
                    self.tree.iterativeDrawLevel(self.depth, self.shapes, self.Level, self.pixel_data, self.width, self.height, self.aproxLimit)
               elif(self.drawLevel):
                    self.drawLevel = False
                    self.drawImg = True
          else:
               if(self.drawImg):
                    self.drawImg = False
                    self.drawFull = True
                    self.tree.recursiveDrawFull(self.depth, self.shapes, self.Full)
               elif(self.drawFull):
                    self.drawFull = False
                    self.drawLevel = True
                    self.tree.recursiveDrawLevel(self.depth, self.shapes, self.Level, self.pixel_data, self.width, self.height, self.aproxLimit)
               elif(self.drawLevel):
                    self.drawLevel = False
                    self.drawImg = True
          
     def pressLeft(self):
          if (self.iterativeMode):

               if(self.drawImg):
                    self.drawImg = False
                    self.drawLevel = True
                    self.tree.iterativeDrawLevel(self.depth, self.shapes, self.Level, self.pixel_data, self.width, self.height, self.aproxLimit)
               elif(self.drawLevel):
                    self.drawLevel = False
                    self.drawFull = True
                    self.tree.iterativeDrawFull(self.depth, self.shapes, self.Full)
               elif(self.drawFull):
                    self.drawFull = False
                    self.drawImg = True
          else:
               if(self.drawImg):
                    self.drawImg = False
                    self.drawLevel = True
                    self.tree.recursiveDrawLevelDrawLevel(self.depth, self.shapes, self.Level, self.pixel_data, self.width, self.height, self.aproxLimit)
               elif(self.drawLevel):
                    self.drawLevel = False
                    self.drawFull = True
                    self.tree.recursiveDrawFullDrawFull(self.depth, self.shapes, self.Full)
               elif(self.drawFull):
                    self.drawFull = False
                    self.drawImg = True
          

     def on_key_press(self, key, modifiers):
          if (key == pyglet.window.key.MOTION_UP):
               self.pressUp()
          elif(key == pyglet.window.key.MOTION_DOWN):
               self.pressDown()
          elif(key == pyglet.window.key.MOTION_RIGHT):
               self.pressRight()
          elif(key == pyglet.window.key.MOTION_LEFT):
               self.pressLeft()
          elif(key == pyglet.window.key.M):
               self.pressM()
          elif(key == pyglet.window.key.ESCAPE):
               self.close()  

     def on_draw(self):
          self.clear()
          if (self.drawFull): 
               self.Full.draw()
          if (self.drawLevel):
               self.Level.draw()
          if (self.drawImg):
               self.img.blit(0,0,0)

     def initTree(self):
          self.tree = binaryTree(self.width, self.height, self.pixel_data)
          self.tree.iterativeSubdivide(self.depth)



          
          
          