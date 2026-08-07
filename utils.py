import os


def pausar():
    input('\nPressione ENTER para continuar...')


def limpar_tela():
    if os.name == 'nt':      
        os.system('cls')
    else:                    
        os.system('clear')