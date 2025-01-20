def xor_arquivo(arquivo_origem, palavra_passe, arquivo_destino):
    try:
        with open(arquivo_origem, 'rb') as f_origem, open(arquivo_destino, 'wb') as f_destino:
            ascii_palavra = [ord(c) for c in palavra_passe]
            for i, byte in enumerate(f_origem.read()):
                byte_xor = byte ^ ascii_palavra[i % len(ascii_palavra)]
                f_destino.write(bytes([byte_xor]))
        print("Processamento concluído com sucesso!")
    except Exception as e:
        print(f"Erro: {e}")

def main():
    arquivo_origem = input("Digite o nome do arquivo de origem: ")
    palavra_passe = input("Digite a palavra-passe: ")
    arquivo_destino = input("Digite o nome do arquivo de destino: ")
    xor_arquivo(arquivo_origem, palavra_passe, arquivo_destino)

if __name__ == "__main__":
    main()