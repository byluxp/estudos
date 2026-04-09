import random 

numeros = ()
for c in range (1,5):
    valor = (random.randint(1,10))
    numeros = numeros + (valor,) #com o "valor," a virgula no final diz pro python que é uma tupla e não apenas um numero inteiro

print(numeros)