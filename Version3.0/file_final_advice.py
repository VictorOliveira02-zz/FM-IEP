from colorama import Fore
import colorama

colorama.init(autoreset=True)

def add_medias(txt):
    arquivo = open('Quinto_Conceito.txt', 'a+')
    arquivo.write(txt)
    arquivo.close()


def files():
    try:
        arquivo = open("Quinto_Conceito.txt", "a+")
    except:
        print(Fore.RED + '\nNÃO FOI POSSIVEL ABRIR O ARQUIVO Quinto_Conceito.txt!\n')
    else:
        print(Fore.GREEN + '\033[1;32mARQUIVO Quinto_Conceito.txt CRIADO COM SUCESSO!\n')
        arquivo.close()


def open_arquivo():
    try:
        arquivo = open("Quinto_Conceito.txt", "r")
    except:
        print(Fore.RED + '\nNÃO FOI POSSIVEL ABRIR O ARQUIVO Quinto_Conceito.txt!\n')
    else:
        print(Fore.YELLOW + arquivo.read())
        arquivo.close()


def reset():
    arquivo = open('Quinto_Conceito.txt', 'w+')
    arquivo.close()
