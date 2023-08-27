# codigo para calcular cada tipo de haste comprada e informar o valor total (com o desconto se houver)
tipos = int(input("Digite quantos tipos de hastes foram compradas: "))


if tipos == 3: # somente há desconto se for comprado maia de 3 tipos de hastes
  hasteAco = int(input("Digite quantas hastes de aço foram compradas: "))
  hasteCobre = int(input("Digite quantas hastes de cobre foram compradas: "))
  hasteAlu = int(input("Digite quantas hastes de aluminio foram compradas: "))
  quantidade = hasteAco + hasteAlu + hasteCobre
  valorBruto = (hasteAco * 2.5) + (hasteCobre * 4) + (hasteAlu * 5)


  if quantidade < 6: #dados como na tabela dada
    print("Não há desconto para esta quantidade de hastes")
    print("O valor total é de: "+str(valorBruto)+ " reais")
  elif quantidade > 15:
    desconto = valorBruto * 0.10
    print ("O valor total é de: "+str(desconto)+ " reais")
  elif quantidade < 20:
    desconto = valorBruto * 0.15
    print ("O valor total é de: "+str(desconto)+ " reais")
  else:
    desconto = valorBruto * 0.2
    print ("O valor total é de: "+str(desconto)+ " reais")
else:
  print ("Desculpa, somente acima de 3 tipos de hastes que tem desconto")