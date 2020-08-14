from time import sleep
from arquivos import *   
from libs import *
from datetime import datetime
from pytz import timezone
import colored
from colored import stylize
import os

data_e_hora_atuais = datetime.now()
fuso_horario = timezone('America/Sao_Paulo')
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime("%d/%m/%Y %H:%M")

vermelho = colored.fg("red_1") + colored.attr("bold")
azul = colored.fg("cyan") + colored.attr("bold")
verde = colored.fg("green") + colored.attr("bold")
roxo = colored.fg("magenta") + colored.attr("bold")
amarelo = colored.fg("yellow") + colored.attr("bold")
verde_pale = colored.fg("deep_pink_3b") + colored.attr("bold")



name = os.environ['USERNAME']

print(stylize(f'\n{" -> PRODUZIDO POR: VICTOR ALVES DE OLIVEIRA - 2020 V2.0 <- ": ^70}\n', vermelho, colored.attr("underlined")))
print(stylize(f'\n{" INSTITUTO IEDA PICON ":=^70}', azul, colored.attr("underlined")))
print(stylize(f'\n{f" OLÁ, PROFESSOR(A) {name.upper()} SEJA MUITO BEM-VINDO ": ^70}', azul, colored.attr("underlined")))
print(stylize(f'\n{f" {data_e_hora_sao_paulo_em_texto} ": ^70}', azul, colored.attr("underlined")))


sleep(3)
files()

