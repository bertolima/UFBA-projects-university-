class Endereco:
    def __init__(self, rua: str, numero: str, cep: str, estado: str, cidade:str):
        self.__rua = rua
        self.__numero = numero
        self.__cep = cep
        self.__estado = estado
        self.__cidade = cidade
    
    def __str__(self):
        return f'Rua: {self.__rua}, Número: {self.__numero}, CEP: {self.__cep}, Estado: {self.__estado}, Cidade: {self.__cidade}'
    

    def atualizerEndereco(self, *args):
        if (len(args) == 5):
            self.__rua = args[0]
            self.__numero = args[1]
            self.__cep = args[2]
            self.__estado = args[3]
            self.__cidade = args[4]
        elif (len(args) == 3):
            self.__rua = args[0]
            self.__numero = args[1]
            self.__cep = args[2]

    def getRua(self):
        return self.__rua
    
    def getNumero(self):
        return self.__numero
    
    def getCep(self):
        return self.__cep
    
    def getEstado(self):
        return self.__cep
    
    def getCidade(self):
        return self.__cidade
