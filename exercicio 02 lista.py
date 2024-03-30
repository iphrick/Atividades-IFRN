#Questão 2 
valor = float(input("Digite o valor do saque: "))

cedula100 = int(valor // 100)
valor %= 100

cedula50 = int(valor // 50)
valor %= 50

cedula20 = int(valor // 20)
valor %= 20

cedula10 = int(valor // 10)
valor %= 10

cedula5 = int(valor // 5)
valor %= 5

cedula2 = int(valor // 2)
valor %= 2

moeda1 = int(valor // 1)
valor %= 1

moeda050 = int(valor // 0.5)
valor = round(valor % 0.5, 2)

moeda025 = int(valor // 0.25)
valor = round(valor % 0.25, 2)

moeda010 = int(valor // 0.10)
valor = round(valor % 0.10, 2)

moeda005 = int(valor // 0.05)
valor = round(valor % 0.05, 2)

moeda001 = int(valor // 0.01)

print("Cédulas:")
print("R$100:", cedula100)
print("R$50:", cedula50)
print("R$20:", cedula20)
print("R$10:", cedula10)
print("R$5:", cedula5)
print("R$2:", cedula2)

print("\nMoedas:")
print("R$1:", moeda1)
print("R$0.50:", moeda050)
print("R$0.25:", moeda025)
print("R$0.10:", moeda010)
print("R$0.05:", moeda005)
print("R$0.01:", moeda001)