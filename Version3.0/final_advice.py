import file_final_advice
from colorama import Fore
import colorama
import libs


colorama.init(autoreset=True)


def comma_advice(msg):
    valid = False
    while not valid:
        inputed = input(msg).strip().replace(',', '.')
        return float(inputed)


def read_advice(txt):
    while True:
        try:
            read = comma_advice(txt)
        except (ValueError, TypeError, KeyboardInterrupt):
            print(Fore.RED + '\nPOR FAVOR, UTILIZE APENAS NÚMEROS!')
        else:
            return read


def average_final_advice():
    grade = {}
    classes = libs.read_int("-> TURMA QUE IRÁ FECHAR QUINTO CONCEITO (Somente Número da série): ")
    quantity = libs.read_int(f"-> NÚMERO TOTAL DE ALUNOS DO {classes}° ANO: ")

    file_final_advice.add_average(f'\n{f" QUINTO CONCEITO {classes}° ANO ":=^70}')
    file_final_advice.add_average('\nN | QUINTO CONCEITO | SITUACAO\n')
    file_final_advice.add_average(f"{'-'*31}\n")

    for student in range(quantity):
        print(f'\nFechando Quinto Conceito: Número da Chamada -> {student+1}')
        for bim in range(0, 4):
            bimestral = read_advice(f'\nNOTA FINAL {bim+1}° BIMESTRE: ')
            while bimestral > 10 or bimestral < 0:
                print(Fore.RED + '\nATENÇÃO! O VALOR MÁXIMO DO QUINTO CONCEITO É DE 10 PONTOS')
                bimestral = read_advice(f'\nNOTA FINAL {bim+1}° BIMESTRE: ')
            grade[f"{bim+1}° Bimestre"] = bimestral
            

        sumGrade = sum(grade.values())
        final_advice = sumGrade/4

        if final_advice > 6.75:
            situation = 'APROVADO'
        else:
            situation = 'REPROVADO'

        file_final_advice.add_average(f'{student+1:<2}| {final_advice:.2f}            |{situation:>10}\n')

        print(Fore.YELLOW + f'SOMATÓRIA DAS MÉDIAS: {sumGrade}')
        print(Fore.RED + f'\nQUINTO CONCEITO: {final_advice:.2f} - {situation}!')
