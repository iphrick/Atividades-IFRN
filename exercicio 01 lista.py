#Questão 1

n = int(input("Digite um valor de até 4 digitos: "))
if n > 9999:
    print("O número possui mais que 4 digitos.")
else:
    d1 = n % 10
    n //= 10
    d2 = n % 10
    n //= 10
    d3 = n % 10
    n //= 10
    d4 = n % 10

    soma = d1 + d2 + d3 + d4
    resultado = soma
    print("O resultado da soma dos dígitos é:", resultado)