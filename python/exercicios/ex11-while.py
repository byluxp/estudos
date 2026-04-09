num = int (input('Digite o quanto você quer sacar: R$ ')) # pede para o usuário digitar o valor do saque

saque = cedulas50 = cedulas20 = cedulas10 = cedulas1 = 0 # inicia as variáveis de cada tipo de cédula com o valor 0

while saque < num:
    if num - saque >= 50: # se o valor do saque menos o valor já sacado for maior ou igual a 50
        saque += 50 # o valor do saque é incrementado em 50
        cedulas50 += 1 # o número de cédulas de 50 é incrementado em 1
    elif num - saque >= 20: # se o valor do saque menos o valor já sacado for maior ou igual a 20
        saque += 20 # o valor do saque é incrementado em 20
        cedulas20 += 1 # o número de cédulas de 20 é incrementado em 1
    elif num - saque >= 10: # se o valor do saque menos o valor já sacado for maior ou igual a 10
        saque += 10 # o valor do saque é incrementado em 10
        cedulas10 += 1 # o número de cédulas de 10 é incrementado em 1
    elif num - saque >= 1: # se o valor do saque menos o valor já sacado for maior ou igual a 1
        saque += 1 # o valor do saque é incrementado em 1
        cedulas1 += 1 # o número de cédulas de 1 é incrementado em 1

print(f'O valor do saque é R$ {num}. Você receberá {cedulas50} cédulas de R$ 50, {cedulas20} cédulas de R$ 20, {cedulas10} cédulas de R$ 10 e {cedulas1} cédulas de R$ 1.') # imprime o valor do saque e a quantidade de cada tipo de cédula que o usuário receberá