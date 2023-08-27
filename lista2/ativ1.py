#código que concede ou não o financiamento de algo de acordo com seu salário
salario = float(input("Digite o valor do seu salario:"))
financiamento = float(input("Digite o valor do financiamento desejado: "))


if financiamento <= salario * 5:
    print ("Financiamento Concedido ")
else:
    print ("Financiamento Negado ")
print ("Obrigado por nos consultar.")