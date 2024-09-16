# Dados dois números inteiros positivos, determinar o Máximo Divisor Comum (MDC)
# entre eles usando o Algoritmo de Euclides.

D1 = int(input(("Digite o primeiro número inteiro positivo: "))) 
D2 = int(input(("Digite o segundo número positivo: ")))
Num1 = D1
Num2 = D2
while D2 != 0:
    resto = D1 % D2
    D1 = D2
    D2 = resto
print( "O MDC de: ", Num1," | ", Num2)
print("É :", D1)
