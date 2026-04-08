valorCasa = int (input("Digite o valor da casa: "))
salario = float (input("Digite o salário do comprador: "))
anos = int (input("Digite a quantidade de anos para pagar: "))

parcela = valorCasa / (anos * 12)

if parcela > (salario * 0.3):
    print ("Empréstimo negado. O valor da parcela será: R$", parcela, "que corresponde a ", parcela/salario*100, "% do salário.")
else:
    print ("Empréstimo aprovado. O valor da parcela será: R$", parcela, 'que corresponde a ', parcela/salario*100, "% do salário.")