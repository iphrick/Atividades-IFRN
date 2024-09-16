# Faça um programa que:
# a) Solicite ao usuário um valor inteiro inicial e a razão da P.A.;
# b) Solicite um novo valor inteiro positivo correspondente a quantidade de elementos da P.A. e exiba
# os valores dessa P.A.;
# c) Informe se a P.A. é constante, crescente ou decrescente
# d) Calcule a soma dos elementos dessa P.A.;
# e) Solicite ao usuário um outro valor inteiro n correspondente a enésima posição de um elemento
# da P.A. e exibir o valor desse elemento.
import sys
valor_inicial = int(input('informe um valor inteiro inicial: '))
razão = int(input('informe a razão da P.A: '))
qt_elementos = int(input('informe um navo valor inteiro positivo correspondente a quantiade de elementos da P.A: '))

pa = []
for i in range(qt_elementos):
 elementos_pa = valor_inicial + i *razão
 pa.append(elementos_pa)

 print("Os valores dessa P.A são: ")
 for valor in pa:
     print(valor , end = ' ')
 print()

if qt_elementos < 0:
    print('informe um valor inteiro positivo')
    sys.exit
elif razão == 0:
    print('A PA é : Constante')

elif razão > 0:
    print('A PA é: Crescente')
elif razão < 0:
    print('A PA é: Decrescente')
soma_pa = sum(pa)
print("A soma dessa P.A é:", soma_pa)

posicao = int(input("Digite a posição (n) do elemento da P.A.: "))
if 1 <= posicao <= qt_elementos:
    valor_posicao = pa[posicao - 1]
    print(f"O valor do elemento na posição {posicao} é: {valor_posicao}")
else:
    print("Posição inválida!")

    
