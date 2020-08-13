def prova(msg):
    while True:
        try:
            prova1 = float(input(msg))
        except ValueError:
            print('\nPOR FAVOR,UTILIZE APENAS NÚMEROS COM PONTO!')
        else:
            return prova1

def teste(msg):
    while True:
        try:
            teste1 = float(input(msg))
        except ValueError:
            print('\nPOR FAVOR,UTILIZE APENAS NÚMEROS COM PONTO!')
        else:
            return teste1

def at1(msg):
    while True:
        try:
             at11 = float(input(msg))
        except ValueError:
            print('\nPOR FAVOR,UTILIZE APENAS NÚMEROS COM PONTO!')
        else:
            return at11

def at2(msg):
    while True:
        try:
             at22 = float(input(msg))
        except ValueError:
            print('\nPOR FAVOR,UTILIZE APENAS NÚMEROS COM PONTO!')
        else:
            return at22

def at3(msg):
    while True:
        try:
             at33 = float(input(msg))
        except ValueError:
            print('\nPOR FAVOR,UTILIZE APENAS NÚMEROS COM PONTO!')
        else:
            return at33

print(f'\n{" -> PRODUZIDO POR: VICTOR ALVES DE OLIVEIRA - 2020 <- ": ^70}\n')
print(f'\n{" INSTITUTO IEDA PICON ":=^70}\n')

