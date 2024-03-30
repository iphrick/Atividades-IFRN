#Exercicio 03

hora_partida = int(input("Hora de partida (formato 24 horas): "))
minuto_partida = int(input("Minuto de partida: "))
hora_chegada = int(input("Hora de chegada (formato 24 horas): "))
minuto_chegada = int(input("Minuto de chegada: "))
segundos_parados = int(input("Número de segundos parados para descanso: "))
litros_combustivel = float(input("Número de litros de combustível gasto (em litros): "))
preco_combustivel = float(input("Preço do litro de combustível (em R$): "))
distancia_percorrida = float(input("Distância percorrida (em Km): "))

hora_partida_segundos = hora_partida * 3600 + minuto_partida * 60
hora_chegada_segundos = hora_chegada * 3600 + minuto_chegada * 60
tempo_viagem_segundos = hora_chegada_segundos - hora_partida_segundos - segundos_parados


velocidade_media_global = distancia_percorrida / (tempo_viagem_segundos / 3600)

tempo_em_movimento_segundos = tempo_viagem_segundos - segundos_parados
velocidade_media_movimento = distancia_percorrida / (tempo_em_movimento_segundos / 3600)

custo_viagem_combustivel = litros_combustivel * preco_combustivel

desempenho_km_por_litro = distancia_percorrida / litros_combustivel
desempenho_litros_por_hora = litros_combustivel / (tempo_viagem_segundos / 3600)
desempenho_custo_por_km = custo_viagem_combustivel / distancia_percorrida


print("Dados da viagem:")
print("Tempo de viagem:", tempo_viagem_segundos, "segundos")
print("Velocidade média global:", round(velocidade_media_global, 2), "Km/h")
print("Velocidade média em movimento:", round(velocidade_media_movimento, 2), "Km/h")
print("Custo da viagem com combustível: R$", round(custo_viagem_combustivel, 2))
print("Desempenho do carro:")
print("- Km/l:", round(desempenho_km_por_litro, 2))
print("- Litros/h:", round(desempenho_litros_por_hora, 2))
print("- R$/Km:", round(desempenho_custo_por_km, 2))