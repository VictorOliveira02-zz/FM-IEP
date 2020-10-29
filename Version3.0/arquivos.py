from colorama import Fore
import colorama

colorama.init(autoreset=True)

def add_medias(txt):
    arquivo = open('FM_IEP.txt', 'a+')
    arquivo.write(txt)
    arquivo.close()


def files():
    try:
        arquivo = open("FM_IEP.txt", "a+")
    except:
        print(Fore.RED + '\nNÃO FOI POSSIVEL ABRIR O ARQUIVO FM_IEP.txt!\n')
    else:
        print(Fore.GREEN + '\n\033[1;32mARQUIVO FM_IEP.txt CRIADO COM SUCESSO!\n')
        arquivo.close()


def open_arquivo():
    try:
        arquivo = open("FM_IEP.txt", "r")
    except:
        print(Fore.RED + '\nNÃO FOI POSSIVEL ABRIR O ARQUIVO FM_IEP.txt!\n')
    else:
        print(Fore.YELLOW + arquivo.read())
        arquivo.close()


def reset():
    arquivo = open('FM_IEP.txt', 'w+')
    arquivo.close()
