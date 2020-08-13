from time import sleep
from arquivos import *   
from libs import *
from datetime import datetime
from pytz import timezone
import emoji
import os

data_e_hora_atuais = datetime.now()
fuso_horario = timezone('America/Sao_Paulo')
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime("%d/%m/%Y %H:%M")


name = os.environ['USERNAME']

print(f'\n\033[4;31m{" -> PRODUZIDO POR: VICTOR ALVES DE OLIVEIRA - 2020 V2.0 <- ": ^70}\033[m\n')
print(f'\n\033[1;36m{" INSTITUTO IEDA PICON ":=^70}\033[m')
print(emoji.emojize(f'\n\033[1;36m{f" OLÁ, PROFESSOR(A) {name.upper()} SEJA MUITO BEM VINDO :grinning: :v: ": ^80}\033[m', use_aliases = True))
print(f'\n\033[1;36m{f" {data_e_hora_sao_paulo_em_texto} ": ^70}\033[m')


sleep(3)
files()

while True:
    sleep(2)
    print(f'\033[1;34m{" FECHAMENTO DA MÉDIA ": ^70}\033[m')
    print('-'*70)
    
    print()

    
    turma = read_int("\033[1;95m-> TURMA QUE IRÁ FECHAR MÉDIA (Somente Número da série):\033[m ")
    qnt = read_int(f"\033[1;95m-> NÚMERO TOTAL DE ALUNOS DO {turma}° ANO:\033[m ")

    add_medias(f'\n{f" MEDIA FINAL {turma} ANO ":=^70}')
    add_medias('\nN | MEDIA FINAL | SITUACAO\n')
    add_medias(f"{'-'*26}\n")
    for aluno in range(qnt):
        n1 = prova('\n\033[1;33mNOTA DA PROVA\033[m(6.0): ')
        n2 = teste('\n\033[1;33mNOTA DO TESTE\033[m(1.0): ')
        n3 = atividade('\n\033[1;33mNOTA DA ATIVIDADE 1\033[m(1.0): ')
        n4 = atividade('\n\033[1;33mNOTA DA ATIVIDADE 2\033[m(1.0): ')
        n5 = atividade('\n\033[1;33mNOTA DA ATIVIDADE 3\033[m(1.0): ')
        
        NF = n1 + n2 + n3 + n4 + n5
        if NF > 6.75:
            situacao = 'APROVADO'
        else:
            situacao = 'REPROVADO'

        if NF >= 0 and NF <= 0.24:
            print(f'\033[1;33mNOTA FINAL :\033[m {NF:.2f}')
            NF = 0.0
            print(emoji.emojize(f'\n\033[1;31mMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO!\033[m:sweat:', use_aliases = True))
        elif NF > 0.24 and NF <= 0.74:
            print(f'\033[1;33mNOTA FINAL :\033[m {NF:.2f}')
            NF = 0.5
            print(emoji.emojize(f'\n\033[1;31mMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO!\033[m :sweat:', use_aliases = True))
        elif NF > 0.74 and NF < 1:
            print(f'\033[1;33mNOTA FINAL :\033[m {NF:.2f}')
            NF = 1.0
            print(emoji.emojize(f'\n\033[1;31mMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO!\033[m :sweat:', use_aliases = True))
        elif NF >= 1 and NF <= 1.24:
            print(f'\033[1;33mNOTA FINAL :\033[m {NF:.2f}')
            NF = 1.0
            print(emoji.emojize(f'\n\033[1;31mMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO!\033[m :sweat:', use_aliases = True))
        elif NF > 1.24 and NF <= 1.74:
            print(f'\033[1;33mNOTA FINAL :\033[m {NF:.2f}')
            NF = 1.5
            print(emoji.emojize(f'\n\033[1;31mMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO!\033[m :sweat:', use_aliases = True))
        elif NF > 1.74 and NF < 2:
            print(f'\033[1;33mNOTA FINAL :\033[m {NF:.2f}')
            NF = 2.0
            print(emoji.emojize(f'\n\033[1;31mMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO!\033[m :sweat:', use_aliases = True))   
        elif NF >= 2 and NF <= 2.24:
            print(f'\033[1;33mNOTA FINAL :\033[m {NF:.2f}')
            NF = 2.0
            print(emoji.emojize(f'\n\033[1;31mMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO!\033[m :sweat:', use_aliases = True))
        elif NF > 2.24 and NF <= 2.74:
            print(f'\033[1;33mNOTA FINAL :\033[m {NF:.2f}')
            NF = 2.5
            print(emoji.emojize(f'\n\033[1;31mMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO!\033[m :sweat:', use_aliases = True))
        elif NF > 2.74 and NF < 3:
            print(f'\033[1;33mNOTA FINAL :\033[m {NF:.2f}')
            NF = 3.0
            print(emoji.emojize(f'\n\033[1;31mMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO!\033[m :sweat:', use_aliases = True))
        elif NF >= 3 and NF <= 3.24:
            print(f'\033[1;33mNOTA FINAL :\033[m {NF:.2f}')
            NF = 3.0
            print(emoji.emojize(f'\n\033[1;31mMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO!\033[m :sweat:', use_aliases = True))
        elif NF > 3.24 and NF <= 3.74:
            print(f'\033[1;33mNOTA FINAL :\033[m {NF:.2f}')
            NF = 3.5
            print(emoji.emojize(f'\n\033[1;31mMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO!\033[m :sweat:', use_aliases = True))
        elif NF > 3.74 and NF < 4:
            print(f'\033[1;33mNOTA FINAL :\033[m {NF:.2f}')
            NF = 4.0
            print(emoji.emojize(f'\n\033[1;31mMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO!\033[m :sweat:', use_aliases = True))
        elif NF >= 4 and NF <= 4.24:
            print(f'\033[1;33mNOTA FINAL :\033[m {NF:.2f}')
            NF = 4.0
            print(emoji.emojize(f'\n\033[1;31mMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO!\033[m :sweat:', use_aliases = True))
        elif NF > 4.24 and NF <= 4.74:
            print(f'\033[1;33mNOTA FINAL :\033[m {NF:.2f}')
            NF = 4.5
            print(emoji.emojize(f'\n\033[1;31mMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO!\033[m :sweat:', use_aliases = True))
        elif NF > 4.74 and NF < 5:
            print(f'\033[1;33mNOTA FINAL :\033[m {NF:.2f}')
            NF = 5.0
            print(emoji.emojize(f'\n\033[1;31mMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO!\033[m :sweat:', use_aliases = True))
        elif NF >= 5 and NF <= 5.24:
            print(f'\033[1;33mNOTA FINAL :\033[m {NF:.2f}')
            NF = 5.0
            print(emoji.emojize(f'\n\033[1;31mMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO!\033[m :sweat:', use_aliases = True))
        elif NF > 5.24 and NF <= 5.74:
            print(f'\033[1;33mNOTA FINAL :\033[m {NF:.2f}')
            NF = 5.5
            print(emoji.emojize(f'\n\033[1;31mMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO!\033[m :sweat:', use_aliases = True))
        elif NF > 5.74 and NF < 6:
            print(f'\033[1;33mNOTA FINAL :\033[m {NF:.2f}')
            NF = 6.0
            print(emoji.emojize(f'\n\033[1;31mMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO!\033[m :sweat:', use_aliases = True))
        elif NF >= 6 and NF <= 6.24:
            print(f'\033[1;33mNOTA FINAL :\033[m {NF:.2f}')
            NF = 6.0
            print(emoji.emojize(f'\n\033[1;31mMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO!\033[m :sweat:', use_aliases = True))
        elif NF > 6.24 and NF <= 6.74:
            print(f'\033[1;33mNOTA FINAL :\033[m {NF:.2f}')
            NF = 6.5
            print(emoji.emojize(f'\n\033[1;31mMÉDIA FINAL: {NF:.2f} - ALUNO REPROVADO!\033[m :sweat:', use_aliases = True))
        elif NF > 6.74 and NF < 7:
            print(f'\033[1;33mNOTA FINAL :\033[m {NF:.2f}')
            NF = 7.0
            print(emoji.emojize(f'\n\033[1;32mMÉDIA FINAL: {NF:.2f} - ALUNO APROVADO!\033[m :smiley:', use_aliases = True))  
        elif NF >= 7 and NF <= 7.24:
            print(f'\033[1;33mNOTA FINAL :\033[m {NF:.2f}')
            NF = 7.0
            print(emoji.emojize(f'\n\033[1;32mMÉDIA FINAL: {NF:.2f} - ALUNO APROVADO!\033[m :smiley:', use_aliases = True))  
        elif NF > 7.24 and NF <= 7.74:
            print(f'\033[1;33mNOTA FINAL :\033[m {NF:.2f}')
            NF = 7.5
            print(emoji.emojize(f'\n\033[1;32mMÉDIA FINAL: {NF:.2f} - ALUNO APROVADO!\033[m :smiley:', use_aliases = True))  
        elif NF > 7.74 and NF < 8:
            print(f'\033[1;33mNOTA FINAL :\033[m {NF:.2f}')
            NF = 8.0
            print(emoji.emojize(f'\n\033[1;32mMÉDIA FINAL: {NF:.2f} - ALUNO APROVADO!\033[m :smiley:', use_aliases = True))  
        elif NF >= 8 and NF <= 8.24:
            print(f'\033[1;33mNOTA FINAL :\033[m {NF:.2f}')
            NF = 8.0
            print(emoji.emojize(f'\n\033[1;32mMÉDIA FINAL: {NF:.2f} - ALUNO APROVADO!\033[m :smiley:', use_aliases = True))  
        elif NF > 8.24 and NF <= 8.74:
            print(f'\033[1;33mNOTA FINAL :\033[m {NF:.2f}')
            NF = 8.5
            print(emoji.emojize(f'\n\033[1;32mMÉDIA FINAL: {NF:.2f} - ALUNO APROVADO!\033[m :smiley:', use_aliases = True))  
        elif NF > 8.74 and NF < 9:
            print(f'\033[1;33mNOTA FINAL :\033[m {NF:.2f}')
            NF = 9.0
            print(emoji.emojize(f'\n\033[1;32mMÉDIA FINAL: {NF:.2f} - ALUNO APROVADO!\033[m :smiley:', use_aliases = True))    
        elif NF >= 9 and NF <= 9.24:
            print(f'\033[1;33mNOTA FINAL :\033[m {NF:.2f}')
            NF = 9.0
            print(emoji.emojize(f'\n\033[1;32mMÉDIA FINAL: {NF:.2f} - ALUNO APROVADO!\033[m :smiley:', use_aliases = True))  
        elif NF > 9.24 and NF <= 9.74:
            print(f'\033[1;33mNOTA FINAL :\033[m {NF:.2f}')
            NF = 9.5
            print(emoji.emojize(f'\n\033[1;32mMÉDIA FINAL: {NF:.2f} - ALUNO APROVADO!\033[m :smiley:', use_aliases = True))  
        elif NF > 9.74 and NF < 10:
            print(f'\033[1;33mNOTA FINAL :\033[m {NF:.2f}')
            NF = 10.0
            print(emoji.emojize(f'\n\033[1;32mMÉDIA FINAL: {NF:.2f} - ALUNO APROVADO!\033[m :smiley:', use_aliases = True))  
        elif NF == 10:
            print(f'\033[1;33mNOTA FINAL :\033[m {NF:.2f}')
            NF = 10.0
            print(emoji.emojize(f'\n\033[1;32mMÉDIA FINAL: {NF:.2f} - ALUNO APROVADO!\033[m :smiley:', use_aliases = True))

        add_medias(f'{aluno+1:<2}|  {NF:<11}|{situacao:>10}\n')

    option = main()

    if option == 1:
        print('\033[1;33m[ 1 ] - FECHAR MAIS MÉDIAS.\033[m')
        continue
    elif option == 2:
        print('\033[1;33m[ 2 ] - DAR UMA OLHADA NAS MÉDIAS JA FEITAS.\033[m')
        print(emoji.emojize(f'\n\033[1;32mAGUARDE SÓ UM POUQINHO, APROVEITE PARA BEBER UM POUCO DE ÁGUA...:tropical_drink:', use_aliases = True))
        sleep(4)
        open_arquivo()
        main()
    elif option == 3:
        print('\033[1;33m[ 3 ] - APAGAR TODOS OS DADOS DO ARQUIVO.\033[m')
        print(emoji.emojize(f'\n\033[1;32mAGUARDE SÓ UM POUQINHO, APROVEITE PARA BEBER UM POUCO DE ÁGUA...:tropical_drink:', use_aliases = True))
        sleep(4)
        reset()
        continue
    elif option == 4:
        print(emoji.emojize(f'\033[1;32m{f"ATÉ MAIS, PROFESSOR(A) {name.upper()}. OBRIGADO POR UTILIZAR! :wave:": ^80}\033[m', use_aliases = True))
        print('-'*70)
        break
    while True:
        if option > 4 or option < 0:
            print(emoji.emojize('\n\033[1;31mPOR FAVOR,ESCOLHA UMA OPÇÃO VÁLIDA!\033[m:no_entry_sign:', use_aliases = True))
            main()    
