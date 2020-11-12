from datetime import datetime
from colorama import Fore
from time import sleep
import file_FM_IEP
import colorama
import libs
import os


current_date = datetime.now()
date = current_date.strftime("%d/%m/%Y")

colorama.init(autoreset=True)
name = os.environ['USERNAME']

print(Fore.RED + f'\n{" -> PRODUZIDO POR: VICTOR ALVES DE OLIVEIRA - 2020 V3.0 <- ": ^70}\n')
print(Fore.CYAN + f'\n{" INSTITUTO IEDA PICON ":=^70}')
print(Fore.CYAN + f'\n{f" OLÁ, PROFESSOR(A) {name.upper()} SEJA MUITO BEM-VINDO! ": ^70}')
print(Fore.CYAN + f'\n{f"{date}": ^70}')


sleep(1)

while True:
    libs.main()
    print(Fore.BLUE + f'{" FECHAMENTO DA MÉDIA ": ^70}')
    print('-'*70)
    
    print()

    classes = libs.read_int("-> TURMA QUE IRÁ FECHAR MÉDIA (Somente Número da série): ")
    quantity = libs.read_int(f"-> NÚMERO TOTAL DE ALUNOS DO {classes}° ANO: ")

    file_FM_IEP.add_average(f'\n{f" MEDIA FINAL {classes} ANO ":=^70}')
    file_FM_IEP.add_average('\nN | MEDIA FINAL | SITUACAO\n')
    file_FM_IEP.add_average(f"{'-'*26}\n")
    for student in range(quantity):
        print(f'\nFechando a Média: Número da Chamada -> {student+1}')
        grade1 = libs.prova('NOTA DA PROVA(6.0): ')
        grade2 = libs.teste('\nNOTA DO TESTE(1.0): ')
        grade3 = libs.atividade('\nNOTA DA ATIVIDADE 1(1.0): ')
        grade4 = libs.atividade('\nNOTA DA ATIVIDADE 2(1.0): ')
        grade5 = libs.atividade('\nNOTA DA ATIVIDADE 3(1.0): ')
        
        NF = grade1 + grade2 + grade3 + grade4 + grade5
        if NF > 6.75:
            situation = 'APROVADO'
        else:
            situation = 'REPROVADO'

        NF = str(NF)
        interger = int(NF[0])
        decimal = int(NF[2:4])

        print(Fore.YELLOW + f'NOTA FINAL : {NF}')

        if decimal <= 24:
            decimal = 00
        elif decimal >= 25 and decimal <=74:
            decimal = 50
        elif decimal >= 75:
            decimal = 00
            interger += 1
        elif interger >= 10:
            interger = 10
            decimal = 00

        final_grade = str(interger) + '.' + str(decimal)

        print(Fore.RED + f'\nMÉDIA FINAL: {final_grade} - {situation}!')
        print('='*70)        

        file_FM_IEP.add_average(f'{student+1:<2}|  {final_grade:<11}|{situation:>10}\n')
