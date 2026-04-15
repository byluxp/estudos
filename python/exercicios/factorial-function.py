def fatorial(n):
    fat = 1   
    for c in range(n, 0, -1):
        if n == 0 or n == 1:
            return 1
        else:
            fat *= c
            print(f"{c} x ", end="")
            if c > 1:
                print(" ", end="")
    print(f"= {fat} ", end="")
    return fat
    
num = int(input("Digite um número para calcular o fatorial: "))
resultado = fatorial(num)
print(f"O fatorial de {num} é: {resultado}")