from colorama import Fore
import colorama

colorama.init(autoreset=True)

def add_average(txt):
    file = open('Quinto_Conceito.txt', 'a+')
    file.write(txt)
    file.close()


def open_file():
    try:
        file = open("Quinto_Conceito.txt", "a+")
    except:
        print(Fore.RED + '\nNÃO FOI POSSIVEL ABRIR O ARQUIVO Quinto_Conceito.txt!\n')
    else:
        print(Fore.GREEN + '\033[1;32mARQUIVO Quinto_Conceito.txt CRIADO COM SUCESSO!\n')
        file.close()


def read_file():
    try:
        file = open("Quinto_Conceito.txt", "r")
    except:
        print(Fore.RED + '\nNÃO FOI POSSIVEL ABRIR O ARQUIVO Quinto_Conceito.txt!\n')
    else:
        print(Fore.YELLOW + file.read())
        file.close()


def reset_file():
    file = open('Quinto_Conceito.txt', 'w+')
    file.close()
