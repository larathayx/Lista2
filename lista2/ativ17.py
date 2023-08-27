#codigo para calcular o valor de y de acordo com a formula dada
z = float(input("Digite o valor de z para o calculo: "))
w = float(input("Digite o valor de w para o calculo: "))
#formula
if w > 0 or z < 7:
    x = (5 * w + 1) / 3
    t = 5 * z + 2
else:
    x = 5 * z + 2
    t = (5 * w + 1) / 3
y = (7 * x*3 - 3 * x*0.5 - 8 * t) / (5 * (x + 1))

print("O valor de y é: "+str(y))