from classe_LSE import cLSE
from classe_Pilha import cPilha
from classe_Fila import cFila
import random
class CCarta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe
        if valor=='Ás':
        	self.valornum=1
        elif valor=='Valete':
        	self.valornum=11
        elif valor=='Dama':
        	self.valornum=12
        elif valor=='Rei':
        	self.valornum=13
        else:
         	self.valornum=valor
    def Par(C1, C2):
        if isinstance(C1, CCarta) and isinstance(C2, CCarta):
            if C1.valor == C2.valor:
                return True
        else:
            return False

    def __str__(self):
        naipes = {
            'Copas': '\u2665',
            'Ouros': '\u2666',
            'Espadas': '\u2660',
            'Paus': '\u2663'
        }
        return f"{self.valor}{naipes.get(self.naipe, '')}"
class cBaralho:
    def __init__(self):
        naipes = ['Paus', 'Copas', 'Espadas', 'Ouros']
        valores = ['Ás', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei']
        self.cartas = cLSE()
        for naipe in naipes:
            for valor in valores:
                self.cartas.insereNo(CCarta(valor, naipe))

    def GerarACE(self):
        Baralho = self.cartas
        ACE = cPilha(cLSE.getTamanho(self.cartas))
        while Baralho.getTamanho() > 0:
            carta=cLSE.RemoveNoAleatorio(Baralho)
            ACE.push(carta)

        return ACE
class jogador:
	def __init__(self,Nome):
		self.nome=Nome
		self.mao=[0]*13
		self.monte=cPilha(52)
	def getCartas(self):
		Cartas=[]
		for i in self.mao:
			if isinstance(i, cFila):
				atual=i._inicio
				while atual!=None:
					Cartas.append(str(atual.__dado__))
					atual=atual.__prox__
		return Cartas
	def __str__(self):
		Cartas=self.getCartas()
		return self.nome+" - "+str(len(Cartas))+" Cartas - "+'(' + ','.join(Cartas) + ')'
 
class JogoMico:
	def __init__(self,jogadores):
		self.jogadores=[jogador(Nome) for Nome in jogadores]
		self.numjogadores=len(self.jogadores)
		Baralho=cBaralho()
		self.mico=cLSE.RemoveNoAleatorio(Baralho.cartas)
		self.ACE=Baralho.GerarACE()
	def DistribuirCartas(self,log=False):
		Saida=""
		Iteração=0
		indiceJogador=-1
		while self.ACE.topo>0:
			if indiceJogador==self.numjogadores-1:
				indiceJogador=0

			else:
				indiceJogador+=1
			Carta=self.ACE.pop().__dado__
			indicecarta=int(Carta.valornum)-1
			if isinstance(self.jogadores[indiceJogador].mao[indicecarta], cFila):
				self.jogadores[indiceJogador].mao[indicecarta].queue(Carta)
			else:
				self.jogadores[indiceJogador].mao[indicecarta]=cFila()
				self.jogadores[indiceJogador].mao[indicecarta].queue(Carta)
			if log==True:
				Iteração+=1
				if Iteração%self.numjogadores==0:
					Saida+=str(Iteração)+"°-Carta:"+ str(Carta) + "-Jogador:"+ self.jogadores[indiceJogador].nome+"\n"
				else:
					Saida+=str(Iteração)+"°-Carta:"+ str(Carta) + "-Jogador:"+ self.jogadores[indiceJogador].nome+"->  "
		if log==True:
			print("\n\nDistribuição das Cartas entre os jogadores:\n")
			print(Saida[:-4],"\n")
	def Guardar_Pares(self):
		for jogador in self.jogadores:
			mao = jogador.mao
			Pares=""
			for fila in mao:
				if isinstance(fila, cFila):
					if fila._numElems > 1:
						true,carta1 = fila.dequeue()
						true,carta2 = fila.dequeue()
						Pares+=f"{str(carta1)} e {str(carta2)},"
						jogador.monte.push(carta1)
						jogador.monte.push(carta2)
			if len(Pares)>0:
				print(f"{jogador.nome} formou os pares: ({Pares[:-1]})")			

	def Trocar_Cartas(self):
		num_jogadores = len(self.jogadores)

		for i in range(num_jogadores):
			jogador_atual = self.jogadores[i]
			jogador_direita = self.jogadores[(i + 1) % num_jogadores]

			
			while True:
				if len(jogador_direita.getCartas())==0:
					if i==0:
						jogador_direita = self.jogadores[num_jogadores-1]
					else:	
						jogador_direita = self.jogadores[(i + -1) % num_jogadores]
				j = random.randint(0, 12)
				if isinstance(jogador_direita.mao[j], cFila) and jogador_direita.mao[j].size() > 0:
					true,carta = jogador_direita.mao[j].dequeue()
					if isinstance(jogador_atual.mao[j], cFila):
						jogador_atual.mao[j].queue(carta)
					else:
						jogador_atual.mao[j]=cFila()
						jogador_atual.mao[j].queue(carta)
					print(f"{jogador_atual.nome} pegou a {str(carta)} da mão de {jogador_direita.nome}")
					break

	def verificar_fim_jogo(self):
		num_jogadores = len(self.jogadores)
		jogadores_mico = []
		Jogadores_Vencedores=[]
		for jogador in self.jogadores:
			if len(jogador.getCartas()) == 0:
				Jogadores_Vencedores.append(jogador)
			if len(jogador.getCartas()) == 1:
				jogadores_mico.append(jogador)
		if len(jogadores_mico) ==1 and num_jogadores==len(jogadores_mico)+len(Jogadores_Vencedores):
			return jogadores_mico[0].nome
		else:
			return False

	def Rodada(self):
		print("\nTrocando as Cartas entre os Jogadores:")
		self.Trocar_Cartas()
		print("\nGuardando cartas nos montes:")
		self.Guardar_Pares()
		print("\nStatus dos Jogadores:")
		for jogador in jogo.jogadores:
			print(jogador)
		Fim=self.verificar_fim_jogo()
		NRodada=0
		while Fim==False:
			NRodada+=1
			print("\n\n\nRodada N°",NRodada)
			Fim=self.verificar_fim_jogo()
			print("\nTrocando as Cartas entre os Jogadores:")
			self.Trocar_Cartas()
			print("\nGuardando cartas nos montes:")
			self.Guardar_Pares()
			print("\nStatus dos Jogadores:")
			for jogador in jogo.jogadores:
				print(jogador)
		print(f"{Fim} perdeu!!")
	def Jogar(self):
		print("\ninicio do jogo:")
		print("ACE:",self.ACE)
		print("\nCarta Mico:",self.mico)
		jogo.DistribuirCartas()
		print("\nStatus dos Jogadores:")
		for jogador in self.jogadores:
			print(jogador)
		print("\nGuardando cartas nos montes:")
		self.Guardar_Pares()
		self.Rodada()



			



jogo=JogoMico(["a","b","c"])
jogo.Jogar()

