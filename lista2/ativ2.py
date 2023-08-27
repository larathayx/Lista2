#código para calcular a velocidade media e indicar a maior entre dois carros
distancia1 = float(input("Digite a distancia em metros percorrida do carro 1: "))
tempo1 = int(input("Digite o tempo em minutos gasto do carro 1: "))
velocidadeM1 = distancia1/tempo1


distancia2 = float(input("Digite a distancia em metros percorrida do carro 2: "))
tempo2 = int(input("Digite o tempo gasto em minutos do carro 2: "))
velocidadeM2 = distancia2/tempo2 #calculo para velocidade média


if  velocidadeM1 == velocidadeM2:
    print("Os dois carros tiveram a mesma velocidade")
elif velocidadeM1 > velocidadeM2:
    print ("O carro 1 teve a maior velocidade média")
else:
    print ("O carro 2 teve a maior velocidade média")