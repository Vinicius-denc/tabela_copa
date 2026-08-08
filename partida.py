
import dados


def partida(time1, time2):
   
    # if indice_grupo >= len(grupos):
    #             indice_grupo = 0  

    
    #print(f'GRUPO {grupo[indice_grupo]}')
    print(f'{time1["nome"]} X {time2["nome"]}')
    print('Resultado:')

    
    resultado1 = ler_placar(time1['nome'])    
    print('X')
    resultado2 = ler_placar(time2['nome'])

    return resultado1, resultado2

    # Lista vazia, vou acrescentando as partidas para serem consultadas pela função resultados
def registrar_partida(time1, time2, resultado1, resultado2):
    dados.partidas_anteriores.append(f"{time1['nome']} {resultado1} X {resultado2} {time2['nome']}")


def ler_placar(time):
    
    while True:
        try:
            resultado = int(input(f'{time}:'))

            if resultado < 0:
                print('O placar não pode ser negativo!')
                continue

            return resultado
        except ValueError:
            print(f'Digite o placar do {time}')

def resultados(partidas_anteriores):

    #A variavel partida_anteriores vem da função partida
    if not partidas_anteriores:
        return 'Não há partidas para serem exibidas'
    else:
        return '\n'.join(partidas_anteriores)
    # o join() pega os itens da lista, junta eles e adiciona um separador, no caso o \n
