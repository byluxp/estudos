num1 = int(input('Digite um número: ')) # pede para o usuário digitar um número
fatorial = 1 # inicia a variável fatorial com o valor 1
contador = num1 # inicia a variável contador com o valor do número digitado
while contador > 1: # enquanto o contador for maior que 1
    fatorial *= contador # fatorial se torna fatorial multiplicado por contador
    contador -= 1 # contador é decrementado em 1
    print('fatorial:[{}] contador: [{}]'.format(fatorial, contador)) # imprime o valor de fatorial e contador a cada iteração
print('O fatorial de {} é {}'.format(num1, fatorial)) # imprime o