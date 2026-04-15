import valores

p = float(input('Digite o valor em reais: R$ '))
print(f'Aumentando {valores.moeda(p)} em 10% temos {(valores.aumentar(p,10,True))}') # True para adicionar formatação
print(f'Diminuindo {valores.moeda(p)} em 10% temos {(valores.diminuir(p,10,True))}')
print(f'O dobro de {valores.moeda(p)} é {valores.dobro(p,True)}')
print(f'A metade de {valores.moeda(p)} é {valores.metade(p,True)}') # Não esquecer de salvar
