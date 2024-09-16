#Faça um programa que solicite ao usuário um valor inteiro positivo e informe a
#quantidade de dígitos.

num = int(input('Informe um numero inteiro positivo: '))
contador = 0
if num <=0:
    print(" ERRO! Informe um numero positivo")

else:
   contador = 0
   while num > 0:
    num//= 10 
    contador += 1
   
    if contador == 0:
     contador = 1
print('O valor informado pussui :', contador,'Digitos')
        


       




    
    

    

        


   
   
