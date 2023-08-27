# código para calcular  a média de notas
nome = input("Digite seu nome: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))


media = (nota1 + nota2)/2
print (nome+", "+str(media)) # saida : nome, média e "aprovado", "recuperação" ou "reprovado"
if media >= 0 and media < 5:
  print("Reprovado")
elif media >=5 and media < 7:
  print ("Recuperação")
elif media >=7 and media <=10:
  print("Aprovado")