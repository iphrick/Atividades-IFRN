# Um determinado material radioativo perde metade de sua massa a cada 50 segundos.
# Faça um programa que solicite a massa inicial (em gramas) e que calcule o tempo necessário para que
# essa massa se torne menor que 0,5 grama. Ao término, o programa deve exibir a massa inicial, a massa
# final e o tempo que levou para o decaimento (exiba o tempo informando horas, minutos e segundos).

#Solicitando a massa inicial

massa_inicial = (input('Digite a massa em gramas '))
massa_final_desejada = (0.5)
taxa_de_decaimento = 50
tempo = 0 
massa_atual = float(massa_inicial)

while massa_atual > massa_final_desejada:
   massa_atual/= 2   
   tempo +=taxa_de_decaimento

#convertendo o tempo para segundos

horas = str(int(tempo/3600)).zfill(2)
minutos=str(int(tempo/60)).zfill(2)
segundos = str(int(tempo%60)).zfill(2)

#Resultado 
print("Massa inicial: ",massa_inicial)
print("Massa Final: ",massa_atual)
print("Tempo de Decaimento: " ,horas,":",minutos,":",segundos)