#codigo para comparar 3 números e verificar o maior
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))


if num1 > num2 and num1 > num3 :
  print (str(num1)+ " é o maior numero")
elif num2 > num1 and num2 > num3:
  print (str(num2)+ " é o maior numero")
else:
  print (str(num3)+ " é o maior numero")