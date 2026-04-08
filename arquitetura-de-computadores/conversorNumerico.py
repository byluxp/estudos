num = int (input('Digite o valor para converter:'))
opção = int (input('Digite a opção de conversão: \n 1 - Binário \n 2 - Octal \n 3 - Hexadecimal \n'))

if opção == 1:
    print ('O número {} convertido para Binário é: {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print ('O número {} convertido para Octal é: {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print ('O número {} convertido para Hexadecimal é: {}'.format(num, hex(num)[2:]))
else:    
    print ('Opção inválida. Por favor, escolha uma opção entre 1 e 3.')