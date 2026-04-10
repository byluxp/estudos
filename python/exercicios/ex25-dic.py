boletim = {}
alunos = []

while True:
    boletim['nome'] = input("Digite o nome do aluno: ")
    boletim['nota1'] = float(input("Digite a primeira nota: "))
    boletim['nota2'] = float(input("Digite a segunda nota: "))
    boletim['media'] = (boletim['nota1'] + boletim['nota2']) / 2
    boletim['situacao'] = "Aprovado" if boletim['media'] >= 7 else "Reprovado" 
    alunos.append(boletim.copy()) # adiciona uma cópia do boletim atual à lista de alunos
    resposta = input("Deseja continuar? (s/n): ").upper()
    if resposta == 'S':
        continue
    if resposta == 'N':
        break
    else:
        print("Resposta inválida. Encerrando o programa.")
        break
for aluno in alunos:
    print(f'O nome é {aluno["nome"]} a média é {aluno["media"]} e a situação é {aluno["situacao"]}')