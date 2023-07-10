from Endereco import Endereco
from Imovel import Imovel

class Proprietario:
    def __init__(self, nome : str, cpf : str, rg: str, rua: str, numero: str, cep: str, estado: str = "BA", cidade:str = "Salvador"):
        self.__nome = nome
        self.__cpf = cpf
        self.__rg = rg
        self.__endereco = Endereco(rua, numero, cep, estado, cidade)
        self.__imoveis: list[Imovel] = []

    def getNome(self) -> str:
        return self.__nome
    
    def getCpf(self) -> str:
        return self.__cpf
    
    def getRg(self) -> str:
        return self.__rg
    
    def getEndereco(self)-> Endereco:
        return self.__endereco
    
    def cadastrarImovel(self, imovel:Imovel):
        self.__imoveis.append(imovel)
    
    def atualizarEndereco(self, *args):
        if (len(args) == 5):
            self.__endereco.atualizerEndereco(args[0], args[1], args[2], args[3], args[4])
        elif (len(args) == 3):
            self.__endereco.atualizerEndereco(args[0], args[1], args[2])
    
    def verImoveis(self, tipo:str):
        for imovel in self.__imoveis:
            if (imovel.getTipo() == tipo.upper()):
                print(imovel)
    def __str__(self):
        return f'Nome: {self.__nome}, CPF: {self.__cpf}, RG: {self.__rg}, Endereço: {self.__endereco}'
    
