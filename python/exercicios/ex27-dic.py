from datetime import date

funcionarios = {}
empresa = []

while True:
    funcionarios['nome'] = input("Digite o nome do funcionário: ")
    funcionarios['nascimento'] = input("Digite a data de nascimento (dd/mm/aaaa): ")
    funcionarios['carteira'] = input("Digite o número da carteira de trabalho (0 não tem): ")
    if funcionarios['carteira'] == '0':
        break
    else:
        funcionarios['salario'] = float(input("Digite o salário: "))
        funcionarios['contratacao'] = input("Digite o ano de contratação: ")
    aposentadoria = int(funcionarios['contratacao']) - int(funcionarios['nascimento'][-4:]) + 35
    empresa.append(funcionarios.copy())
    resposta = input("Deseja continuar? (s/n): ").upper(    )
    if resposta == 'N':
        break
print('==' * 30)
print(f'O nome do funcionário é: {funcionarios["nome"]}')
print(f'A idade do funcionário é: {date.today().year - int(funcionarios["nascimento"][-4:])} anos')
print(f'O número da carteira de trabalho é: {funcionarios["carteira"]}')
print(f'O salário do funcionário é: R${funcionarios["salario"]:.2f}')
print(f'O ano de contratação é: {funcionarios["contratacao"]}')
print(f'O funcionário se aposentará com {aposentadoria} anos')