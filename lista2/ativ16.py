# Ler um número inteiro de três dígitos
numero = int(input("Informe um número de 3 dígitos: "))

# Separar os dígitos
primeiro_digito = numero // 100
segundo_digito = (numero // 10) % 10
terceiro_digito = numero % 10

# Calcular a soma dos dígitos
soma_digitos = primeiro_digito + segundo_digito + terceiro_digito

print(f"Soma dos dígitos do número {numero} é igual a {soma_digitos}")

# Verificar se o número formado é divisor de 16 e múltiplo de 4
if 16 % soma_digitos == 0 and soma_digitos % 4 == 0:
    print("O número informado é divisor de 16 e múltiplo de 4 ao mesmo tempo.")
else:
    print("O número informado não atende às condições.")