while True:
    print(f'\n{" NÃO USE VÍRGULAS! USE APENAS PONTO(.)! EX: 3.75 ":=^70}\n')
    print(f'\n{" FECHAMENTO DA MÉDIA ": ^70}\n')
    print('-'*70)
    
    n1 = prova('\nNOTA DA PROVA(6.0): ')
    n2 = teste('\nNOTA DO TESTE(1.0): ')
    n3 = at1('\nNOTA DA ATIVIDADE 1(1.0): ')
    n4 = at2('\nNOTA DA ATIVIDADE 2(1.0): ')
    n5 = at3('\nNOTA DA ATIVIDADE 3(1.0): ')

    NF = n1 + n2 + n3 + n4 + n5

    if NF >= 0 and NF <= 0.24:
        print(f'NOTA FINAL : {NF:.2f}')
        NF = 0.0
        print(f'\nALUNO REPROVADO! - NOTA :{NF}')
    elif NF > 0.24 and NF <= 0.74:
        print(f'NOTA FINAL : {NF:.2f}')
        NF = 0.5
        print(f'\nALUNO REPROVADO! - NOTA :{NF}')
    elif NF > 0.74 and NF < 1:
        print(f'NOTA FINAL : {NF:.2f}')
        NF = 1.0
        print(f'\nALUNO REPROVADO! - NOTA :{NF}')  
    elif NF >= 1 and NF <= 1.24:
        print(f'NOTA FINAL : {NF:.2f}')
        NF = 1.0
        print(f'\nALUNO REPROVADO! - NOTA :{NF}')
    elif NF > 1.24 and NF <= 1.74:
        print(f'NOTA FINAL : {NF:.2f}')
        NF = 1.5
        print(f'\nALUNO REPROVADO! - NOTA :{NF}')
    elif NF > 1.74 and NF < 2:
        print(f'NOTA FINAL : {NF:.2f}')
        NF = 2.0
        print(f'\nALUNO REPROVADO! - NOTA :{NF}')   
    elif NF >= 2 and NF <= 2.24:
        print(f'NOTA FINAL : {NF:.2f}')
        NF = 2.0
        print(f'\nALUNO REPROVADO! - NOTA :{NF}')
    elif NF > 2.24 and NF <= 2.74:
        print(f'NOTA FINAL : {NF}')
        NF = 2.5
        print(f'\nALUNO REPROVADO! - NOTA :{NF}')
    elif NF > 2.74 and NF < 3:
        print(f'NOTA FINAL : {NF:.2f}')
        NF = 3.0
        print(f'\nALUNO REPROVADO! - NOTA :{NF}') 
    elif NF >= 3 and NF <= 3.24:
        print(f'NOTA FINAL : {NF:.2f}')
        NF = 3.0
        print(f'\nALUNO REPROVADO! - NOTA :{NF}')
    elif NF > 3.24 and NF <= 3.74:
        print(f'NOTA FINAL : {NF:.2f}')
        NF = 3.5
        print(f'\nALUNO REPROVADO! - NOTA :{NF}')
    elif NF > 3.74 and NF < 4:
        print(f'NOTA FINAL : {NF:.2f}')
        NF = 4.0
        print(f'\nALUNO REPROVADO! - NOTA :{NF}')
    elif NF >= 4 and NF <= 4.24:
        print(f'NOTA FINAL : {NF:.2f}')
        NF = 4.0
        print(f'\nALUNO REPROVADO! - NOTA :{NF}')
    elif NF > 4.24 and NF <= 4.74:
        print(f'NOTA FINAL : {NF:.2f}')
        NF = 4.5
        print(f'\nALUNO REPROVADO! - NOTA :{NF}')
    elif NF > 4.74 and NF < 5:
        print(f'NOTA FINAL : {NF:.2f}')
        NF = 5.0
        print(f'\nALUNO REPROVADO! - NOTA :{NF}')
    elif NF >= 5 and NF <= 5.24:
        print(f'NOTA FINAL : {NF:.2f}')
        NF = 5.0
        print(f'\nALUNO REPROVADO! - NOTA :{NF}')
    elif NF > 5.24 and NF <= 5.74:
        print(f'NOTA FINAL : {NF:.2f}')
        NF = 5.5
        print(f'\nALUNO REPROVADO! - NOTA :{NF}')
    elif NF > 5.74 and NF < 6:
        print(f'NOTA FINAL : {NF:.2f}')
        NF = 6.0
        print(f'\nALUNO REPROVADO! - NOTA :{NF}')
    elif NF >= 6 and NF <= 6.24:
        print(f'NOTA FINAL : {NF:.2f}')
        NF = 6.0
        print(f'\nALUNO REPROVADO! - NOTA :{NF}')
    elif NF > 6.24 and NF <= 6.74:
        print(f'NOTA FINAL : {NF:.2f}')
        NF = 6.5
        print(f'\nALUNO REPROVADO! - NOTA :{NF}')
    elif NF > 6.74 and NF < 7:
        print(f'NOTA FINAL : {NF:.2f}')
        NF = 7.0
        print(f'\nALUNO APROVADO! - NOTA :{NF}')   
    elif NF >= 7 and NF <= 7.24:
        print(f'NOTA FINAL : {NF:.2f}')
        NF = 7.0
        print(f'\nALUNO APROVADO! - NOTA :{NF}')
    elif NF > 7.24 and NF <= 7.74:
        print(f'NOTA FINAL : {NF:.2f}')
        NF = 7.5
        print(f'\nALUNO APROVADO! - NOTA :{NF}')
    elif NF > 7.74 and NF < 8:
        print(f'NOTA FINAL : {NF:.2f}')
        NF = 8.0
        print(f'\nALUNO APROVADO! - NOTA :{NF}') 
    elif NF >= 8 and NF <= 8.24:
        print(f'NOTA FINAL : {NF:.2f}')
        NF = 8.0
        print(f'\nALUNO APROVADO! - NOTA :{NF}')
    elif NF > 8.24 and NF <= 8.74:
        print(f'NOTA FINAL : {NF:.2f}')
        NF = 8.5
        print(f'\nALUNO APROVADO! - NOTA :{NF}')
    elif NF > 8.74 and NF < 9:
        print(f'NOTA FINAL : {NF:.2f}')
        NF = 9.0
        print(f'\nALUNO APROVADO! - NOTA :{NF}')   
    elif NF >= 9 and NF <= 9.24:
        print(f'NOTA FINAL : {NF:.2f}')
        NF = 9.0
        print(f'\nALUNO APROVADO! - NOTA :{NF}')
    elif NF > 9.24 and NF <= 9.74:
        print(f'NOTA FINAL : {NF:.2f}')
        NF = 9.5
        print(f'\nALUNO APROVADO! - NOTA :{NF}')
    elif NF > 9.74 and NF < 10:
        print(f'NOTA FINAL : {NF:.2f}')
        NF = 10.0
        print(f'\nALUNO APROVADO! - NOTA :{NF}')
    elif NF == 10:
        print(f'NOTA FINAL : {NF:.2f}')
        NF = 10.0
        print(f'\nALUNO APROVADO! - NOTA :{NF}')
    else:
        print(f'NOTA FINAL : {NF:.2f}')
        print(f'\nOPPS! REVISE AS NOTAS!!')
        
    

