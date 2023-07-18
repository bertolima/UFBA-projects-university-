import pyglet
from Triangle import Triangle


class binaryTree:
	def __init__(self, width:float, height:float, lista):
		self.imgHeight = height
		self.imgWidth = width
		
		self.pixelList = lista

		self.left:Triangle = None
		self.right:Triangle = None

		self.depth:int = None

	#recursive methods
	def recursiveSubdivide(self, maxDepth):
		self.depth = maxDepth
		self.left = Triangle(0, self.imgHeight, self.imgWidth, 0, 0, 0, 0)
		self.right = Triangle(0, self.imgHeight, self.imgWidth, 0, self.imgWidth, self.imgHeight, 0)
		self.left.divide(maxDepth)
		self.right.divide(maxDepth)
	
	def recursiveDrawFull(self, maxDepth, shapes, batch):
		self.left.drawFull(maxDepth, shapes, batch)
		self.right.drawFull(maxDepth, shapes, batch)

	def recursiveDrawLevel(self, maxDepth, shapes, batch, lista, width, height, flag):
		self.left.drawLevel(maxDepth, shapes, batch, lista, width, height, flag)
		self.right.drawLevel(maxDepth, shapes, batch, lista, width, height, flag)
	
	def recursiveAddLevel(self):
		self.depth+=1
		self.left.addLevel()
		self.right.addLevel()
	
	#iterative methods
	def iterativeSubdivide(self, maxDepth):
		self.depth = maxDepth
		self.left = Triangle(0, self.imgHeight, self.imgWidth, 0, 0, 0, 0)
		self.right = Triangle(0, self.imgHeight, self.imgWidth, 0, self.imgWidth, self.imgHeight, 0)
		parent:list[Triangle] = []
		parent.append(self.left)
		parent.append(self.right)
		child:list[Triangle] = []
		for i in range(maxDepth):
			for node in parent:
				node.calcularIntensidadeMedia(self.pixelList, self.imgWidth)
				node.subdivide()
				child.append(node.getLeft())
				child.append(node.getRight())
			parent = child
			child:list[Triangle] = []

	def iterativeDrawFull(self, maxDepth, shapes:list, batch):
		parent:list[Triangle] = []
		parent.append(self.left)
		parent.append(self.right)
		shapes.append(pyglet.shapes.Line(0,self.imgWidth,self.imgWidth,0, color =(255, 255,255,255), batch=batch))
		child:list[Triangle] = []
		for i in range(maxDepth):
			for node in parent:
				shapes.append(node.createShape(batch))
				child.append(node.getLeft())
				child.append(node.getRight())
			parent = child
			child:list[Triangle] = []

	def iterativeDrawLevel(self, maxDepth, shapes, batch, lista, width, height, flag):
		parent:list[Triangle] = []
		parent.append(self.left)
		parent.append(self.right)
		child:list[Triangle] = []
		for i in range(maxDepth):
			for node in parent:
				if(node.getErro() > flag):
					shapes.append(node.createShape(batch))
					child.append(node.getLeft())
					child.append(node.getRight())
			parent = child
			child:list[Triangle] = []

	def iterativeAddLevel(self):
		self.depth+=1
		parent:list[Triangle] = []
		parent.append(self.left)
		parent.append(self.right)
		child:list[Triangle] = []
		for i in range(self.depth-1):
			for node in parent:
				child.append(node.getLeft())
				child.append(node.getRight())
			parent = child
			child:list[Triangle] = []
		for node in parent:
			node.subdivide()
			node.calcularIntensidadeMedia(self.pixelList, self.imgWidth)

	#important acessor
	def getDepth(self):
		return self.depth

        
            
            