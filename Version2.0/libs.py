import colored
from colored import stylize

vermelho = colored.fg("red_1") + colored.attr("bold")
roxo = colored.fg("magenta") + colored.attr("bold")

def read_int(txt):
    while True:
        try:
            read = int(input(txt))
        except (ValueError, TypeError, KeyboardInterrupt):
            print(stylize('\nPOR FAVOR,UTILIZE APENAS NÚMEROS!', vermelho, colored.attr("underlined")))
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
                print(stylize('\nATENÇÃO! O VALOR MÁXIMO DA PROVA É DE 6 PONTOS', vermelho, colored.attr("underlined")))
                prova = virgula(msg) 
        except ValueError:
            print(stylize('\nPOR FAVOR,UTILIZE APENAS NOTAS VÁLIDAS!', vermelho, colored.attr("underlined")))
        else:
            return prova

def teste(msg):
    while True:
        try:
            teste = virgula(msg)
            while teste > 1 or teste < 0:
                print(stylize('\nATENÇÃO! O VALOR MÁXIMO DO TESTE É DE 1 PONTO ', vermelho, colored.attr("underlined")))
                teste = virgula(msg) 
        except ValueError:
            print(stylize('\nPOR FAVOR,UTILIZE APENAS NOTAS VÁLIDAS!', vermelho, colored.attr("underlined")))
        else:
            return teste

def atividade(msg):
    while True:
        try:
            atividade = virgula(msg)
            while atividade > 1 or atividade < 0:
                print(stylize('\nATENÇÃO! O VALOR MÁXIMO DA ATIVIDADE 1 É DE 1 PONTO ', vermelho, colored.attr("underlined")))
                atividade = virgula(msg) 
        except ValueError:
            print(stylize('\nPOR FAVOR,UTILIZE APENAS NOTAS VÁLIDAS!', vermelho, colored.attr("underlined")))
        else:
            return atividade

def main():
    print(stylize("\n-> O QUE DESEJA FAZER AGORA?\n[ 1 ] - FECHAR MAIS MÉDIAS.\n[ 2 ] - DAR UMA OLHADA NAS MÉDIAS JA FEITAS.\n[ 3 ] - APAGAR TODOS OS DADOS DO ARQUIVO.\n[ 4 ] - SAIR. ", roxo, colored.attr("underlined")))
    option = read_int(stylize('-> Sua Opção:', roxo, colored.attr("underlined")))
    return option 
