import random
import time
from os import system as sys

#### Variaveis a utilizar ####
# count -> contador de erros
# letra -> letra que o usuário informou
# lista_palavras -> lista com as palavras que serão usadas no jogo
# palavra -> palavra selecionada de forma aleatória pelo programa
# amostra -> recebe "_" com a quantidade de letras da palavra selecionada

def main():
    global descobrir
    global count
    global display
    global lista_de_palavras
    global palavra
    global chutes
    global letra
    global nome

    chutes = []
    lista_de_palavras = ["aba", "jornal"]
    palavra = random.choice(lista_de_palavras)
    display = "-" * len(palavra)
    count =  0
    descobrir = len(palavra)


def print_forca():
    if count == 0:
        print("""
     _______
    |       |
    |       |
    |
    |
    |
 ___|___
        """)
    elif count == 1:
        print("""
     _______
    |       |
    |       |
    |       O
    |
    |
 ___|___
    """)
    elif count == 2:
        print("""
     _______
    |       |
    |       |
    |       O
    |       |
    |
 ___|___""")
    elif count == 3:
        print("""
     _______
    |       |
    |       |
    |       O
    |      /|
    |
 ___|___""")
    elif count == 4:
        print("""
     _______
    |       |
    |       |
    |       O
    |      /|\\
    |
 ___|___""")
    elif count == 5:
        print("""
     _______
    |       |
    |       |
    |       O
    |      /|\\
    |      / 
 ___|___""")
    elif count == 6:
        print("""
     _______
    |       |
    |       |
    |       O
    |      /|\\
    |      / \\
 ___|___""")


def letra_in_palavra():
    global count, descobrir, display, chutes, letra
    if letra in chutes:
        print("Já tentaste esta letra!")
        time.sleep(1)
        return

    chutes.append(letra)
    if letra in palavra:
        indice = []
        for (l, i) in zip(palavra, range(len(palavra))):
            if l == letra:
                indice.append(i)
        for i in indice:
            display = display[:i]+letra+display[i+1:]

        descobrir -= len(indice)
    else:
        count += 1


def loop_letra():
    global count, descobrir, letra, chutes
    while True:
        if (count == 6) or (descobrir == 0):
            break

        print(chutes)
        print_forca()
        print(display)
        letra = input("letra: ").strip()
        letra_in_palavra()
        sys('cls') # cls -> clear

    print(display)
    print_forca()


def menu():
    nome = input('Informe seu nome: ')
    print(f"Seja bem vindo, {nome}.")
    while True:
        esperar_e_limpar()
        sim_nao = input("Deseja jogar? S - (sim) ou N - (não).\nOpção: ")
        if sim_nao.upper() == "S":
            main()
            loop_letra()
        elif sim_nao.upper() == "N":
            print(f"Até logo, {nome}!")
            exit()
        else:
            print("Informe uma opão válida")


def esperar_e_limpar(sleep:int=1):
    time.sleep(sleep)
    sys('cls') # system('clear')

menu()
