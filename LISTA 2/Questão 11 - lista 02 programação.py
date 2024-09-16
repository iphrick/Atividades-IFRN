# Um robô pode se mover em oito sentidos em um plano cartesiano: U (cima); D (baixo);
# R (direita); L (esquerda); O (noroeste/cima-esquerda); N (nordeste/cima-direita); E (sudeste/baixo-direita)
# e W (sudoeste/baixo-esquerda).
# Faça um programa que:
# a) Solicite ao usuário a posição inicial do robô (suas coordenadas X e Y);
# b) Solicite ao usuário uma string. Letras maiúsculas e minúsculas são indistintas e aquelas
# informadas que estejam fora das estabelecidas (U, D, R, L, O, N, E e W) devem ser ignoradas.
# c) Com base em cada letra válida (U, D, R, L, O, N, E e W), o robô deverá se deslocar 1 (uma)
# unidade em cada eixo (X e Y) por vez em função da direção;
# Ao final, indique:
# a) a posição inicial do robô (coordenadas X e Y);
# b) a posição final do robô (coordenadas X e Y);
# c) quantos movimentos válidos ele executou;
# d) quais foram os movimentos válidos que ele executou;
# e) em que quadrante ele iniciou (posição inicial de X e Y) e;
# f) em que quadrante ele terminou (posição final de X e Y)
x_inicial = int(input("Digite a coordenada X inicial do robô: "))
y_inicial = int(input("Digite a coordenada Y inicial do robô: "))
x = x_inicial
y = y_inicial

movimentos = input("Digite a sequência de movimentos do robô (U, D, R, L, O, N, E, W): ").upper()

direcoes = {
    'U': (0, 1),
    'D': (0, -1),
    'R': (1, 0),
    'L': (-1, 0),
    'O': (-1, 1),
    'N': (1, 1),
    'E': (1, -1),
    'W': (-1, -1)
}

movimentos_validos = []
quantidade_movimentos_validos = 0

for movimento in movimentos:
    if movimento in direcoes:
        dx, dy = direcoes[movimento]
        x += dx
        y += dy
        movimentos_validos.append(movimento)
        quantidade_movimentos_validos += 1

if x_inicial > 0 and y_inicial > 0:
    quadrante_inicial = "1º Quadrante"
elif x_inicial < 0 and y_inicial > 0:
    quadrante_inicial = "2º Quadrante"
elif x_inicial < 0 and y_inicial < 0:
    quadrante_inicial = "3º Quadrante"
elif x_inicial > 0 and y_inicial < 0:
    quadrante_inicial = "4º Quadrante"
elif x_inicial == 0 and y_inicial != 0:
    quadrante_inicial = "Eixo Y"
elif y_inicial == 0 and x_inicial != 0:
    quadrante_inicial = "Eixo X"
else:
    quadrante_inicial = "Origem"

if x > 0 and y > 0:
    quadrante_final = "1º Quadrante"
elif x < 0 and y > 0:
    quadrante_final = "2º Quadrante"
elif x < 0 and y < 0:
    quadrante_final = "3º Quadrante"
elif x > 0 and y < 0:
    quadrante_final = "4º Quadrante"
elif x == 0 and y != 0:
    quadrante_final = "Eixo Y"
elif y == 0 and x != 0:
    quadrante_final = "Eixo X"
else:
    quadrante_final = "Origem"

print(f"Posição inicial do robô: ({x_inicial}, {y_inicial})")
print(f"Posição final do robô: ({x}, {y})")
print(f"Quantidade de movimentos válidos: {quantidade_movimentos_validos}")
print(f"Movimentos válidos executados: {', '.join(movimentos_validos)}")
print(f"Quadrante inicial: {quadrante_inicial}")
print(f"Quadrante final: {quadrante_final}")
