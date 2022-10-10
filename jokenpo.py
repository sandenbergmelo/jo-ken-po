from random import randint
from time import sleep
from os import system, name

itens = ('Pedra ✊', 'Papel 🖐', 'Tesoura ✌')

while True:
    computador = randint(1, 3)

    print('-=' * 10)
    print('Jo Ken Po!'.center(20))
    print('-=' * 10)

    print('O que você escolhe?')
    print('[1] Pedra ✊')
    print('[2] Papel 🖐')
    print('[3] Tesoura ✌')
    jogador = int(input('Opção: '))

    if not 1 <= jogador <= 3:
        print('Opção inválida!')
        input('Pressione ENTER para continuar...')
        system('cls' if name == 'nt' else 'clear')
        continue

    print('JO')
    sleep(.7)
    print('KEN')
    sleep(.7)
    print('PÔ!!!')

    print('-=' * 12)
    print(f'Jogador jogou {itens[jogador - 1]}')
    print(f'Computador jogou {itens[computador - 1]}')
    print('-=' * 12)

    if computador == 1:  # Computador escolheu PEDRA
        if jogador == 1:
            print('EMPATE')
        elif jogador == 2:
            print('JOGADOR VENCEU')
        elif jogador == 3:
            print('COMPUTADOR VENCEU')

    elif computador == 2:  # Computador escolheu PAPEL
        if jogador == 1:
            print('COMPUTADOR VENCEU')
        elif jogador == 2:
            print('EMPATE')
        elif jogador == 3:
            print('JOGADOR VENCEU')

    elif computador == 3:  # Computador escolheu TESOURA
        if jogador == 1:
            print('JOGADOR VENCEU')
        elif jogador == 2:
            print('COMPUTADOR VENCEU')
        elif jogador == 3:
            print('EMPATE')

    input('\nPressione ENTER para jogar de novo ')
    system('cls' if name == 'nt' else 'clear')
