
import dados



def partida(grupos, grupo, partidas, indice_grupo, indice_partidas):


    grupo_atual = grupos[indice_grupo]
    indice_time1, indice_time2 = partidas[indice_partidas]

    
    time1 = grupo_atual[indice_time1]
    time2 = grupo_atual[indice_time2]
    
    
    print(f'GRUPO {grupo[indice_grupo]}')
    print(f'{time1["nome"]} X {time2["nome"]}')
    print('Resultado:')

    
    resultado1 = ler_placar(time1['nome'])    
    print('X')
    resultado2 = ler_placar(time2['nome'])

    
    dados.partidas_anteriores.append(f'{time1['nome']} {resultado1} X {resultado2} {time2['nome']}')
    
    if resultado1 > resultado2:
        time1['pontos'] += 3
        time1['vitorias'] += 1
        time1['gols'] += resultado1
        time2['derrotas'] += 1
        time2['gols'] += resultado2
        
    elif resultado2 > resultado1:
        time2['pontos'] += 3
        time2['vitorias'] += 1
        time2['gols'] += resultado2
        time1['derrotas'] += 1
        time1['gols'] += resultado1

    else:
        time1['pontos'] += 1
        time1['gols'] += resultado1
        time1['empates'] += 1
        time2['pontos'] += 1 
        time2['gols'] += resultado2
        time2['empates'] += 1
        

    indice_partidas +=1

    if indice_partidas >= len(partidas):
        indice_partidas = 0
        indice_grupo += 1
    
    return indice_grupo, indice_partidas

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
    
    if not partidas_anteriores:
        return 'Não há partidas para serem exibidas'
    else:
        return '\n'.join(partidas_anteriores)