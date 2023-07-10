from Imovel import Imovel
from Proprietario import Proprietario

def cadatrarProprietario() -> Proprietario:
    print("---CADASTRO DE PROPRIETÁRIO---")
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")
    rg = input("Digite o RG: ")
    rua = input("Digite a rua de residência: ")
    numero = input("Digite o número da residência: ")
    cep = input("Digite o CEP da residência: ")
    estado = input("Digite o estado de residência(use sigla, Bahia = BA): ")
    cidade = input("Digite a cidade de residência: ")
    return Proprietario(nome, cpf, rg, rua, numero, cep, estado, cidade)

def cadatrarImovel() -> Imovel:
    print("---CADASTRO DE IMÓVEL---")
    iptu = float(input("Digite o valor do IPTU: "))
    tipo = input("Digite o tipo do imóvel(casa ou apto): ")
    utlizacao = input("Digite a utitlização do imóvel(campo, cidade ou praia): ")
    rua = input("Digite a rua do imóvel: ")
    numero = input("Digite o número do imóvel: ")
    cep = input("Digite o CEP do imóvel: ")
    estado = input("Digite o estado(use sigla, Bahia = BA): ")
    cidade = input("Digite a cidade: ")
    return Imovel(iptu, tipo, utlizacao, rua, numero, cep, estado, cidade)

def alugar(imoveis:list[Imovel]):
    print("---IMOVEIS DISPONIVEIS---")
    for imovel in imoveis:
        print(imovel)
    current = None
    cep = input("Digite o CEP do imóvel desejado: ")
    numero = input("Digite o número do imovel desejado: ")
    for imovel in imoveis:
        if(imovel.getEndereco().getCep() == cep and imovel.getEndereco().getNumero() == numero):
            current = imovel
            break
    if(current is None):
        print("Imóvel não encontrado")
    else:
        mes = input("Digite o mês da locação: ")
        inicio = int(input("Digite a data de início da locação: "))
        final = int(input("Digite a data final da locação: "))
        current.alugar(inicio, final, mes)

def desalugar(imoveis:list[Imovel]):
    print("---IMOVEIS---")
    for imovel in imoveis:
        print(imovel)
    current = None
    cep = input("Digite o CEP do imóvel que você quer desalugar: ")
    numero = input("Digite o número do imovel que você quer desalugar: ")
    for imovel in imoveis:
        if(imovel.getEndereco().getCep() == cep and imovel.getEndereco().getNumero() == numero):
            current = imovel
            break
    if(current is None):
        print("Imóvel não encontrado")
    else:
        mes = input("Digite o mês da locação: ")
        inicio = int(input("Digite a data de início da locação: "))
        final = int(input("Digite a data final da locação: "))
        current.desalugar(inicio, final, mes)


def action() -> int:
    print("Digite o dígito correspondente a ação")
    print("0 - Encerrar Simulação")
    print("1 - Cadastrar Proprietário")
    print("2 - Cadastrar Imóvel")
    print("3 - Ver Imóveis")
    print("4 - Alugar")
    print("5 - Desalugar")
    flag = int(input())
    return flag


if __name__ == '__main__':
    proprietarios: list[Proprietario]= []
    imoveis: list[Imovel]= []
    print("---SISTEMA DE LOCAÇÃO DE IMÓVEIS---")
    running = True
    while(running):
        flag = action()
        if(flag == 0):
            running = False
        elif(flag == 1):
            proprietario = cadatrarProprietario()
            ver = int(input("Deseja cadastrar um imóvel a esse proprietário?(1 - Sim, 2 - Não)"))
            if (ver == 1):
                imovel = cadatrarImovel()
                proprietario.cadastrarImovel(imovel)
                imoveis.append(imovel)
            proprietarios.append(proprietario)
        elif(flag == 2):
            imoveis.append(cadatrarImovel())
        elif(flag == 3):
            for imovel in imoveis:
                print(imovel)
        elif(flag == 4):
            alugar(imoveis)
        elif(flag == 5):
            desalugar(imoveis)

    print("---ENCERRANDO SIMULAÇÃO---")
    

