from datetime import datetime
from time import sleep
from pytz import timezone
from colorama import Fore
from calendar import calendar
import colorama
import os
import sys  

sys.path.append('C:\\Users\\victo\\Desktop\\Victor\\Programação\\Linguagem Python\\FM _IEP\\Version 2.0\\libs.py')
import libs

sys.path.append('C:\\Users\\victo\\Desktop\\Victor\\Programação\\Linguagem Python\\FM _IEP\\Version 2.0\\arquivos.py')
import arquivos


data_e_hora_atuais = datetime.now()
fuso_horario = timezone('America/Sao_Paulo')
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime("%d/%m/%Y %H:%M")

colorama.init(autoreset=True)

name = os.environ['USERNAME']

print(Fore.RED + f'\n{" -> PRODUZIDO POR: VICTOR ALVES DE OLIVEIRA - 2020 V2.1 <- ": ^70}\n')
print(Fore.CYAN + f'\n{" INSTITUTO IEDA PICON ":=^70}')
print(Fore.CYAN + f'\n{f" OLÁ, PROFESSOR(A) {name.upper()} SEJA MUITO BEM-VINDO ": ^70}')
print(Fore.CYAN + f'\n{f" {data_e_hora_sao_paulo_em_texto} ": ^70}')


sleep(3)
arquivos.files()

