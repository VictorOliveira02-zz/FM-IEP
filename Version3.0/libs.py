from datetime import datetime
from calendar import calendar
from colorama import Fore
from time import sleep
import final_advice
import colorama
import arquivos
import os

name = os.environ['USERNAME']
colorama.init(autoreset=True)


def read_int(txt):
    while True:
        try:
            read = int(input(txt))
        except (ValueError, TypeError, KeyboardInterrupt):
            print(Fore.RED + '\nPOR FAVOR,UTILIZE APENAS NÚMEROS!')
        else:
            return read

def virgula(msg):
    válido = False
    while not válido:
        entrada = input(msg).strip().replace(',', '.')
        return float(entrada)


def prova(msg):
    while True:
        try:
            prova = virgula(msg)
            while prova > 6 or prova < 0:
                print(Fore.RED + '\nATENÇÃO! O VALOR MÁXIMO DA PROVA É DE 6 PONTOS')
                prova = virgula(msg) 
        except ValueError:
            print(Fore.RED + '\nPOR FAVOR,UTILIZE APENAS NOTAS VÁLIDAS!')
        else:
            return prova


def teste(msg):
    while True:
        try:
            teste = virgula(msg)
            while teste > 1 or teste < 0:
                print(Fore.RED + '\nATENÇÃO! O VALOR MÁXIMO DO TESTE É DE 1 PONTO ')
                teste = virgula(msg) 
        except ValueError:
            print(Fore.RED + '\nPOR FAVOR,UTILIZE APENAS NOTAS VÁLIDAS!')
        else:
            return teste


def atividade(msg):
    while True:
        try:
            atividade = virgula(msg)
            while atividade > 1 or atividade < 0:
                print(Fore.RED + '\nATENÇÃO! O VALOR MÁXIMO DA ATIVIDADE 1 É DE 1 PONTO ')
                atividade = virgula(msg) 
        except ValueError:
            print(Fore.RED + '\nPOR FAVOR,UTILIZE APENAS NOTAS VÁLIDAS!')
        else:
            return atividade


def main():
    print(Fore.MAGENTA + f'\n{" MENU PRINCIPAL ":=^70}')
    print(Fore.MAGENTA + "\n-> O QUE DESEJA FAZER AGORA?\n[ 1 ] - FECHAR MÉDIAS.\n[ 2 ] - DAR UMA OLHADA NAS MÉDIAS JÁ FEITAS.\n[ 3 ] - APAGAR TODOS OS DADOS DO ARQUIVO.\n[ 4 ] - VER CALENDÁRIO.\n[ 5 ] - FECHAR QUINTO CONCEITO.\n[ 6 ] - SAIR.")
    option = read_int('-> Sua Opção:')

    if option > 6 or option < 0:
        print(Fore.RED + '\nPOR FAVOR,ESCOLHA UMA OPÇÃO VÁLIDA!')
        main()
    else:
        if option == 1:
            print(Fore.MAGENTA + '[ 1 ] - FECHAR MÉDIAS.')
            pass
        elif option == 2:
            print(Fore.MAGENTA + '[ 2 ] - DAR UMA OLHADA NAS MÉDIAS JÁ FEITAS.')
            print(Fore.BLUE + f'\nAGUARDE SÓ UM POUQINHO, APROVEITE PARA BEBER UM POUCO DE ÁGUA...')
            sleep(2)
            arquivos.open_arquivo()
            main()
        elif option == 3:
            print(Fore.MAGENTA + '[ 3 ] - APAGAR TODOS OS DADOS DO ARQUIVO FM_IEP.txt.')
            print(Fore.BLUE + f'\nAGUARDE SÓ UM POUQINHO, APROVEITE PARA BEBER UM POUCO DE ÁGUA...')
            print('Apagando Dados do Arquivo...')
            sleep(2)
            arquivos.reset()
            print('Dados do Arquivo apagados com Sucesso!')
            main()
        elif option == 4:
            print(Fore.MAGENTA + '[ 4 ] - VER CALENDÁRIO.')
            print(Fore.BLUE + f'\nAGUARDE SÓ UM POUQINHO, APROVEITE PARA BEBER UM POUCO DE ÁGUA...')
            print('-'*70)
            sleep(2)
            now = datetime.now()
            print(calendar(now.year))
            print('-'*70)
            main()
        elif option == 5:
            print(Fore.MAGENTA + '[ 5 ] - FECHAR QUINTO CONCEITO.\n')
            final_advice.media_final_advice()
            main()
        elif option == 6:
            print(Fore.GREEN + f'{f"ATÉ MAIS, PROFESSOR(A) {name.upper()}. OBRIGADO POR UTILIZAR!": ^80}')
            print('-'*70)
            exit()
