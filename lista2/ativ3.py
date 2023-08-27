#código para comparar a idade de duas pessoas
nome1 = input ("Digite o nome da pessoa 1: ")
idade1 = int (input("Digite a idade da pessoa 1: "))
nome2 = input ("Digite o nome da pessoa 2: ")
idade2 = int (input("Digite a idade da pessoa 2: "))
anoAtual = int (input("Digite o ano atual com 4 digitos: "))


pessoa1 = idade1 - anoAtual
pessoa2 = idade2 - anoAtual


if pessoa1 < pessoa2: #comparação
    print (str(nome1)+ str(pessoa1)+" é a pessoa mais nova") #saída = pessoa mais nova e seu ano de nascimento
else:
    print (str(nome2)+ str( pessoa2)+ " é a pessoa mais nova")