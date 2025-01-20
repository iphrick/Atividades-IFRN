import random

def ler_palavras(arquivo):
    with open(arquivo, 'r') as file:
        return [linha.strip() for linha in file if 5 <= len(linha.strip()) <= 8]

def fornecer_feedback(palavra, tentativa):
    return " ".join(
        f"\033[32m{letra}\033[0m" if letra == palavra[i] else
        f"\033[33m{letra}\033[0m" if letra in palavra else
        f"\033[90m{letra}\033[0m"
        for i, letra in enumerate(tentativa)
    )

def jogar():
    palavra_sorteada = random.choice(ler_palavras('arquivo_palavras.txt'))
    for tentativa_num in range(1, 7):
        tentativa = input(f"Tentativa {tentativa_num}/6: ").strip().lower()
        
        if len(tentativa) != len(palavra_sorteada):
            print(f"A palavra deve ter {len(palavra_sorteada)} letras. Tente novamente.")
            continue
        
        print(fornecer_feedback(palavra_sorteada, tentativa))
        
        if tentativa == palavra_sorteada:
            print(f"Parabéns! Você acertou a palavra em {tentativa_num} tentativas.")
            return
        
    print(f"Você perdeu! A palavra era: {palavra_sorteada}")

if __name__ == "__main__":
    jogar()