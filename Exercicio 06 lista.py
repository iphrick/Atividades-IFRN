#Questão 06

sexo = input("Informe o sexo (masculino/feminino): ")
data_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")
data_inicio_contribuicao = input("Informe a data de início da contribuição previdenciária (DD/MM/AAAA): ")

sexo = sexo.lower()

dia_nascimento = int(data_nascimento[:2])
mes_nascimento = int(data_nascimento[3:5])
ano_nascimento = int(data_nascimento[6:])

dia_contribuicao = int(data_inicio_contribuicao[:2])
mes_contribuicao = int(data_inicio_contribuicao[3:5])
ano_contribuicao = int(data_inicio_contribuicao[6:])

idade_minima_homens = 65
idade_minima_mulheres = 62
tempo_contribuicao_homens = 35 * 365
tempo_contribuicao_mulheres = 30 * 365

if sexo == "masculino":
    idade_minima = idade_minima_homens
    tempo_contribuicao_minimo = tempo_contribuicao_homens
elif sexo == "feminino":
    idade_minima = idade_minima_mulheres
    tempo_contribuicao_minimo = tempo_contribuicao_mulheres
else:
    print("Sexo inválido.")
    exit()

data_nascimento_dias = ano_nascimento * 365 + mes_nascimento * 30 + dia_nascimento
data_inicio_contribuicao_dias = ano_contribuicao * 365 + mes_contribuicao * 30 + dia_contribuicao

if (data_inicio_contribuicao_dias - data_nascimento_dias) < 15 * 365:
    print("É necessário ter pelo menos 15 anos de contribuição.")
    exit()

idade = (365 * 2024 - data_nascimento_dias) // 365
tempo_contribuicao = (365 * 2024 - data_inicio_contribuicao_dias)

if idade >= idade_minima and tempo_contribuicao >= tempo_contribuicao_minimo:
    data_aposentadoria_dias = data_nascimento_dias + idade_minima * 365
    anos, dias_restantes = divmod(data_aposentadoria_dias, 365)
    meses, dias = divmod(dias_restantes, 30)
    print("Data de aposentadoria:", f"{dias}/{meses}/{anos}")
else:
    print("Você ainda não atende aos requisitos para aposentadoria.")