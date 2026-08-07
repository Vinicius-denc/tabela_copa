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
