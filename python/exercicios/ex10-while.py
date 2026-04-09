valor = 0
opçao = ''
escolhas = maior = menor = 0
while opçao != 'S':
    num = int(input('Digite um valor: '))
    opçao = input('Deseja sair? [S/N] ').upper()
    valor += num
    escolhas += 1
    if escolhas == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print('A soma dos valores é: {}. Você digitou {} números. E a média dos valores é {}'.format(valor, escolhas, valor/escolhas))
print ('O maior valor é {} e o menor valor é {}'.format(maior, menor))