# codigo para calcular o valor da energia de acordo com o tipo de consumidor
consumidor = input("DIgite seu tipo de consumidor: ")
consumo = float(input("Digite a quantidade de energia consumida: "))


if consumidor == "I" or consumidor == "industrial":
    valorP = (0.68 * consumo) + 34 # dados pela tabela
    print("O valor a ser pago será de: "+str(valorP)+ " reais")
elif consumidor == "C" or consumidor == "comercial":
    valorP = (0.37 * consumo) + 45
    print("O valor a ser pago será de: "+str(valorP)+ " reais")
else:
    valorP = (0.77 * consumo) - 22
    print("O valor a ser pago será de: "+str(valorP)+ " reais")