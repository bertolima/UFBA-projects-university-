class Agenda:
    def __init__(self):
        self.__datasBloqueadas: list[tuple(int, int, str)] = []
        self.__datasDisponiveis: list[tuple(int, int, str)] = []
        self.__datasAlugadas: list[tuple(int, int, str)] = []
    
    def bloquear(self, inicio:int, final:int, mes:str):
        intervalo = (inicio, final, mes.upper())
        self.__datasBloqueadas.append(intervalo)
    
    def desbloquear(self, inicio:int, final:int, mes:str):
        mes = mes.upper()
        for intervalo in self.__datasBloqueadas:
            if(intervalo[2] == mes):
                if (inicio <= intervalo[0] and final >= intervalo[1]):
                    self.__datasBloqueadas.remove(intervalo)

    def alugar(self, inicio:int, final:int, mes:str):
        if(self.isBloqueado(inicio, final, mes) or self.isAlugado(inicio, final, mes)):
            print("Imovel indisponível nas data fornecidas.")
        else:
            intervalo = (inicio, final, mes.upper())
            self.__datasAlugadas.append(intervalo)
    
    def desalugar(self, inicio:int, final:int, mes:str):
        mes = mes.upper()
        ver = False
        for intervalo in self.__datasAlugadas:
            if(intervalo[2] == mes):
                if (inicio == intervalo[0] and final == intervalo[1]):
                    self.__datasAlugadas.remove(intervalo)
                    print("Imóvel desalugado com sucesso!!!")
                    ver = True
                    break
        if ver == False:
            print("Datas não encontradas.")

    def isBloqueado(self, inicio:int, final:int, mes:str) -> bool:
        mes = mes.upper()
        for intervalo in self.__datasBloqueadas:
            if(intervalo[2] == mes):
                if ((inicio >= intervalo(0) and final <= intervalo(1))):
                    return True
        return False
    
    def isAlugado(self, inicio:int, final:int, mes:str) -> bool:
        mes = mes.upper()
        for intervalo in self.__datasAlugadas:
            if(intervalo[2] == mes):
                if ((inicio >= intervalo[0] and final <= intervalo[1])):
                    return True
        return False

    def mostrarDatasAlugadas(self):
        for intervalo in self.__datasAlugadas:
            print("Imovel alugado:", intervalo[2], intervalo[0], "-", intervalo[1], ".", end="")

