#código para calcular imposto de renda de acordo com a tabela dada
salario = float(input("Digite o seu salario bruto: "))


if salario <= 1903.98:
  print("Seu salario é isento de imposto ")
elif salario <= 2826.65: # saida = salário bruto, imposto e o salário líquido
  imposto = (salario * 0.075) - 142.80
  salarioL = salario - imposto
  print ("Seu salario bruto é de: "+str(salario)+
         " ,Seu imposto é de: "+str(imposto)+
         " e Seu salario liquido é de: "+str(salarioL))
elif salario <= 3751.05:
  imposto = (salario * 0.15) - 548.82
  salarioL = salario - imposto
  print ("Seu salario bruto é de: "+str(salario)+
         " ,Seu imposto é de: "+str(imposto)+
         " e Seu salario liquido é de: "+str(salarioL))
elif salario <= 4664.68:
  imposto = (salario * 0.225) - 636.13
  salarioL = salario - imposto
  print ("Seu salario bruto é de: "+str(salario)+
         " ,Seu imposto é de: "+str(imposto)+
         " e Seu salario liquido é de: "+str(salarioL))
else:
  imposto = (salario * 0.275) - 869.36
  salarioL = salario - imposto
  print ("Seu salario bruto é de: "+str(salario)+
         " ,Seu imposto é de: "+str(imposto)+
         " e Seu salario liquido é de: "+str(salarioL))