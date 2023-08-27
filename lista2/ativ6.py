# código para calcular  a média de notas  e faltas de um aluno
media = int(input("Digite sua media: "))
faltas = int(input("Digite o numero de faltas: "))
# faltas acima de 32 reprova / média abaixo de 7 reprova
if media >=7 and faltas <=32:
    print("Aprovado")
elif media < 7 and faltas <= 32:
    print ("Reprovado por média")
elif media >=7 and faltas >32:
    print ("Reprovado por faltas")
else:
    print ("Reprovado por faltas e média")