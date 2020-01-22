s_n = 's'
S = 69
while s_n == 's':
    from time import sleep
    from random import randint
    N = int(input('''\033[1;37m[Facil]\033[0;0m \033[1;32m3 Bombas\033[0;0m
\033[1;34m[Médio]\033[0;0m \033[1;32m6 Bombas\033[0;0m
\033[1;31m[Difícil]\033[0;0m \033[1;32m9 Bombas\033[0;0m
\033[1;33m[Impossível]\033[0;0m \033[1;32m15 Bombas\033[0;0m

\033[1;32mDigite a quantidade de bombas: \033[0;0m'''))
    while S == 69:
        rodada = 0
        matriz = []
        matriz_modificada = []
        banco_de_dados = []
        posições = []
        players = []
        posições2 = []
        contador = 0
        placar = 0
        if (N == 3) or (N == 6) or (N == 9) or (N == 15):
            for i in range(2):
                players.append(input('\033[1;32mDigite o nome de um dos jogadores: \033[0;0m'))
            for i in range(5):
                lista = []
                for x in range(5):
                    lista.append('*')
                matriz.append(lista)
            for i in range(5):
                for x in range(5):
                    print('\033[1;96m[\033[0;0m',matriz[i][x], end=' \033[1;96m]\033[0;0m')
                print()
            for i in range(5):
                lista2 = []
                for x in range(5):
                    lista2.append('*')
                matriz_modificada.append(lista2)
            for i in range(0,N):
                jogador_1 = input(f'\033[0;32m{players[0]}, em qual casa você quer colocar suas bombas? Digite primeiro a posição horizontal e depois a posição vertical: \033[0;0m').split(' ')
                jogador_1[0] = int(jogador_1[0]) #Posição de linhas
                jogador_1[1] = int(jogador_1[1]) #Posição de colunas
                while True:
                    if jogador_1[0] < 1 or jogador_1[0] > 5 or jogador_1[1] < 1 or jogador_1[1] > 5:
                        jogador_1 = input('[ERRO] Casa inválida, digite novamente: ').split(' ')
                        jogador_1[0] = int(jogador_1[0])  # Posição de linhas
                        jogador_1[1] = int(jogador_1[1])  # Posição de colunas
                    elif jogador_1 in posições:
                        jogador_1 = input('Essa casa já foi selecionada, tente novamente: ').split(' ')
                        jogador_1[0] = int(jogador_1[0])  # Posição de linhas
                        jogador_1[1] = int(jogador_1[1])  # Posição de colunas
                    else:
                        break
                matriz_modificada[jogador_1[1]-1][jogador_1[0]-1] = '\033[31m'+'1''\033[0;0m'
                posições.append(jogador_1)
                print('\033[1;31mBomba Adicionada!!!\033[0;0m')
            for i in range(100):
                print('')
            for i in range(5):
                for x in range(5):
                    print('\033[1;96m[\033[0;0m',matriz[i][x], end=' \033[1;96m]\033[0;0m')
                print()
            for i in range(0,10):
                jogador_2 = input(f'\033[1;32m{players[1]}, em qual casa você quer jogar? \033[0;0m').split(' ')
                jogador_2[0] = int(jogador_2[0])  # Posição de linhas
                jogador_2[1] = int(jogador_2[1])  # Posição de colunas
                while True:
                    if jogador_2[0] < 1 or jogador_2[0] > 5 or jogador_2[1] < 1 or jogador_2[1] > 5:
                        jogador_2 = input('[ERRO] Casa inválida, digite novamente: ').split(' ')
                        jogador_2[0] = int(jogador_2[0])  # Posição de linhas
                        jogador_2[1] = int(jogador_2[1])  # Posição de colunas
                    elif jogador_2 in posições2:
                        jogador_2 = input('Essa casa já foi selecionada, tente novamente: ').split(' ')
                        jogador_2[0] = int(jogador_2[0])  # Posição de linhas
                        jogador_2[1] = int(jogador_2[1])  # Posição de colunas
                    else:
                        break
                rodada += 1
                print(f'\033[1;36mRODADA: [{rodada}]\033[0;0m')
                if jogador_2 in posições:
                    for i in range(3):
                        print('\033[1;31mpi\033[0;0m')
                        sleep(0.5)
                    print('\033[1;31mVocê explodiu!\033[0;0m')
                    for i in range(3):
                        print('')
                    print(f'\033[1;35m[O jogador {players[0]}, venceu!]\033[0;0m')
                    for i in range(3):
                        print('')
                    print(f'\033[1;96mSeu placar final foi de: {placar}\033[0;0m')
                    print(f'\033[1;36mVocê terminou na rodada [{rodada}]!\033[0;0m')
                    break
                placar += 1
                contador += 1
                posições2.append(jogador_2)
                print(f'\033[1;38mSeu placar: {placar}\033[0;0m')
            if placar == 10:
                print(f'O jogador {players[1]}, venceu!')
            print('')
            print("\033[1;96mAs bombas são representadas pelo número 1\033[0;0m")
            for i in range(5):
                for x in range(5):
                    print('\033[1;96m[\033[0;0m',matriz_modificada[i][x], end=' \033[1;96m]\033[0;0m')
                print()
            print('')
            s_n = input("\033[1;32mVocê quer jogar novamente? s/n: \033[0;0m")
            if s_n == 's':
                N = int(input('''\033[1;37m[Facil]\033[0;0m \033[1;32m3 Bombas\033[0;0m
\033[1;34m[Médio]\033[0;0m \033[1;32m6 Bombas\033[0;0m
\033[1;31m[Difícil]\033[0;0m \033[1;32m9 Bombas\033[0;0m
\033[1;33m[Impossível]\033[0;0m \033[1;32m15 Bombas\033[0;0m

\033[1;32mDigite a quantidade de bombas: \033[0;0m'''))
            else:
                break
        else:
            N = int(input('''
\033[1;37m[Facil]\033[0;0m \033[1;32m3 Bombas\033[0;0m
\033[1;34m[Médio]\033[0;0m \033[1;32m6 Bombas\033[0;0m
\033[1;31m[Difícil]\033[0;0m \033[1;32m9 Bombas\033[0;0m
\033[1;33m[Impossível]\033[0;0m \033[1;32m15 Bombas\033[0;0m

\033[1;32mQuantidade de bombas inválida, digite novamente: \033[0;0m
'''))
