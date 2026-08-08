#MELHORIAS
#mensagem de VAI COMEÇAR O JOGO!!!!
#classificação ordenada;
#melhorar a impressão da tabela;
#corrigir detalhes visuais.




#PROXIMO PASSO FASE DE GRUPOS.
#Limpar o menu quando digita um numero
#Adicionar gols tomados no criterio de desempate

#impedir partidas após o fim da fase de grupos OK
#limpar a tela do menu quando digitar caracteres aleatorios OK
#Melhorar a sequencia de partidas intercalando grupos OK
#Exibir a partida anterior OK
#Separar os arquivos OK
#Limpar a tela OK
#menu interativo (EM ANDAMENTO)
#Criar variavel do grupo igual a do time (time1 = grupos[indice_grupo][indice_time1]) OK
#Melhorar a exibição dos grupos
#ordenar os grupos por pontos
#verificar dados errados do usuário(no placar e no menu) OK
#CORRIGIR O PROBLEMA DO INDICE DOS JOGOS OK
#sistema de placar e pontos OK
#transformar os times em dicionários, acrescentar pontos, vitórias, derrotas e empates OK
#classificar os times por pontos OK
#arrumar sistema de pontuação OK
#fazer o cabeçalho da partida ser responsivo com o nome das seleções OK
#filtrar os dados dos resultados dos jogos OK
# deixar entradas do menu em minusculo  OK

import dados
from utils import pausar, limpar_tela
from classificacao import exibe_classificacao, atualizar_classificacao
from partida import partida, resultados, registrar_partida
from dados import define_rodada



indice_partidas = 0
indice_grupo = 0
encerra_programa = False
numero_de_partidas = 0


while not encerra_programa:
    print('COPA DO MUNDO 2026')
    print('(P) - Iniciar a partida\n'
          '(C) - Ver classificações\n'
          '(A) - Partida anterior\n'
          '(S) - Sair')  
    
    navegacao_menu = input('Escolha uma das opções: ').strip().lower()
    
    if navegacao_menu == 'p':

        if navegacao_menu == 'p':

            total_partidas_grupos = len(dados.grupos) * (
            len(dados.primeira_rodada)
            + len(dados.segunda_rodada)
            + len(dados.terceira_rodada)
        )

        if numero_de_partidas >= total_partidas_grupos:
            print('A fase de grupos terminou!')
            pausar()
            limpar_tela()
            continue

        rodada_atual = define_rodada(numero_de_partidas, dados.grupos, dados.primeira_rodada, dados.segunda_rodada, dados.terceira_rodada)

        grupo_atual = dados.grupos[indice_grupo]
        indice_time1, indice_time2 = rodada_atual[indice_partidas]

        time1 = grupo_atual[indice_time1]
        time2 = grupo_atual[indice_time2]


        limpar_tela()
        resultado1, resultado2 = partida(time1, time2)
        registrar_partida(time1, time2, resultado1,resultado2)
        atualizar_classificacao(time1, time2, resultado1, resultado2)


        numero_de_partidas +=1 
        indice_partidas +=1

        #  Faz o controle das trocas dos grupos da rodada
        if indice_partidas >= len(rodada_atual):
            indice_partidas = 0
            indice_grupo += 1

            if indice_grupo >=len(dados.grupos):
                indice_grupo = 0

        pausar()
        limpar_tela()
        
    elif navegacao_menu == 'c':

        limpar_tela()
        exibe_classificacao(dados.grupos, dados.grupo)
        pausar()
        limpar_tela()        

    elif navegacao_menu == 'a':
        
        limpar_tela()
        print(resultados(dados.partidas_anteriores))
        pausar()
        limpar_tela()
            
    elif navegacao_menu == 's':
        encerra_programa = True

    elif navegacao_menu == '':
        limpar_tela()
        #print('Opção inválida!')
        #pausar()
        limpar_tela()

    elif len(navegacao_menu) > 1:
        limpar_tela()


    else:
        continue
    














