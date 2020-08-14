import colored
from colored import stylize

vermelho = colored.fg("red_1") + colored.attr("bold")
verde = colored.fg("green") + colored.attr("bold")
verde_olive = colored.fg("dark_olive_green_3b") + colored.attr("bold")

def add_medias(txt):
    arquivo = open('FM_IEP.txt', 'a+')
    arquivo.write(txt)
    arquivo.close()

def files():
    try:
        arquivo = open("FM_IEP.txt", "a+")
    except:
        print(stylize('\nNÃO FOI POSSIVEL ABRIR O ARQUIVO FM_IEP.txt!\n', vermelho, colored.attr("underlined")))
    else:
        print(stylize('\n\033[1;32mARQUIVO FM_IEP.txt CRIADO COM SUCESSO!\n', verde, colored.attr("underlined")))
        arquivo.close()

def open_arquivo():
    try:
        arquivo = open("FM_IEP.txt", "r")
    except:
        print(stylize('\nNÃO FOI POSSIVEL ABRIR O ARQUIVO FM_IEP.txt!\n', vermelho, colored.attr("underlined")))
    else:
        print(stylize(arquivo.read(), verde_olive, colored.attr("underlined")))
        arquivo.close()

def reset():
    arquivo = open('FM_IEP.txt', 'w+')
    arquivo.close()
