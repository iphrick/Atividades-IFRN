#Dado que uma Progressão Geométrica (P.G.) é a uma sequência numérica cujo
#quociente (q) ou razão entre um número e outro (exceto o primeiro) é sempre igual. Vale lembrar que
#essa razão é sempre constante e pode ser qualquer número racional (positivos, negativos, frações) exceto
#o número zero (0).

# a) Solicite ao usuário um valor inteiro inicial e a razão da P.G.;
# b) Solicite um novo valor inteiro positivo correspondente a quantidade de elementos da PG e exiba
# os valores dessa P.G.;
# c) Informe se a P.G. é constante, oscilante, crescente ou decrescente
# d) Calcule a soma dos elementos dessa P.G.;
# e) Solicite um outro valor inteiro n correspondente a enésima posição de um elemento da P.G. e
# exibir o valor desse elemento. 

import sys
valor_inicial = int(input('informe um valor inteiro inicial: '))
razão = int(input('informe a razão da P.G: '))
qt_elementos = int(input('informe um navo valor inteiro positivo correspondente a quantiade de elementos da P.G: '))

pg = []
for i in range(qt_elementos):
 elementos_pg = valor_inicial  * (razão**i)
 pg.append(elementos_pg)

 print("Os valores dessa P.G são: ")
 for valor in pg:
     print(valor , end = ' ')
 print()

if qt_elementos < 0:
    print('informe um valor inteiro positivo')
    sys.exit
elif razão  == 1:
    print('A PG é : Constante')

elif razão > 1:
    print('A PG é: Crescente')
elif razão >=0 <=1:
    print('A PG é: Decrescente')
elif razão < 0:    
    print('A PG é: Oscilante')
soma_pg = sum(pg)
print("A soma dessa P.G é:", soma_pg)

posicao = int(input("Digite a posição (n) do elemento da P.G.: "))
if 1 <= posicao <= qt_elementos:
    valor_posicao = pg[posicao - 1]
    print(f"O valor do elemento na posição {posicao} é: {valor_posicao}")
else:
    print("Posição inválida!")