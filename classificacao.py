def exibe_classificacao(grupos, grupo):
    for i in range(len(grupos)):

        grupo_atual = grupos[i]

        grupo_atual.sort(
            key=lambda selecao: (
                selecao['pontos'],
                selecao['vitorias'],
                selecao['gols']
            ),
            reverse=True
        )
    
        print(f'(GRUPO {grupo[i]})')
        print(f'|{"Seleção":<15} |{"Pts":^7}| {"V":^3} | {"D":^3} | {"E":^3} | {"G":^4}|')
        print('-'*50)
        for selecao in grupo_atual:
            print(f'|{selecao["nome"]:<15} | {selecao["pontos"]:^5} | {selecao["vitorias"]:^3} | {selecao["derrotas"]:^3} | {selecao["empates"]:^3} | {selecao["gols"]:^3} |')
        print()


def atualizar_classificacao(time1, time2, resultado1, resultado2):
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