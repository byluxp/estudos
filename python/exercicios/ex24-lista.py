alunos = []
notas = [[],[]]

while True:
    alunos.append(input("Digite o nome do aluno: "))
    notas[0].append(float(input("Digite a primeira nota: ")))
    notas[1].append(float(input("Digite a segunda nota: ")))
    resposta = input("Deseja continuar? (s/n): ").upper()
    if resposta == 'N':
        break

for i in range(len(alunos)):
    media = (notas[0][i] + notas[1][i]) / 2
    print(f'{alunos[i]} - Média: {media:.2f}')
    if media >= 7:
        print("Situação: Aprovado")
    elif media >= 5:
        print("Situação: Recuperação")