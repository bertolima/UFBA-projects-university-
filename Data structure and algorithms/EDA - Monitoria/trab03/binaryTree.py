from pyglet import *
from Triangle import Triangle

class binaryTree:
	def __init__(self, width, height):
		self.height = height
		self.width = width
		self.left = None
		self.right = None
		self.depth = None

	def subdivide(self, maxDepth):
		self.depth = maxDepth
		self.left = Triangle(0, self.height, self.width, 0, 0, 0, 0)
		self.right = Triangle(0, self.height, self.width, 0, self.width, self.height, 0)
		self.left.divide(maxDepth)
		self.right.divide(maxDepth)

	def drawFull(self, maxDepth, shapes, batch):
		self.left.drawFull(maxDepth, shapes, batch)
		self.right.drawFull(maxDepth, shapes, batch)

	def drawLevel(self, maxDepth, shapes, batch, lista, width, height, flag):
		self.left.drawLevel(maxDepth, shapes, batch, lista, width, height, flag)
		self.right.drawLevel(maxDepth, shapes, batch, lista, width, height, flag)
	
	def addNivel(self):
		self.depth+=1
		self.left.addLevel()
		self.right.addLevel()
		
	def getDepth(self):
		return self.depth

        
            
            