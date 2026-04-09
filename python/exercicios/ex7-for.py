y = 0
for c in range(1,6):
    s = int(input('Digite um valor: '))
    if s % 2 == 0:
       s = 0 # transformar o valor em 0 para não ser somado
    else:
        y += s # y se torna y + s, ou seja, vai somando os valores ímpares digitados pelo usuário
    print (y) # imprime o valor de y a cada iteração
print('Soma: ', y) #imprime o valor total de y