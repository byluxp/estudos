# esse programa lê o numero digitado e o escreve por extenso
# 
num = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

posicao = int(input('Digite o número que você quer mostrar de 1 a 20:'))

while posicao > 20:
    print('Escolha um número válido!')
    posicao = int(input('Digite o número que você quer mostrar de 1 a 20:'))
print(f'Você digitou o numero: {num[posicao-1]}')