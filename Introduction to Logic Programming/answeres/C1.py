#Entrada
q1, q2, q3 = input().split()
e1, e2, e3 = input().split()
q1 = int(q1)
q2 = int(q2)
q3 = int(q3)
e1 = int(e1)
e2 = int(e2)
e3 = int(e3)
#logica
poison1 = q1 - (3 * e1)
poison2 = q2 - (3 * e2)
poison3 = q3 - (3 * e3)
total = poison1 + poison2 + poison3
#saida
print(total)