while True:
    sleep(2)
    print(stylize(f'{" FECHAMENTO DA MÉDIA ": ^70}', verde_pale, colored.attr("underlined")))
    print('-'*70)
    
    print()

    
    turma = read_int(stylize("-> TURMA QUE IRÁ FECHAR MÉDIA (Somente Número da série): ", roxo, colored.attr("underlined")))
    qnt = read_int(stylize(f"-> NÚMERO TOTAL DE ALUNOS DO {turma}° ANO: ", roxo, colored.attr("underlined")))

    add_medias(f'\n{f" MEDIA FINAL {turma} ANO ":=^70}')
    add_medias('\nN | MEDIA FINAL | SITUACAO\n')
    add_medias(f"{'-'*26}\n")
    for aluno in range(qnt):
        n1 = prova(stylize('\nNOTA DA PROVA(6.0): ', amarelo, colored.attr("underlined")))
        n2 = teste(stylize('\nNOTA DO TESTE(1.0): ', amarelo, colored.attr("underlined")))
        n3 = atividade(stylize('\nNOTA DA ATIVIDADE 1(1.0): ', amarelo, colored.attr("underlined")))
        n4 = atividade(stylize('\nNOTA DA ATIVIDADE 2(1.0): ', amarelo, colored.attr("underlined")))
        n5 = atividade(stylize('\nNOTA DA ATIVIDADE 3(1.0): ', amarelo, colored.attr("underlined")))
        
        NF = n1 + n2 + n3 + n4 + n5
        if NF > 6.75:
            situacao = 'APROVADO'
        else:
            situacao = 'REPROVADO'

        if NF >= 0 and NF <= 0.24:
            print(stylize(f'NOTA FINAL : {NF:.2f}', amarelo, colored.attr("underlined")))
            NF = 0.0
            print(stylize(f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO!', vermelho, colored.attr("underlined")))
            print('='*70)
        elif NF > 0.24 and NF <= 0.74:
            print(stylize(f'NOTA FINAL : {NF:.2f}', amarelo, colored.attr("underlined")))
            NF = 0.5
            print(stylize(f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ', vermelho, colored.attr("underlined")))
            print('='*70)
        elif NF > 0.74 and NF < 1:
            print(stylize(f'NOTA FINAL : {NF:.2f}', amarelo, colored.attr("underlined")))
            NF = 1.0
            print(stylize(f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ', vermelho, colored.attr("underlined")))
            print('='*70)
        elif NF >= 1 and NF <= 1.24:
            print(stylize(f'NOTA FINAL : {NF:.2f}', amarelo, colored.attr("underlined")))
            NF = 1.0
            print(stylize(f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ', vermelho, colored.attr("underlined")))
            print('='*70)
        elif NF > 1.24 and NF <= 1.74:
            print(stylize(f'NOTA FINAL : {NF:.2f}', amarelo, colored.attr("underlined")))
            NF = 1.5
            print(stylize(f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ', vermelho, colored.attr("underlined")))
            print('='*70)
        elif NF > 1.74 and NF < 2:
            print(stylize(f'NOTA FINAL : {NF:.2f}', amarelo, colored.attr("underlined")))
            NF = 2.0
            print(stylize(f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ', vermelho, colored.attr("underlined")))
            print('='*70)   
        elif NF >= 2 and NF <= 2.24:
            print(stylize(f'NOTA FINAL : {NF:.2f}', amarelo, colored.attr("underlined")))
            NF = 2.0
            print(stylize(f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ', vermelho, colored.attr("underlined")))
            print('='*70)
        elif NF > 2.24 and NF <= 2.74:
            print(stylize(f'NOTA FINAL : {NF:.2f}', amarelo, colored.attr("underlined")))
            NF = 2.5
            print(stylize(f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ', vermelho, colored.attr("underlined")))
            print('='*70)
        elif NF > 2.74 and NF < 3:
            print(stylize(f'NOTA FINAL : {NF:.2f}', amarelo, colored.attr("underlined")))
            NF = 3.0
            print(stylize(f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ', vermelho, colored.attr("underlined")))
            print('='*70)
        elif NF >= 3 and NF <= 3.24:
            print(stylize(f'NOTA FINAL : {NF:.2f}', amarelo, colored.attr("underlined")))
            NF = 3.0
            print(stylize(f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ', vermelho, colored.attr("underlined")))
            print('='*70)
        elif NF > 3.24 and NF <= 3.74:
            print(stylize(f'NOTA FINAL : {NF:.2f}', amarelo, colored.attr("underlined")))
            NF = 3.5
            print(stylize(f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ', vermelho, colored.attr("underlined")))
            print('='*70)
        elif NF > 3.74 and NF < 4:
            print(stylize(f'NOTA FINAL : {NF:.2f}', amarelo, colored.attr("underlined")))
            NF = 4.0
            print(stylize(f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ', vermelho, colored.attr("underlined")))
            print('='*70)
        elif NF >= 4 and NF <= 4.24:
            print(stylize(f'NOTA FINAL : {NF:.2f}', amarelo, colored.attr("underlined")))
            NF = 4.0
            print(stylize(f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ', vermelho, colored.attr("underlined")))
            print('='*70)
        elif NF > 4.24 and NF <= 4.74:
            print(stylize(f'NOTA FINAL : {NF:.2f}', amarelo, colored.attr("underlined")))
            NF = 4.5
            print(stylize(f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ', vermelho, colored.attr("underlined")))
            print('='*70)
        elif NF > 4.74 and NF < 5:
            print(stylize(f'NOTA FINAL : {NF:.2f}', amarelo, colored.attr("underlined")))
            NF = 5.0
            print(stylize(f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ', vermelho, colored.attr("underlined")))
            print('='*70)
        elif NF >= 5 and NF <= 5.24:
            print(stylize(f'NOTA FINAL : {NF:.2f}', amarelo, colored.attr("underlined")))
            NF = 5.0
            print(stylize(f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ', vermelho, colored.attr("underlined")))
            print('='*70)
        elif NF > 5.24 and NF <= 5.74:
            print(stylize(f'NOTA FINAL : {NF:.2f}', amarelo, colored.attr("underlined")))
            NF = 5.5
            print(stylize(f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ', vermelho, colored.attr("underlined")))
            print('='*70)
        elif NF > 5.74 and NF < 6:
            print(stylize(f'NOTA FINAL : {NF:.2f}', amarelo, colored.attr("underlined")))
            NF = 6.0
            print(stylize(f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ', vermelho, colored.attr("underlined")))
            print('='*70)
        elif NF >= 6 and NF <= 6.24:
            print(stylize(f'NOTA FINAL : {NF:.2f}', amarelo, colored.attr("underlined")))
            NF = 6.0
            print(stylize(f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ', vermelho, colored.attr("underlined")))
            print('='*70)
        elif NF > 6.24 and NF <= 6.74:
            print(stylize(f'NOTA FINAL : {NF:.2f}', amarelo, colored.attr("underlined")))
            NF = 6.5
            print(stylize(f'\nMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO! ', vermelho, colored.attr("underlined")))
            print('='*70)
        elif NF > 6.74 and NF < 7:
            print(stylize(f'NOTA FINAL : {NF:.2f}', amarelo, colored.attr("underlined")))
            NF = 7.0
            print(stylize(f'\nMÉDIA FINAL: {NF:.2f} - ALUNO APROVADO!', verde, colored.attr("underlined")))
            print('='*70) 
            print('='*70) 
        elif NF >= 7 and NF <= 7.24:
            print(stylize(f'NOTA FINAL : {NF:.2f}', amarelo, colored.attr("underlined")))
            NF = 7.0
            print(stylize(f'\nMÉDIA FINAL: {NF:.2f} - ALUNO APROVADO!', verde, colored.attr("underlined")))
            print('='*70)  
        elif NF > 7.24 and NF <= 7.74:
            print(stylize(f'NOTA FINAL : {NF:.2f}', amarelo, colored.attr("underlined")))
            NF = 7.5
            print(stylize(f'\nMÉDIA FINAL: {NF:.2f} - ALUNO APROVADO!', verde, colored.attr("underlined")))
            print('='*70)  
        elif NF > 7.74 and NF < 8:
            print(stylize(f'NOTA FINAL : {NF:.2f}', amarelo, colored.attr("underlined")))
            NF = 8.0
            print(stylize(f'\nMÉDIA FINAL: {NF:.2f} - ALUNO APROVADO!', verde, colored.attr("underlined")))
            print('='*70)  
        elif NF >= 8 and NF <= 8.24:
            print(stylize(f'NOTA FINAL : {NF:.2f}', amarelo, colored.attr("underlined")))
            NF = 8.0
            print(stylize(f'\nMÉDIA FINAL: {NF:.2f} - ALUNO APROVADO!', verde, colored.attr("underlined")))
            print('='*70)  
        elif NF > 8.24 and NF <= 8.74:
            print(stylize(f'NOTA FINAL : {NF:.2f}', amarelo, colored.attr("underlined")))
            NF = 8.5
            print(stylize(f'\nMÉDIA FINAL: {NF:.2f} - ALUNO APROVADO!', verde, colored.attr("underlined")))
            print('='*70)  
        elif NF > 8.74 and NF < 9:
            print(stylize(f'NOTA FINAL : {NF:.2f}', amarelo, colored.attr("underlined")))
            NF = 9.0
            print(stylize(f'\nMÉDIA FINAL: {NF:.2f} - ALUNO APROVADO!', verde, colored.attr("underlined")))
            print('='*70)    
        elif NF >= 9 and NF <= 9.24:
            print(stylize(f'NOTA FINAL : {NF:.2f}', amarelo, colored.attr("underlined")))
            NF = 9.0
            print(stylize(f'\nMÉDIA FINAL: {NF:.2f} - ALUNO APROVADO!', verde, colored.attr("underlined")))
            print('='*70)  
        elif NF > 9.24 and NF <= 9.74:
            print(stylize(f'NOTA FINAL : {NF:.2f}', amarelo, colored.attr("underlined")))
            NF = 9.5
            print(stylize(f'\nMÉDIA FINAL: {NF:.2f} - ALUNO APROVADO!', verde, colored.attr("underlined")))
            print('='*70)  
        elif NF > 9.74 and NF < 10:
            print(stylize(f'NOTA FINAL : {NF:.2f}', amarelo, colored.attr("underlined")))
            NF = 10.0
            print(stylize(f'\nMÉDIA FINAL: {NF:.2f} - ALUNO APROVADO!', verde, colored.attr("underlined")))
            print('='*70)  
        elif NF == 10:
            print(stylize(f'NOTA FINAL : {NF:.2f}', amarelo, colored.attr("underlined")))
            NF = 10.0
            print(stylize(f'\nMÉDIA FINAL: {NF:.2f} - ALUNO APROVADO!', verde, colored.attr("underlined")))
            print('='*70)

        add_medias(f'{aluno+1:<2}|  {NF:<11}|{situacao:>10}\n')

    option = main()

    if option == 1:
        print(stylize('[ 1 ] - FECHAR MAIS MÉDIAS.', roxo, colored.attr("underlined")))
        continue
    elif option == 2:
        print(stylize('[ 2 ] - DAR UMA OLHADA NAS MÉDIAS JA FEITAS.', roxo, colored.attr("underlined")))
        print(stylize(f'\nAGUARDE SÓ UM POUQINHO, APROVEITE PARA BEBER UM POUCO DE ÁGUA...', azul, colored.attr("underlined")))
        sleep(4)
        open_arquivo()
        main()
    elif option == 3:
        print(stylize('[ 3 ] - APAGAR TODOS OS DADOS DO ARQUIVO.', roxo, colored.attr("underlined")))
        print(stylize(f'\nAGUARDE SÓ UM POUQINHO, APROVEITE PARA BEBER UM POUCO DE ÁGUA...', azul, colored.attr("underlined")))
        sleep(4)
        reset()
        continue
    elif option == 4:
        print(stylize(f'{f"ATÉ MAIS, PROFESSOR(A) {name.upper()}. OBRIGADO POR UTILIZAR!": ^80}', verde, colored.attr("underlined")))
        print('-'*70)
        break
    while True:
        if option > 4 or option < 0:
            print(stylize('\nPOR FAVOR,ESCOLHA UMA OPÇÃO VÁLIDA!', vermelho, colored.attr("underlined")))
            main()    
