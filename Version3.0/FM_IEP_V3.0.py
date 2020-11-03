from datetime import datetime
from colorama import Fore
from pytz import timezone
from time import sleep
import colorama
import arquivos
import libs
import os


data_e_hora_atuais = datetime.now()
fuso_horario = timezone('America/Sao_Paulo')
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime("%d/%m/%Y")

colorama.init(autoreset=True)
name = os.environ['USERNAME']

print(Fore.RED + f'\n{" -> PRODUZIDO POR: VICTOR ALVES DE OLIVEIRA - 2020 V3.0 <- ": ^70}\n')
print(Fore.CYAN + f'\n{" INSTITUTO IEDA PICON ":=^70}')
print(Fore.CYAN + f'\n{f" OLÁ, PROFESSOR(A) {name.upper()} SEJA MUITO BEM-VINDO! ": ^70}')
print(Fore.CYAN + f'\n{f" {data_e_hora_sao_paulo_em_texto} ": ^70}')


sleep(1)

while True:
    libs.main()
    print(Fore.BLUE + f'{" FECHAMENTO DA MÉDIA ": ^70}')
    print('-'*70)
    
    print()

    turma = libs.read_int("-> TURMA QUE IRÁ FECHAR MÉDIA (Somente Número da série): ")
    qnt = libs.read_int(f"-> NÚMERO TOTAL DE ALUNOS DO {turma}° ANO: ")

    arquivos.add_medias(f'\n{f" MEDIA FINAL {turma} ANO ":=^70}')
    arquivos.add_medias('\nN | MEDIA FINAL | SITUACAO\n')
    arquivos.add_medias(f"{'-'*26}\n")
    for aluno in range(qnt):
        print(f'\nFechando a Média: Número da Chamada -> {aluno+1}')
        n1 = libs.prova('NOTA DA PROVA(6.0): ')
        n2 = libs.teste('\nNOTA DO TESTE(1.0): ')
        n3 = libs.atividade('\nNOTA DA ATIVIDADE 1(1.0): ')
        n4 = libs.atividade('\nNOTA DA ATIVIDADE 2(1.0): ')
        n5 = libs.atividade('\nNOTA DA ATIVIDADE 3(1.0): ')
        
        NF = n1 + n2 + n3 + n4 + n5
        if NF > 6.75:
            situacao = 'APROVADO'
        else:
            situacao = 'REPROVADO'

        NF = str(NF)
        inteiro = int(NF[0])
        decimal = int(NF[2:4])

        print(Fore.YELLOW + f'NOTA FINAL : {NF}')

        if decimal <= 24:
            decimal = 00
        elif decimal >= 25 and decimal <=74:
            decimal = 50
        elif decimal >= 75:
            decimal = 00
            inteiro += 1
        elif inteiro >= 10:
            inteiro = 10
            decimal = 00

        nota_final = str(inteiro) + '.' + str(decimal)

        print(Fore.RED + f'\nMÉDIA FINAL: {nota_final} - {situacao}!')
        print('='*70)        

        arquivos.add_medias(f'{aluno+1:<2}|  {nota_final:<11}|{situacao:>10}\n')
