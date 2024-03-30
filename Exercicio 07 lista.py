lado1 = float(input("Informe o comprimento do primeiro lado do triângulo: "))
lado2 = float(input("Informe o comprimento do segundo lado do triângulo: "))
lado3 = float(input("Informe o comprimento do terceiro lado do triângulo: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    angulo1 = (lado2 ** 2 + lado3 ** 2 - lado1 ** 2) / (2 * lado2 * lado3)
    angulo2 = (lado1 ** 2 + lado3 ** 2 - lado2 ** 2) / (2 * lado1 * lado3)
    angulo3 = 1 - angulo1 - angulo2

    angulo1 = angulo1 * 180
    angulo2 = angulo2 * 180
    angulo3 = angulo3 * 180

    if lado1 == lado2 == lado3:
        tipo_lado = "equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo_lado = "isósceles"
    else:
        tipo_lado = "escaleno"

    if angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
        tipo_angulo = "obtuso"
    elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
        tipo_angulo = "retângulo"
    else:
        tipo_angulo = "agudo"

    print("O triângulo é", tipo_lado, "e", tipo_angulo + ".")
else:
    print("Não é possível formar um triângulo com esses lados.")
