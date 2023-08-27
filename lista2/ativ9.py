# código para calcular o valor ideal de calorias diárias de acordo com suas informações
sexo = input("Digite seu sexo: ")
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em centimetros: "))
idade = int(input("Digite a sua idade: "))


if sexo == "masculino":
  homem = 66 + ( 13.7 * peso ) + ( 5 * altura )- (6.8 * idade)# cálculo
  print ("Seu valor ideal de calorias diarias é de: " +str(homem))
elif sexo == "feminino":
  mulher =  665 + (9.6 * peso) + (1.8 * altura )- (4.7 * idade)
  print ("Seu valor ideal de calorias diarias é de: "+str(mulher))
else:
  print ("Entrada de dados não é valida")