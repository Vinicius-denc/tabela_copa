def criar_selecao(nome):
    return {
        'nome': nome,
        'pontos': 0,
        'vitorias': 0,
        'derrotas': 0,
        'empates': 0,
        'gols': 0
    }

grupos = [
    [
        criar_selecao('Mexico'),
        criar_selecao('Africa do Sul'),
        criar_selecao('Coreia do Sul'),
        criar_selecao('Tchequia')
    ],
    [
        criar_selecao('Suiça'),
        criar_selecao('Canada'),
        criar_selecao('Bosnia'),
        criar_selecao('Catar')
    ],
    [
        criar_selecao('Brasil'),
        criar_selecao('Marrocos'),
        criar_selecao('Escocia'),
        criar_selecao('Haiti')
    ],
    [
        criar_selecao('Estados Unidos'),
        criar_selecao('Australia'),
        criar_selecao('Paraguai'),
        criar_selecao('Turquia')
    ], 
    [
        criar_selecao('Alemanha'),
        criar_selecao('Costa do Marfim'),
        criar_selecao('Equador'),
        criar_selecao('Curaçao')
    ],
    [
        criar_selecao('Paises Baixos'),
        criar_selecao('Japao'),
        criar_selecao('Suecia'),
        criar_selecao('Tunisia')
    ],
    [
        criar_selecao('Belgica'),
        criar_selecao('Egito'),
        criar_selecao('Ira'),
        criar_selecao('Nova Zelandia')
    ],
    [
        criar_selecao('Espanha'),
        criar_selecao('Cabo Verde'),
        criar_selecao('Uruguai'),
        criar_selecao('Arabia Saudita')
    ],
    [
        criar_selecao('França'),
        criar_selecao('Noruega'),
        criar_selecao('Senegal'),
        criar_selecao('Iraque')
    ],
    [
        criar_selecao('Argentina'),
        criar_selecao('Austria'),
        criar_selecao('Argelia'),
        criar_selecao('Jordania')
    ], 
    [
        criar_selecao('Colombia'),
        criar_selecao('Portugal'),
        criar_selecao('Congo'),
        criar_selecao('Uzbequistao')
    ], 
    [
        criar_selecao('Inglaterra'),
        criar_selecao('Croacia'),
        criar_selecao('Gana'),
        criar_selecao('Panama')
    ]
]

grupo = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L')

partidas = ((0,1),(2,3),(3,1),(0,2),(1,2),(3,0))



partidas_anteriores = []
