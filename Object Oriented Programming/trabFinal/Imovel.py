from Endereco import Endereco
from Agenda import Agenda

class Imovel:
    def __init__(self, nIptu:float, tipo:str, utilizacao:str, rua: str, numero: str, cep: str, estado: str = "BA", cidade:str = "Salvador"):
        self.__nIptu = nIptu
        self.__tipo = tipo.upper()
        self.__utilizacao = utilizacao.upper()
        self.__endereco = Endereco(rua, numero, cep, estado, cidade)
        self.__agenda = Agenda()

    def getIptu(self):
        return self.__nIptu
    
    def getTipo(self):
        return self.__tipo
    
    def getUtilizacao(self):
        return self.__utilizacao
    
    def setIptu(self, nIptu:float):
        self.__nIptu = nIptu
    
    def getEndereco(self):
        return self.__endereco
    
    def alugar(self, inicio:int, final:int, mes:str):
        self.__agenda.alugar(inicio, final, mes)
    
    def desalugar(self, inicio:int, final:int, mes:str):
        self.__agenda.desalugar(inicio, final, mes)
    
    def bloquear(self, inicio:int, final:int, mes:str):
        self.__agenda.bloquear(inicio, final, mes)

    def desbloqeuar(self, inicio:int, final:int, mes:str):
        self.__agenda.desbloquear(inicio, final, mes)
    
    def __str__(self):
        return f'Imóvel - {self.__endereco}, Valor IPTU: {self.__nIptu}, Tipo: {self.__tipo}, Utilização: {self.__utilizacao}'
    