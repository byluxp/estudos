x = int (input("Digite um número inteiro: "))
y = int (input("Digite outro número inteiro: "))

x = x % y  # o % significa: o resto da divisão de x por y
print ("x", x)
x = x % y
print ("x", x)
y = y % x

print("O valor de y é:", y)