from random import randint
from time import sleep
from os import system, name

itens = ('Pedra ✊', 'Papel 🖐', 'Tesoura ✌')

while True:
    computador = randint(0, 2)

    print('-=' * 10)
    print('Jo Ken Po!'.center(20))
    print('-=' * 10)

    jogador = int(input('''O que vai jogar?
[0] Pedra
[1] Papel
[2] Tesoura
Opção: '''))

    if 0 <= jogador <= 2:

        print('JO')
        sleep(.7)
        print('KEN')
        sleep(.7)
        print('PÔ!!!')

        print('-=' * 12)
        print(f'Jogador jogou {itens[jogador]}')
        print(f'Computador jogou {itens[computador]}')
        print('-=' * 12)

        if computador == 0:  # Computador escolheu PEDRA
            if jogador == 0:
                print('EMPATE')
            elif jogador == 1:
                print('JOGADOR VENCEU')
            elif jogador == 2:
                print('COMPUTADOR VENCEU')

        elif computador == 1:  # Computador escolheu PAPEL
            if jogador == 0:
                print('COMPUTADOR VENCEU')
            elif jogador == 1:
                print('EMPATE')
            elif jogador == 2:
                print('JOGADOR VENCEU')

        elif computador == 2:  # Computador escolheu TESOURA
            if jogador == 0:
                print('JOGADOR VENCEU')
            elif jogador == 1:
                print('COMPUTADOR VENCEU')
            elif jogador == 2:
                print('EMPATE')

        input('\nPressione ENTER para jogar de novo ')
        system('cls' if name == 'nt' else 'clear')
    else:
        print('Opção INVÁLIDA')
        input('\nPressione ENTER para jogar de novo ')
