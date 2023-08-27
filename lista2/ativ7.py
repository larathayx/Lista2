# código para informar se um triângulo é retângulo , acutângulo, ou obtusângulo
angulo1 = int(input("Digite um angulo do triangulo: "))
angulo2 = int(input("Digite o segundo angulo do triangulo: "))
angulo3 = int(input("Digite o terceiro angulo do triangulo: "))


if (angulo1 + angulo2 + angulo3) != 180: # se a soma dos 3 ângulos não for igual a 180 "mensagem de erro"
    print ("Os ângulos informados não formam um triângulo")
elif angulo1 <90 and angulo2 <90 and angulo3 <90:
    print ("È um triângulo Acutângulo")
elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
    print ("È um triângulo Retângulo")
else:
    print ("È um triângulo Obtusângulo")
