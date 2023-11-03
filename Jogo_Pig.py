'''
Projeto sobre >Pig<
Um jogo de várias pessoas
Os jogadores rolam um dado de 6 dados e acumulam a pontuação que recebam como "pontos por rodada", eles podem escolher 
quantas vezes rodam o dado durante a sua rodada. Caso, durante as rolagens o jogador tire 1 no dado, todos os seus pontos 
acumulados são zerados e ele perde a rodada.
'''

import random

def rolagem():
    valor_mini = 1
    valor_max = 6
    rolagem = random.randint(valor_mini,valor_max)

    return rolagem

while True:
    jogadores = input('Quantas pessoas estarão jogando?(escolha entre 2 a 4)')
    if jogadores.isdigit():
        jogadores = int(jogadores)
        if 2 <= jogadores <=4:
            break
        else:
            print('O jogo precisa de 2 a 4 pessoas para ser jogado!')
    else:
        print('Valor inválido. Por favor, digite um número de 2 a 4')

pontuacao_max = 30
pontos_jogador = [0 for _ in range(jogadores)   ]

while max(pontos_jogador) < pontuacao_max:

    for jogadores_idx in range(jogadores):
        print('\nO turno do `{}ª jogador acabou de começar!!'.format(jogadores_idx+1))
        print('Sua pontuação total é de: {}\n'.format(pontos_jogador[jogadores_idx]))
        pontuacao_atual = 0

        while True:    
            continuar = input('Você gostaria de tentar rolar o dado? (s)')
            if continuar.lower () != "s":
                break
            
            valor = rolagem ()

            if valor == 1:
                print('Você rolou 1! Acabou seu turno!')
                pontuacao_atual = 0
                break
            else:
                pontuacao_atual += valor
                print('Você rolou um :{}'.format(valor))

            print('A sua pontuação é {}'.format(pontuacao_atual))

        pontos_jogador[jogadores_idx] += pontuacao_atual
        print('Sua pontuação total é: {}'.format(pontos_jogador[jogadores_idx]))

max_pontos = max(pontos_jogador)
vencedor_idx = pontos_jogador.index(max_pontos)
print('\nO jogador {} é o vencedor com uma pontuação finald de {} pontos!'.format(vencedor_idx,max_pontos))

#Número aleatorio entre 1 a 6
#Verificar se o jogador quer continuar