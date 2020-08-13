import emoji

def read_int(txt):
    while True:
        try:
            read = int(input(txt))
        except (ValueError, TypeError, KeyboardInterrupt):
            print(emoji.emojize('\n\033[1;31mPOR FAVOR,UTILIZE APENAS NÚMEROS!\033[m:no_entry_sign:', use_aliases = True))
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
                print(emoji.emojize('\n\033[1;31mATENÇÃO! O VALOR MÁXIMO DA PROVA É DE 6 PONTOS\033[m:no_entry_sign:', use_aliases = True))
                prova = virgula(msg) 
        except ValueError:
            print(emoji.emojize('\n\033[1;31mPOR FAVOR,UTILIZE APENAS NOTAS VÁLIDAS!\033[m:no_entry_sign:', use_aliases = True))
        else:
            return prova

def teste(msg):
    while True:
        try:
            teste = virgula(msg)
            while teste > 1 or teste < 0:
                print(emoji.emojize('\n\033[1;31mATENÇÃO! O VALOR MÁXIMO DO TESTE É DE 1 PONTO \033[m:no_entry_sign:', use_aliases = True))
                teste = virgula(msg) 
        except ValueError:
            print(emoji.emojize('\n\033[1;31mPOR FAVOR,UTILIZE APENAS NOTAS VÁLIDAS!\033[m:no_entry_sign:', use_aliases = True))
        else:
            return teste

def atividade(msg):
    while True:
        try:
            atividade = virgula(msg)
            while atividade > 1 or atividade < 0:
                print(emoji.emojize('\n\033[1;31mATENÇÃO! O VALOR MÁXIMO DA ATIVIDADE 1 É DE 1 PONTO \033[m:no_entry_sign:', use_aliases = True))
                atividade = virgula(msg) 
        except ValueError:
            print(emoji.emojize('\n\033[1;31mPOR FAVOR,UTILIZE APENAS NOTAS VÁLIDAS!\033[m:no_entry_sign:', use_aliases = True))
        else:
            return atividade

def main():
    print("\n\033[1;95m-> O QUE DESEJA FAZER AGORA?\n[ 1 ] - FECHAR MAIS MÉDIAS.\n[ 2 ] - DAR UMA OLHADA NAS MÉDIAS JA FEITAS.\n[ 3 ] - APAGAR TODOS OS DADOS DO ARQUIVO.\n[ 4 ] - SAIR.\033[m ")
    option = read_int('\033[1;95m-> Sua Opção:\033[m')
    return option 
