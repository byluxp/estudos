valor = 0
opçao = ''
escolhas = 0
while opçao != 'S':
    num = int(input('Digite um valor: '))
    opçao = input('Deseja sair? [S/N] ').upper()
    valor += num
    escolhas += 1
print('A soma dos valores é: {}. Você digitou {} números. E a média dos valores é {}'.format(valor, escolhas, valor/escolhas))