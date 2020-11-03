from colorama import Fore
import colorama
import libs


colorama.init(autoreset=True)


def virgula_advice(msg):
    válido = False
    while not válido:
        entrada = input(msg).strip().replace(',', '.')
        return float(entrada)


def read_advice(txt):
    while True:
        try:
            read = virgula_advice(txt)
        except (ValueError, TypeError, KeyboardInterrupt):
            print(Fore.RED + '\nPOR FAVOR,UTILIZE APENAS NÚMEROS!')
        else:
            return read


def media_final_advice():
    nota = {}
    turma = libs.read_int("-> TURMA QUE IRÁ FECHAR QUINTO CONCEITO (Somente Número da série): ")
    qnt = libs.read_int(f"-> NÚMERO TOTAL DE ALUNOS DO {turma}° ANO: ")
    for aluno in range(qnt):
        print(f'\nFechando Quinto Conceito: Número da Chamada -> {aluno+1}')
        for bim in range(0, 4):
            bimestre = read_advice(f'\nNOTA FINAL {bim+1}° BIMESTRE: ')
            nota[f"{bim+1}° Bimestre"] = bimestre
            

        media_final = sum(nota.values())

        if media_final > 6.75:
            situation = 'APROVADO'
        else:
            situation = 'REPROVADO'


        print(Fore.YELLOW + f'SOMATÓRIA DAS MÉDIAS: {media_final}')
        print(Fore.RED + f'\nQUINTO CONCEITO: {media_final/4:.2f} - {situation}!')
