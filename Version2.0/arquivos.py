import emoji

def add_medias(txt):
    arquivo = open('FM_IEP.txt', 'a+')
    arquivo.write(txt)
    arquivo.close()

def files():
    try:
        arquivo = open("FM_IEP.txt", "a+")
    except:
        print(emoji.emojize('\n\033[1;31mNÃO FOI POSSIVEL ABRIR O ARQUIVO FM_IEP.txt!:-1:\n\033[m', use_aliases = True))
    else:
        print(emoji.emojize('\n\033[1;32mARQUIVO FM_IEP.txt CRIADO COM SUCESSO!:+1:\n\033[m', use_aliases = True))
        arquivo.close()

def open_arquivo():
    try:
        arquivo = open("FM_IEP.txt", "r")
    except:
        print(emoji.emojize('\n\033[1;31mNÃO FOI POSSIVEL ABRIR O ARQUIVO FM_IEP.txt!:-1:\n\033[m', use_aliases = True))
    else:
        print(arquivo.read())
        arquivo.close()

def reset():
    arquivo = open('FM_IEP.txt', 'w+')
    arquivo.close()
