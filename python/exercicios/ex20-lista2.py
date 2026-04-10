nome = []
peso = []
pesados = []
leves = []

while True:
    nome.append(input("Digite o nome: "))
    peso.append(float(input("Digite o peso: ")))
    resposta = input("Deseja continuar? (s/n): ").upper()
    if resposta == 'N':
        break
print(f'Foram cadastrados {len(nome)} pessoas.')

for p in peso:
    if p > 80:
        print(f'Os mais pesados são: {nome[peso.index(p)]} com {p} kg.')

for p in peso:
    if p < 50:
        print(f'Os mais leves são: {nome[peso.index(p)]} com {p} kg.')


