# codigo para calcular o tempo de jogo
horaI = int(input("Digite a hora inicial do jogo: "))
minutosI = int(input("Digite o minuto inicial do jogo: "))
horaF = int(input("Digite a hora final do jogo: "))
minutosF = int(input("Digite o minuto final do jogo: "))
#com base na hora final e inicial


if horaI > 24 or minutosI > 59 or horaF > 24 or minutosF > 59:
    print ("Entrada de dados não é valida")
else:
    conversãoI = (horaI * 60) + minutosI
    conversãoF = (horaF * 60) + minutosF#conversão de horas p/ minutos
    tempoMin = conversãoF - conversãoI
    duracaoHoras = tempoMin // 60
    duracaoMin = tempoMin % 60




    print ("A duração do jogo foi de: " +str(duracaoHoras)+ " hora e " +str(duracaoMin)+ " minutos")