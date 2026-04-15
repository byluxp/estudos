def fatorial(n):
    f = 1
    for c in range(1,n+1):
        f*=c
    return f

num=int(input('Digite um número para calcular o fatorial: '))
fat=fatorial(num)
print(f'O fatorial de {num} é: {fat}')

