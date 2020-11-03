import file_final_advice
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
            print(Fore.RED + '\nPOR FAVOR, UTILIZE APENAS NÚMEROS!')
        else:
            return read


def media_final_advice():
    nota = {}
    turma = libs.read_int("-> TURMA QUE IRÁ FECHAR QUINTO CONCEITO (Somente Número da série): ")
    qnt = libs.read_int(f"-> NÚMERO TOTAL DE ALUNOS DO {turma}° ANO: ")

    file_final_advice.add_medias(f'\n{f" QUINTO CONCEITO {turma}° ANO ":=^70}')
    file_final_advice.add_medias('\nN | QUINTO CONCEITO | SITUACAO\n')
    file_final_advice.add_medias(f"{'-'*31}\n")

    for aluno in range(qnt):
        print(f'\nFechando Quinto Conceito: Número da Chamada -> {aluno+1}')
        for bim in range(0, 4):
            bimestre = read_advice(f'\nNOTA FINAL {bim+1}° BIMESTRE: ')
            while bimestre > 10 or bimestre < 0:
                print(Fore.RED + '\nATENÇÃO! O VALOR MÁXIMO DO QUINTO CONCEITO É DE 10 PONTOS')
                bimestre = read_advice(f'\nNOTA FINAL {bim+1}° BIMESTRE: ')
            nota[f"{bim+1}° Bimestre"] = bimestre
            

        sumGrade = sum(nota.values())
        media_final = sumGrade/4

        if media_final > 6.75:
            situation = 'APROVADO'
        else:
            situation = 'REPROVADO'

        file_final_advice.add_medias(f'{aluno+1:<2}| {media_final:.2f}            |{situation:>10}\n')

        print(Fore.YELLOW + f'SOMATÓRIA DAS MÉDIAS: {sumGrade}')
        print(Fore.RED + f'\nQUINTO CONCEITO: {media_final:.2f} - {situation}!')
