from palavras import palavras
from tentativas import numeroTentativas
import random

def exibir_palavras(palavra, letras_adivinhadas):
    palavra_exibida = ''
    for letra in palavra:
        if letra in letras_adivinhadas:
            palavra_exibida += letra
        else:
            palavra_exibida += '-'
    return palavra_exibida

def jogo_da_forca():
    palavra = random.choice(palavras)
    letras_adivinhadas = []
    tentativas_restantes = numeroTentativas

    print("Bem-vindo ao Jogo da Forca!")
    print(exibir_palavras(palavra, letras_adivinhadas))

    while tentativas_restantes > 0:
        letra = input("Digite uma letra: ").lower()
        
        if letra in letras_adivinhadas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        letras_adivinhadas.append(letra)

        if letra in palavra:
            print(f"A letra '{letra}' está na palavra!")
        else:
            print(f"A letra '{letra}' não está na palavra!")
            tentativas_restantes -= 1
            print(f"Tentativas restantes: {tentativas_restantes}")

        palavra_exibida = exibir_palavras(palavra, letras_adivinhadas)
        print(palavra_exibida)

        if palavra_exibida == palavra:
            print("Parabéns! Você acertou a palavra!")
            break

    if tentativas_restantes == 0:
        print("Você perdeu! A palavra era:", palavra)

if __name__ == "__main__":
    jogo_da_forca()
