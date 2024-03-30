minutos = int(input("Minutos estacionado: "))

horas = minutos // 60
if minutos % 60 > 0:
    horas += 1

valorTotal = 0

if horas <= 2:
    valorTotal = horas * 8
elif horas <= 4:
    valorTotal = 16 + (horas - 2) * 5
elif horas <= 12:
    valorTotal = 26 + (horas - 4) * 3
else:
    valorTotal = 30

print(f"Valor total: R${valorTotal:.2f}")
    
    