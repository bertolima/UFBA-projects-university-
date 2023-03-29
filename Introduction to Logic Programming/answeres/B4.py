# Entrada
x = int(input())
numeros = list(map(int, input().split()))

#criando uma lista para os numeros pares da lista numeros e outra lista para os numeros impares da lista nnumeros
par = [n for n in numeros if n % 2 == 0]
impar = [ n for n in numeros if n % 2 != 0]

#transformando a lista par em uma string
par_str = str(par)

#imprimindo valores
print(*par, sep=" ")
print(*impar, sep=" ")