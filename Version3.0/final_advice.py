from colorama import Fore
import libs
import colorama

colorama.init(autoreset=True)


def virgula_advice(msg):
    válido = False
    while not válido:
        entrada = str(msg).strip().replace(',', '.')
        return float(entrada)


def read_advice(txt):
    while True:
        try:
            read = virgula_advice(float(input(txt)))
        except (ValueError, TypeError, KeyboardInterrupt):
            print(Fore.RED + '\nPOR FAVOR,UTILIZE APENAS NÚMEROS!')
        else:
            return read

def situation_advice():
    situation_aprovado = 'APROVADO'
    situation_reprovado = 'REPROVADO'

    if media_final > 6.75:
        print(situation_aprovado)
    else:
        print(situation_reprovado)


def media_final_advice():
    nota = {}
    turma = libs.read_int("-> TURMA QUE IRÁ FECHAR QUINTO CONCEITO (Somente Número da série): ")
    qnt = libs.read_int(f"-> NÚMERO TOTAL DE ALUNOS DO {turma}° ANO: ")
    for aluno in range(qnt):
        print(f'\nFechando Quinto Conceito: Número da Chamada -> {aluno+1}')
        for bim in range(0, 4):
            bimestre = read_advice(f'Nota Final {bim+1}° Bimestre: ')
            nota[f"{bim+1}° Bimestre"] = bimestre
          
        media_final = sum(nota.values())
        print(Fore.RED + f'\nMÉDIA FINAL: {media_final/4:.f} - {situation_advice}!')

