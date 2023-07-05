import pyglet
from binaryTree import binaryTree

def lerImagem(arq):
        img = pyglet.image.load(arq)
        return img


class Screen:
    
    def __init__(self):
        self.imagem = lerImagem('./DEMs/Terreno0.5K.jpg')
        self.width = self.imagem.width
        self.height = self.imagem.height
        
        
        window = pyglet.window.Window(self.width, self.height)
        self.batch = pyglet.graphics.Batch()
        self.tree = binaryTree(self.width, self.height, self.batch, self.imagem)
        
	
        def initShapes():
               self.tree.subdivide()

               
        
        @window.event
        def on_draw():
            window.clear()
            self.batch.draw()



        window.push_handlers(on_draw)
        initShapes()
        
        pyglet.app.run()
        
	
    
    




screen = Screen()