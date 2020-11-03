from colorama import Fore
import colorama

colorama.init(autoreset=True)

def add_average(txt):
    file = open('FM_IEP.txt', 'a+')
    file.write(txt)
    file.close()


def open_file():
    try:
        file = open("FM_IEP.txt", "a+")
    except:
        print(Fore.RED + '\nNÃO FOI POSSIVEL ABRIR O ARQUIVO FM_IEP.txt!\n')
    else:
        print(Fore.GREEN + '\n\033[1;32mARQUIVO FM_IEP.txt CRIADO COM SUCESSO!\n')
        file.close()


def read_file():
    try:
        file = open("FM_IEP.txt", "r")
    except:
        print(Fore.RED + '\nNÃO FOI POSSIVEL ABRIR O ARQUIVO FM_IEP.txt!\n')
    else:
        print(Fore.YELLOW + file.read())
        file.close()


def reset_file():
    file = open('FM_IEP.txt', 'w+')
    file.close()
