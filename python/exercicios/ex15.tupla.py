itens = ('Açucar', 3.50, 'Farinha', 2.00, 'Chá', 1.50)

c = preco = 0

for c in range(0,len(itens),2): # para c no intervalo de 0 até o tamanho de itens, conte de 2 em 2
    nome = itens[c]
    preco = itens[c+1]     
    print(f'Alimento: {nome} | preço: R${preco:.2f}')
print('fim')