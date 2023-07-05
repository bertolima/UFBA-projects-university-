from pyglet import *
from Triangle import Triangle

class binaryTree:
    def __init__(self, width, height, batch, img):
        self.batch = batch
        self.img = img
        self.left = Triangle(0, height, width, 0, 0, 0, self.batch, 0)
        self.left.calcularIntensidadeMedia(img)
        self.right = Triangle(0, height, width, 0, width, height,self.batch, 0)
        self.right.calcularIntensidadeMedia(img)
	
	

    def subdivide(self):
        self.left.divide(self.batch, self.img)
        self.right.divide(self.batch, self.img)

            
def calculaElevacoes(MDT):

	# Para ter acesso aos pixels/amostras do objeto imagem do Pyglet
	# é necessário recuperar os dados, em formato de um vetor de intensidade.
	# No caso de terrenos existe apenas um canal de "cor" na imagem, referente a intensidade do pixel
	# O valor de "pitch" é definido para que possamos utilizar um endereçamento matricial (linhaxcoluna) para
	# acessar os elementos do vetor. 

	format = 'I'
	pitch = MDT.width * len(format)
	amostras = MDT.get_image_data().get_data(format, pitch)

	# Aqui contaremos quantos pixels possuem cada valor de elevação
	# Lembrando que imagens em tons de cinza (um canal de cor) representam suas intensidades em 1 Byte,
	# ou seja, permite 256 intensidades com valores no intervalo [0..255]

	contElev = [0] * 256

	eMax = 0
	eMin = 256
	eMedia = 0

	for i in range(MDT.width):		
		for j in range(MDT.height):

			# cada linha salta "pitch" elementos (colunas) para passar para a proxima linha 
			elevacao = amostras[i * pitch + j]

			# verifica os valores de intensidade máxima e mínima

			if elevacao > eMax: eMax = elevacao
			elif elevacao < eMin: eMin = elevacao

			# incrementa o contador de elevações do valor encontrado no pixel/amostra

			contElev[elevacao] += 1 	

	# Calcula o somatório das intensidades e divide pelo total de amostras/pixels para gerar a
	# intensidade/elevação média

	eMedia = 0
	for k in range(256):
		eMedia += contElev[k] * k

	eMedia /= MDT.width * MDT.height

	# retorno os valores calculados

	return eMin, eMax, eMedia
            
            