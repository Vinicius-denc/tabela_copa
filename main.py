#MELHORIAS

#mensagem de VAI COMEÇAR O JOGO!!!!
#classificação ordenada;
#impedir partidas após o fim da fase de grupos;
#melhorar a impressão da tabela;
#corrigir detalhes visuais.




#PROXIMO PASSO FASE DE GRUPOS.
#Melhorar a sequencia de partidas intercalando grupos

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
from classificacao import exibe_classificacao
from partida import partida, resultados


numero_de_partidas = 0
indice_partidas = 0
indice_grupo = 0
encerra_programa = False


while not encerra_programa:
    print('COPA DO MUNDO 2026')
    print('(P) - Iniciar a partida\n'
          '(C) - Ver classificações\n'
          '(A) - Partida anterior\n'
          '(S) - Sair')  
    
    navegacao_menu = input('Escolha uma das opções: ').strip().lower()
    
    if navegacao_menu == 'p':
        
        limpar_tela()
        indice_grupo, indice_partidas = partida(numero_de_partidas, dados.grupos, dados.grupo, dados.primeira_rodada, dados.segunda_rodada, dados.terceira_rodada, indice_grupo, indice_partidas)
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

    else:
        continue
    














