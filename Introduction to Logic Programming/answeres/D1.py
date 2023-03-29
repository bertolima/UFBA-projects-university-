#Entrada
temposeg = float(input())

#logica(conversão de unidades)
divnormal = temposeg / 3600
divinteira = temposeg // 3600
restohoras = divnormal - divinteira
horas = divnormal - restohoras
horas = int(horas)
minutosnormal = restohoras * 60
minutosinteiro = int(minutosnormal)
segundosnormal = minutosnormal - minutosinteiro
segundostotal = segundosnormal * 60
minutostotal = minutosnormal - segundosnormal

#Saída

print(horas, "h", sep="")
print(int(minutostotal), "m", sep="")
print(round(segundostotal), "s", sep="")

#Reprise do código

#Entrada
x = int(input())

#logica(converão de unidades)
horas = x // 3600
minutos = ((x / 3600) - horas) * 60
minutos = int(minutos)
segundos = (((x / 3600) - horas) * 60 - minutos) * 60
segundos = round(segundos)

#saida
print(horas, "h" , sep="")
print(minutos , "m", sep="")
print(segundos, "s", sep="")