#código para calcular o consumo médio de um carro
distancia = float (input("Digite a distancia em km: "))
gasolina = int (input("Digite a quantidade de gasolina consumida em litros: "))


consumo = distancia / gasolina
if consumo < 8: #informar se é econômico ou nao
    print ("Venda o Carro!!")
elif consumo <=12 :
    print ("Econômico!!")
else:
    print ("Super econômico!!")