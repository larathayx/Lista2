# codigo parainformar se a pessoa é ou nao maior de idade dependendo do sexo
sexo = input("Digite seu sexo: ")
idade = int (input("Digite sua idade: "))


if sexo == "masculino":
  if idade > 21:
    print("Voçe é maior de idade")
  else:
    print("Voçe é menor de idade")
elif sexo == "feminino":
  if idade > 18:
    print("Voçe é maior de idade")
  else:
    print("Voçe é menor de idade")
else: 
  print ("Entrada de dados não é valida")