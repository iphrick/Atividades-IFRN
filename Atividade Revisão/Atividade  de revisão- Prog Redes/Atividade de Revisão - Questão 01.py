import json
from tabulate import tabulate


def validar_ip(ip):
    try:
        octetos = list(map(int, ip.split('.')))
        if len(octetos) != 4 or not all(0 <= o <= 255 for o in octetos):
            raise ValueError
        return True
    except (ValueError, TypeError):
        return False


def ip_para_inteiro(ip):
    return sum(int(octeto) << (8 * (3 - i)) for i, octeto in enumerate(ip.split('.')))


def inteiro_para_ip(ip_int):
    return '.'.join(str((ip_int >> (8 * (3 - i))) & 0xFF) for i in range(4))


def calcular_subrede(ip, mascara):
    ip_int = ip_para_inteiro(ip)
    mascara_bin = (0xffffffff << (32 - mascara)) & 0xffffffff
    endereco_rede_int = ip_int & mascara_bin
    broadcast_int = endereco_rede_int | (~mascara_bin & 0xffffffff)

    return {
        "endereco_rede": inteiro_para_ip(endereco_rede_int),
        "primeiro_host": inteiro_para_ip(endereco_rede_int + 1),
        "ultimo_host": inteiro_para_ip(broadcast_int - 1),
        "endereco_broadcast": inteiro_para_ip(broadcast_int),
        "mascara_decimal": inteiro_para_ip(mascara_bin),
        "mascara_binario": bin(mascara_bin)[2:].zfill(32),
        "num_hosts_validos": (2 ** (32 - mascara)) - 2
    }


def main():
    ip = input("Digite o endereço IP inicial: ")
    if not validar_ip(ip): 
        return print("IP inválido.")

    try:
        mascara_inicial = int(input("Digite a máscara de rede inicial (0 a 32): "))
        mascara_final = int(input("Digite a máscara de rede final (0 a 32): "))
        if not (0 <= mascara_inicial <= 32 and 0 <= mascara_final <= 32) or mascara_inicial > mascara_final:
            raise ValueError
    except ValueError:
        return print("Máscaras de rede inválidas.")

    resultados = [calcular_subrede(ip, mascara) for mascara in range(mascara_inicial, mascara_final + 1)]
    
    cabecalho = ["Máscara", "Endereço de Rede", "Primeiro Host", "Último Host", "Endereço de Broadcast", "Máscara (Decimal)", "Máscara (Binário)", "Hosts Válidos"]
    tabela = [
        [mascara, res["endereco_rede"], res["primeiro_host"], res["ultimo_host"], res["endereco_broadcast"], 
         res["mascara_decimal"], res["mascara_binario"], res["num_hosts_validos"]] 
        for mascara, res in zip(range(mascara_inicial, mascara_final + 1), resultados)
    ]

    print(tabulate(tabela, headers=cabecalho, tablefmt="grid"))

    try:
        with open("resultados_subrede.json", "a") as f:
            json.dump(resultados, f, indent=4)
            f.write("\n")
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")


if __name__ == "__main__":
    main()