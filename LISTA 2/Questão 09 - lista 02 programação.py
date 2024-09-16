# digito dele elevado a potência n (onde n é a quantidade de dígitos) é igual ao número informado (veja a
# definição detalhada em https://en.wikipedia.org/wiki/Narcissistic_number).
# Faça um programa que solicite ao usuário um número inteiro positivo e informe se ele é (ou não) um
# número de Armstrong, de acordo com a definição. NÃO usar a função LEN().

numero = int(input("Digite um número inteiro positivo: "))

temp_num = numero
contador_digitos = 0
while temp_num > 0:
    contador_digitos += 1
    temp_num //= 10

temp_num = numero
soma = 0
while temp_num > 0:
    digito = temp_num % 10
    soma += digito ** contador_digitos
    temp_num //= 10

if soma == numero:
    print(f"{numero} é um número de Armstrong.")
else:
    print(f"{numero} não é um número de Armstrong.")

numero = int(input("Digite um número inteiro positivo: "))

temp_num = numero
contador_digitos = 0
while temp_num > 0:
    contador_digitos += 1
    temp_num //= 10

temp_num = numero
soma = 0
while temp_num > 0:
    digito = temp_num % 10
    soma += digito ** contador_digitos
    temp_num //= 10

if soma == numero:
    print(f"{numero} é um número de Armstrong.")
else:
    print(f"{numero} não é um número de Armstrong.")