while True:
    sleep(2)
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

        if NF >= 0 and NF <= 0.24:
            print(Fore.YELLOW + f'NOTA FINAL : {NF:.2f}')
            NF = 0.0
            print(Fore.RED + f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO!')
            print('='*70)
        elif NF > 0.24 and NF <= 0.74:
            print(Fore.YELLOW + f'NOTA FINAL : {NF:.2f}')
            NF = 0.5
            print(Fore.RED + f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ')
            print('='*70)
        elif NF > 0.74 and NF < 1:
            print(Fore.YELLOW + f'NOTA FINAL : {NF:.2f}')
            NF = 1.0
            print(Fore.RED + f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ')
            print('='*70)
        elif NF >= 1 and NF <= 1.24:
            print(Fore.YELLOW + f'NOTA FINAL : {NF:.2f}')
            NF = 1.0
            print(Fore.RED + f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ')
            print('='*70)
        elif NF > 1.24 and NF <= 1.74:
            print(Fore.YELLOW + f'NOTA FINAL : {NF:.2f}')
            NF = 1.5
            print(Fore.RED + f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ')
            print('='*70)
        elif NF > 1.74 and NF < 2:
            print(Fore.YELLOW + f'NOTA FINAL : {NF:.2f}')
            NF = 2.0
            print(Fore.RED + f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ')
            print('='*70)   
        elif NF >= 2 and NF <= 2.24:
            print(Fore.YELLOW + f'NOTA FINAL : {NF:.2f}')
            NF = 2.0
            print(Fore.RED + f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ')
            print('='*70)
        elif NF > 2.24 and NF <= 2.74:
            print(Fore.YELLOW + f'NOTA FINAL : {NF:.2f}')
            NF = 2.5
            print(Fore.RED + f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ')
            print('='*70)
        elif NF > 2.74 and NF < 3:
            print(Fore.YELLOW + f'NOTA FINAL : {NF:.2f}')
            NF = 3.0
            print(Fore.RED + f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ')
            print('='*70)
        elif NF >= 3 and NF <= 3.24:
            print(Fore.YELLOW + f'NOTA FINAL : {NF:.2f}')
            NF = 3.0
            print(Fore.RED + f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ')
            print('='*70)
        elif NF > 3.24 and NF <= 3.74:
            print(Fore.YELLOW + f'NOTA FINAL : {NF:.2f}')
            NF = 3.5
            print(Fore.RED + f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ')
            print('='*70)
        elif NF > 3.74 and NF < 4:
            print(Fore.YELLOW + f'NOTA FINAL : {NF:.2f}')
            NF = 4.0
            print(Fore.RED + f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ')
            print('='*70)
        elif NF >= 4 and NF <= 4.24:
            print(Fore.YELLOW + f'NOTA FINAL : {NF:.2f}')
            NF = 4.0
            print(Fore.RED + f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ')
            print('='*70)
        elif NF > 4.24 and NF <= 4.74:
            print(Fore.YELLOW + f'NOTA FINAL : {NF:.2f}')
            NF = 4.5
            print(Fore.RED + f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ')
            print('='*70)
        elif NF > 4.74 and NF < 5:
            print(Fore.YELLOW + f'NOTA FINAL : {NF:.2f}')
            NF = 5.0
            print(Fore.RED + f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ')
            print('='*70)
        elif NF >= 5 and NF <= 5.24:
            print(Fore.YELLOW + f'NOTA FINAL : {NF:.2f}')
            NF = 5.0
            print(Fore.RED + f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ')
            print('='*70)
        elif NF > 5.24 and NF <= 5.74:
            print(Fore.YELLOW + f'NOTA FINAL : {NF:.2f}')
            NF = 5.5
            print(Fore.RED + f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ')
            print('='*70)
        elif NF > 5.74 and NF < 6:
            print(Fore.YELLOW + f'NOTA FINAL : {NF:.2f}')
            NF = 6.0
            print(Fore.RED + f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ')
            print('='*70)
        elif NF >= 6 and NF <= 6.24:
            print(Fore.YELLOW + f'NOTA FINAL : {NF:.2f}')
            NF = 6.0
            print(Fore.RED + f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ')
            print('='*70)
        elif NF > 6.24 and NF <= 6.74:
            print(Fore.YELLOW + f'NOTA FINAL : {NF:.2f}')
            NF = 6.5
            print(Fore.RED + f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ')
            print('='*70)
        elif NF > 6.74 and NF < 7:
            print(Fore.YELLOW + f'NOTA FINAL : {NF:.2f}')
            NF = 7.0
            print(Fore.GREEN + f'\nMÉDIA FINAL: {NF:.2f} - ALUNO APROVADO!')
            print('='*70) 
            print('='*70) 
        elif NF >= 7 and NF <= 7.24:
            print(Fore.YELLOW + f'NOTA FINAL : {NF:.2f}')
            NF = 7.0
            print(Fore.GREEN + f'\nMÉDIA FINAL: {NF:.2f} - ALUNO APROVADO!')
            print('='*70)  
        elif NF > 7.24 and NF <= 7.74:
            print(Fore.YELLOW + f'NOTA FINAL : {NF:.2f}')
            NF = 7.5
            print(Fore.GREEN + f'\nMÉDIA FINAL: {NF:.2f} - ALUNO APROVADO!')
            print('='*70)  
        elif NF > 7.74 and NF < 8:
            print(Fore.YELLOW + f'NOTA FINAL : {NF:.2f}')
            NF = 8.0
            print(Fore.GREEN + f'\nMÉDIA FINAL: {NF:.2f} - ALUNO APROVADO!')
            print('='*70)  
        elif NF >= 8 and NF <= 8.24:
            print(Fore.YELLOW + f'NOTA FINAL : {NF:.2f}')
            NF = 8.0
            print(Fore.GREEN + f'\nMÉDIA FINAL: {NF:.2f} - ALUNO APROVADO!')
            print('='*70)  
        elif NF > 8.24 and NF <= 8.74:
            print(Fore.YELLOW + f'NOTA FINAL : {NF:.2f}')
            NF = 8.5
            print(Fore.GREEN + f'\nMÉDIA FINAL: {NF:.2f} - ALUNO APROVADO!')
            print('='*70)  
        elif NF > 8.74 and NF < 9:
            print(Fore.YELLOW + f'NOTA FINAL : {NF:.2f}')
            NF = 9.0
            print(Fore.GREEN + f'\nMÉDIA FINAL: {NF:.2f} - ALUNO APROVADO!')
            print('='*70)    
        elif NF >= 9 and NF <= 9.24:
            print(Fore.YELLOW + f'NOTA FINAL : {NF:.2f}')
            NF = 9.0
            print(Fore.GREEN + f'\nMÉDIA FINAL: {NF:.2f} - ALUNO APROVADO!')
            print('='*70)  
        elif NF > 9.24 and NF <= 9.74:
            print(Fore.YELLOW + f'NOTA FINAL : {NF:.2f}')
            NF = 9.5
            print(Fore.GREEN + f'\nMÉDIA FINAL: {NF:.2f} - ALUNO APROVADO!')
            print('='*70)  
        elif NF > 9.74 and NF < 10:
            print(Fore.YELLOW + f'NOTA FINAL : {NF:.2f}')
            NF = 10.0
            print(Fore.GREEN + f'\nMÉDIA FINAL: {NF:.2f} - ALUNO APROVADO!')
            print('='*70)  
        elif NF == 10:
            print(Fore.YELLOW + f'NOTA FINAL : {NF:.2f}')
            NF = 10.0
            print(Fore.GREEN + f'\nMÉDIA FINAL: {NF:.2f} - ALUNO APROVADO!')
            print('='*70)

        arquivos.add_medias(f'{aluno+1:<2}|  {NF:<11}|{situacao:>10}\n')

    options = libs.main()

    if options == 1:
        print(Fore.MAGENTA + '[ 1 ] - FECHAR MÉDIAS.')
        continue
    elif options == 2:
        print(Fore.MAGENTA + '[ 2 ] - DAR UMA OLHADA NAS MÉDIAS JA FEITAS.')
        print(Fore.BLUE + f'\nAGUARDE SÓ UM POUQINHO, APROVEITE PARA BEBER UM POUCO DE ÁGUA...')
        sleep(4)
        arquivos.open_arquivo()
        libs.main()
    elif options == 3:
        print(Fore.MAGENTA + '[ 3 ] - APAGAR TODOS OS DADOS DO ARQUIVO.')
        print(Fore.BLUE + f'\nAGUARDE SÓ UM POUQINHO, APROVEITE PARA BEBER UM POUCO DE ÁGUA...')
        print('Apagando Dados do Arquivo...')
        sleep(4)
        arquivos.reset()
        libs.main()
    elif options == 4:
        print(Fore.MAGENTA + '[ 4 ] - VER CALENDÁRIO.')
        print(Fore.BLUE + f'\nAGUARDE SÓ UM POUQINHO, APROVEITE PARA BEBER UM POUCO DE ÁGUA...')
        print('-'*70)
        sleep(4)
        now = datetime.now()
        print(calendar(now.year))
        print('-'*70)
        sleep(3)
        libs.main()
    elif options == 5:
        print(Fore.MAGENTA + '[ 1 ] - FECHAR QUINTO CONCEITO.')
        pass
    elif options == 6:
        print(Fore.GREEN + f'{f"ATÉ MAIS, PROFESSOR(A) {name.upper()}. OBRIGADO POR UTILIZAR!": ^80}')
        print('-'*70)
        break
    while True:
        if options > 6 or options < 0:
            print(Fore.RED + '\nPOR FAVOR,ESCOLHA UMA OPÇÃO VÁLIDA!')
            libs.main()
