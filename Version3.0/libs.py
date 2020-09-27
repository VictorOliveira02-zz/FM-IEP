import colorama
from colorama import Fore

colorama.init(autoreset=True)

def read_int(txt):
    while True:
        try:
            read = int(input(txt))
        except (ValueError, TypeError, KeyboardInterrupt):
            print(Fore.RED + '\nPOR FAVOR,UTILIZE APENAS NÚMEROS!')
            continue
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
    print(Fore.MAGENTA + "\n-> O QUE DESEJA FAZER AGORA?\n[ 1 ] - FECHAR MÉDIAS.\n[ 2 ] - DAR UMA OLHADA NAS MÉDIAS JA FEITAS.\n[ 3 ] - APAGAR TODOS OS DADOS DO ARQUIVO.\n[ 4 ] - VER CALENDÁRIO.\n[ 5 ] - FECHAR QUINTO CONCEITO.\n[ 6 ] - SAIR.")
    option = read_int('-> Sua Opção:')
    return option
