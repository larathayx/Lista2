# codigo para calcular quantos dias tem um mes (independente do ano)
mes = input ("Digite o mes desejado: ")
ano = int(input("Digite o ano desejado: "))


if mes == "janeiro" or mes == "março" or mes == "maio" or mes == "julho" or mes == "agosto" or mes == "outubro" or mes == "dezembro":
    diasDoMes = 31
    print ("Este mês possui "+str(diasDoMes)+ " dias")
elif mes == "fevereiro" and ano % 4 == 0:
    diasDoMes = 28 #(para anos bissextos)
    print ("Este mês possui "+str(diasDoMes)+ " dias")
elif mes == "fevereiro":
    diasDoMes = 29
    print ("Este mês possui "+str(diasDoMes)+ " dias")
else :
    diasDoMes = 30
    print ("Este mês possui "+str(diasDoMes)+ " dias")