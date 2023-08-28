from time import sleep
from random import randint, choice
# Dicionário de cores:
c = {'pr':'\033[0;1;30m', 'vm':'\033[0;1;31m', 'vd':'\033[0;1;32m', 'ama':'\033[0;1;33m', 'az':'\033[0;1;34m', 'rox':'\033[0;1;35m',
    'n':'\033[m', 'neg':'\033[0;1m', 'sub':'\033[4m', 'neg/sub':'\033[1;4m'}

j_confirmacao_atributos=''
while j_confirmacao_atributos!='1':
    j_confirmacao_atributos=''
    j_atributos=1
    print('Distribua 15 pontos entre os seguintes atributos: AGILIDADE, ATAQUE, LUTA, SABEDORIA e VITALIDADE.')
    print('Você pode colocar até 10 pontos em um único atributo.')
    print('("Distribua" -1 no primeiro atributo para que seus pontos sejam igualmente distribuídos, ou seja, 3 pontos para cada atributo)')
    while (j_atributos!=0) or (0>j_agi or 0>j_des or 0>j_lut or 0>j_sab or 0>j_vit) or (j_agi>10 or j_des>10 or j_lut>10 or j_sab>10 or j_vit>10):
        j_atributos=15
        j_agi=int(input('AGILIDADE: '))
        if j_agi==-3 or j_agi==-2:
            i_personalizacao_atributos=1
            print(f'{c["neg"]}PERSONALIZAÇÃO DOS ATRIBUTOS DO INIMIGO ATIVADA{c["n"]}')
            sleep(1)
        else:
            i_personalizacao_atributos=0
        if j_agi==-1 or j_agi==-3:
            j_agi=j_des=j_lut=j_sab=j_vit=3
            break
        if j_agi==-2:
            j_agi=int(input('AGILIDADE: '))
        j_atributos -= j_agi
        print(f'Pontos restantes: {j_atributos}')
        j_des = int(input('DESTRUIÇÃO: '))
        j_atributos -= j_des
        print(f'Pontos restantes: {j_atributos}')
        j_lut = int(input('LUTA: '))
        j_atributos -= j_lut
        print(f'Pontos restantes: {j_atributos}')
        j_sab = int(input('SABEDORIA: '))
        j_atributos -= j_sab
        print(f'Pontos restantes: {j_atributos}')
        j_vit = int(input('VITALIDADE: '))
        j_atributos -= j_vit
        print(f'Pontos restantes: {j_atributos}')
        if j_atributos != 0:
            print(f'{c["vm"]}Os pontos foram distribuídos incorretamente. Você ficou com {c["neg"]}{j_atributos}{c["vm"]} ponto(s) para distribuir.{c["n"]}')
        elif j_agi>10 or j_des>10 or j_lut>10 or j_sab>10 or j_vit>10:
            print(f'{c["vm"]}Algum dos seus atributos ficou com mais do que 10 pontos. Por favor distribua os pontos novamente.{c["n"]}')
        elif 0>j_agi or 0>j_des or 0>j_lut or 0>j_sab or 0>j_vit:
            print(f'{c["vm"]}Nenhum dos seus atributos deve ficar com menos de 0 pontos. Por favor distribua os pontos novamente.{c["n"]}')
    j_vida_max = j_vida_atual = 100 + 20 * j_vit
    j_chance_acerto_base = j_chance_acerto_atual  = 50 + 10 * j_lut
    j_chance_esquiva_base = j_chance_esquiva_atual = 30 + 6 * j_agi
    j_num_habs_melhorias = 2 + j_sab
    if j_sab < 5:
        j_hab1_dano_base = j_hab1_dano_atual = 10 + (2 * j_des)
    elif j_sab >= 5:
        j_hab1_dano_base = j_hab1_dano_atual = 15 + (3 * j_des)
    print(f'''{'SEUS STATUS':-^50}
P. vida máxima: {j_vida_max}
P. dano por ataque base (Corte): {j_hab1_dano_base}
P. chance de acerto: {j_chance_acerto_base}
P. chance de esquiva: {j_chance_esquiva_base}
Nº habilidades melhoradas e/ou desbloqueadas: {j_num_habs_melhorias}
''')
    while '1'!=j_confirmacao_atributos!='2':
        j_confirmacao_atributos = input('Você [1] deseja manter seus atributos como estão ou [2] deseja reajustá-los? R: ')

if j_num_habs_melhorias > 6:
    j_num_habs = j_num_habs_melhorias - 6
else:
    j_num_habs = j_num_habs_melhorias

j_hab2_duracao_atual = j_hab2_duracao_base = 2 + j_sab // 6 * 1
j_hab2_chance_esquiva_extra = 0 + j_sab // 6 * 20
j_hab3_num_golpes = 3 + j_sab // 7 * 1
j_hab3_chance_acerto_perdida = 25 - j_sab // 7 * 13
j_hab4_duracao_atual = j_hab4_duracao_base = 2 + j_sab // 8 * 1
j_hab4_aumento_dano_da_hab1 = (8 + j_sab // 8 * 4) + (j_des * (1 + (j_sab // 8 * 1)))
j_hab5_ganho_resistencia = 6 + j_sab // 9 * 4
j_hab5_cura = 10 + j_sab // 9 * 6
j_hab5_duracao_minima = 1 + j_sab // 9 * 1
j_hab5_duracao_maxima = j_hab5_duracao_atual = j_hab5_duracao_base = 4 + j_sab // 9 * 2
j_hab6_dano = (50 + j_sab // 10 * 30) + (j_des * (10 + (j_sab // 10 * 6)))
j_hab6_duracao_atual = j_hab6_duracao_base = 2 + j_sab // 10 * 1
j_hab6_diminuicao_resistencia = 10 + j_sab // 10 * 4

j_hab2_cooldown_base = 6
j_hab3_cooldown_base = 3
j_hab4_cooldown_base = 5
j_hab5_cooldown_base = 6
j_hab6_cooldown = 1
j_hab5_cooldown_atual = j_hab4_cooldown_atual = j_hab3_cooldown_atual = j_hab2_cooldown_atual = 0

i_confirmacao_atributos=''
i_atributos=1
while i_personalizacao_atributos==1 and i_confirmacao_atributos!='1':
    print(f'{c["neg"]}Agora distribua os os pontos dos atributos do inimigo:{c["n"]}')
    while (i_atributos!=0) or (0>i_agi or 0>i_des or 0>i_lut or 0>i_sab or 0>i_vit) or (i_agi>10 or i_des>10 or i_lut>10 or i_sab>10 or i_vit>10):
        i_atributos=15
        i_agi=int(input('AGILIDADE: '))
        if i_agi==-1:
            i_agi=i_des=i_lut=i_sab=i_vit=3
            break
        i_atributos-=i_agi
        print(f'Pontos restantes: {i_atributos}')
        i_des=int(input('DESTRUIÇÃO: '))
        i_atributos-=i_des
        print(f'Pontos restantes: {i_atributos}')
        i_lut=int(input('LUTA: '))
        i_atributos-=i_lut
        print(f'Pontos restantes: {i_atributos}')
        i_sab=int(input('SABEDORIA: '))
        i_atributos-=i_sab
        print(f'Pontos restantes: {i_atributos}')
        i_vit=int(input('VITALIDADE: '))
        i_atributos-=i_vit
        print(f'Pontos restantes: {i_atributos}')
        if i_atributos!=0:
            print(f'{c["vm"]}Os pontos foram distribuídos incorretamente. Você ficou com {c["neg"]}{i_atributos}{c["vm"]} ponto(s) para distribuir.{c["n"]}')
        elif i_agi>10 or i_des>10 or i_lut>10 or i_sab>10 or i_vit>10:
            print(f'{c["vm"]}Algum dos atributos do inimigo ficou com mais do que 10 pontos. Por favor distribua os pontos novamente.{c["n"]}')
        elif 0>j_agi or 0>j_des or 0>j_lut or 0>j_sab or 0>j_vit:
            print(f'{c["vm"]}Nenhum dos atributos do inimigo deve ficar com menos de 0 pontos. Por favor distribua os pontos novamente.{c["n"]}')
    i_vida_max = i_vida_atual = 150 + 30 * i_vit
    i_chance_acerto_base = i_chance_acerto_atual = 40 + 8 * i_lut
    i_chance_esquiva_base = i_chance_esquiva_atual = 30 + 6 * i_agi
    i_num_habs_melhorias = 2 + i_sab
    if i_sab < 5:
        i_hab1_dano = 15 + 3 * i_des
    elif i_sab >= 5:
        i_hab1_dano = 20 + 4 * i_des
    print(f'''{'STATUS DO INIMIGO':-^45}
P. vida máxima: {i_vida_max}
P. dano por ataque base (Garra): {i_hab1_dano}
P. chance acerto: {i_chance_acerto_base}
P. chance esquiva: {i_chance_esquiva_base}
Nº habilidades melhoradas e/ou desbloqueadas: {i_num_habs_melhorias}
''')
    while '1'!=i_confirmacao_atributos!='2':
        i_confirmacao_atributos=input('Você [1] deseja manter os atributos do inimigo com estão ou [2] deseja reajustá-los? R: ')
if i_personalizacao_atributos!=1:
    while i_atributos!=0 or i_agi>10 or i_des>10 or i_lut>10 or i_sab>10 or i_vit>10:
        i_atributos = 15
        i_agi = randint(0, i_atributos//2)
        i_atributos -= i_agi
        i_des = randint(0, i_atributos//2)
        i_atributos -= i_des
        i_lut = randint(0, i_atributos//2)
        i_atributos -= i_lut
        i_sab = randint(0, i_atributos//2)
        i_atributos -= i_sab
        i_vit = randint(0, i_atributos//2)
        i_atributos -= i_vit
        i_novo_vit = randint(0, i_atributos)
        i_atributos -= i_novo_vit
        i_novo_sab = randint(0, i_atributos)
        i_atributos -= i_novo_sab
        i_novo_lut = randint(0, i_atributos)
        i_atributos -= i_novo_lut
        i_novo_des = randint(0, i_atributos)
        i_atributos -= i_novo_des
        i_novo_agi = randint(0, i_atributos)
        i_atributos -= i_novo_agi
        i_agi+=i_novo_agi
        i_des+=i_novo_des
        i_lut+=i_novo_lut
        i_sab+=i_novo_sab
        i_vit+=i_novo_vit
    # i_agi = i_des = i_lut = i_vit = 2
    # i_sab = 4
    i_vida_max = i_vida_atual = 150 + 30 * i_vit
    i_chance_acerto_base = i_chance_acerto_atual = 40 + 8 * i_lut
    i_chance_esquiva_base = i_chance_esquiva_atual = 30 + 6 * i_agi
    i_num_habs_melhorias = 2 + i_sab
    if i_sab < 5:
        i_hab1_dano = 15 + 3 * i_des
    elif i_sab >= 5:
        i_hab1_dano = 20 + 4 * i_des

i_hab2_perca_chance_esquiva = 15 - i_sab // 6 * 5
i_hab2_dano = (8 + i_sab // 6 * 6) + (i_des * (2 + i_sab // 6 * 1))
i_hab2_duracao_base=i_hab2_duracao_atual = 2 + i_sab // 6 * 1
i_hab3_dano = (20 + i_sab // 7 * 10) + (i_des * (4 + i_sab // 7 * 2))
i_hab3_dano_por_turno = (5 + i_sab // 7 * 1) + (i_des * (1 + i_sab // 7 * 1))
i_hab3_chance_acerto_extra = 20 + i_sab // 7 * 15
i_hab3_duracao_base=i_hab3_duracao_atual = 3 + i_sab // 7 * 999# Bem alta mesmo
i_hab4_diminuicao_chance_acerto = 15 + i_sab // 8 * 10
i_hab4_duracao_base=i_hab4_duracao_atual = 3 + i_sab // 8 * 1
i_hab4_chance_atordoamento = 20 + i_sab // 8 * 15
i_hab5_cura = 40 + i_sab // 9 * 30
i_hab5_imune_a_danos = 2
i_hab6_margem_min_dano = (1 + i_sab // 10 * 9) + (i_des * (1 + i_sab // 10 * 2))
i_hab6_margem_max_dano = (50 + i_sab // 10 * 50) + (i_des * (10 + i_sab // 10 * 10))

i_hab3_cooldown_base = 3
i_hab4_cooldown_base=i_hab6_cooldown_base = 5
i_hab5_cooldown = 1
i_hab2_cooldown_atual=i_hab3_cooldown_atual=i_hab4_cooldown_atual=i_hab6_cooldown_atual= 0

print(f'{c["neg"]}A luta está prestes a começar...')
sleep(2)
print(f'{c["n"]}')
j_resistencia = 0
j_atordoado = 2
i_resistência = 0
i_atordoado = j_hab6_duracao_base+1
turno = 0
j_morrendo = i_morrendo = "vivo"
while True:
    i_vida_max = i_vida_atual
    i_teste_acerto = -1
    turno += 1
    print(f'{c["neg"]+f"Turno {turno}":-^50}{c["n"]}')
    sleep(1)


    if j_hab2_duracao_atual >= j_hab2_duracao_base:
        j_chance_esquiva_atual = j_chance_esquiva_base
    if j_hab4_duracao_atual >= j_hab4_duracao_base:
        j_hab1_dano_atual = j_hab1_dano_base
    if j_hab5_duracao_atual < j_hab5_duracao_base:
        j_vida_atual += j_hab5_cura
        print(f'{c["ama"]}Sua vida foi curada em {c["sub"]+str(j_hab5_cura)+c["ama"]} pontos.{c["n"]}')
        sleep(2)
        if i_hab3_duracao_atual < i_hab3_duracao_base:
            print(f'{c["vd"]}O {c["ama"]+"ÁCIDO"+c["vd"]} na sua pele desaparece, aliviando parte de sua dor.{c["n"]}')
            i_hab3_duracao_atual = i_hab3_duracao_base
            sleep(2)
    else:
        j_resistencia = 0
    if j_hab6_duracao_atual < 2 + j_sab // 10 * 1:
        j_hab6_duracao_atual += 1
    else:
        i_resistência = 0

    j_hab4_duracao_atual += 1
    j_hab5_duracao_atual += 1

    if j_hab2_cooldown_atual > 0:
        j_hab2_cooldown_atual -= 1
    if j_hab3_cooldown_atual > 0:
        j_hab3_cooldown_atual -= 1
    if j_hab4_cooldown_atual > 0:
        j_hab4_cooldown_atual -= 1
    if j_hab5_cooldown_atual > 0:
        j_hab5_cooldown_atual -= 1

    
    if i_hab3_duracao_atual < i_hab3_duracao_base:
        j_vida_atual -= i_hab3_dano_por_turno-j_resistencia
        print(f'{c["ama"]}O ÁCIDO na sua pele queima como fogo, te causando {i_hab3_dano_por_turno-j_resistencia} pontos de dano.{c["n"]}')
        sleep(2)
        if j_vida_atual<=0 and j_morrendo=="vivo":
            print(f'Você sente suas forças se esvaindo, sua mente se desconectando. Você está morrendo. Porém, você não pode desistir. {c["neg"]}Dê seu último suspiro.{c["n"]}')# frase_epica(2).exe
            j_morrendo="morto_por_acido"
            j_hab2_cooldown_atual=j_hab3_cooldown_atual=j_hab4_cooldown_atual=j_hab5_cooldown_atual=j_hab6_duracao_atual=0
            sleep(4)
    

    j_acoes = '[0] Guardar\n'
    if j_num_habs_melhorias >= 7:
        j_acoes += f'[1] {c["az"]}Corte{c["n"]}\n'
    else:
        j_acoes += f'[1] {c["n"]}Corte\n{c["n"]}'
    if j_num_habs_melhorias >= 8 and j_hab2_cooldown_atual == 0:
        j_acoes += f'[2] {c["vd"]}Segunda Chance{c["n"]}\n'
    elif j_num_habs_melhorias >= 8 and j_hab2_cooldown_atual > 0:
        j_acoes += f'[2] {c["neg/sub"]}Segunda Chance{c["n"]} ({j_hab2_cooldown_atual})\n'
    elif j_hab2_cooldown_atual > 0:
        j_acoes += f'[2] {c["neg"]}Segunda Chance{c["n"]} ({j_hab2_cooldown_atual})\n'
    else:
        j_acoes += '[2] Segunda Chance\n'
    if j_num_habs_melhorias >= 9 and j_hab3_cooldown_atual == 0:
        j_acoes += f'[3] {c["pr"]}Cortes Rápidos{c["n"]}\n'
    elif j_num_habs_melhorias >= 9 and j_hab3_cooldown_atual > 0:
        j_acoes += f'[3] {c["neg/sub"]}Cortes Rápidos{c["n"]} ({j_hab3_cooldown_atual})\n'
    elif j_num_habs_melhorias >= 3 and j_hab3_cooldown_atual > 0:
        j_acoes += f'[3] {c["neg"]}Cortes Rápidos{c["n"]} ({j_hab3_cooldown_atual})\n'
    elif j_num_habs_melhorias >= 3:
        j_acoes += '[3] Cortes Rápidos\n'
    if j_num_habs_melhorias >= 10 and j_hab4_cooldown_atual == 0:
        j_acoes += f'[4] {c["vm"]}Raiva{c["n"]}\n'
    elif j_num_habs_melhorias >= 10 and j_hab4_cooldown_atual > 0:
        j_acoes += f'[4] {c["neg/sub"]}Raiva{c["n"]} ({j_hab4_cooldown_atual})\n'
    elif j_num_habs_melhorias >= 4 and j_hab4_cooldown_atual > 0:
        j_acoes += f'[4] {c["neg"]}Raiva{c["n"]} ({j_hab4_cooldown_atual})\n'
    elif j_num_habs_melhorias >= 4:
        j_acoes += '[4] Raiva\n'
    if j_num_habs_melhorias >= 11 and j_hab5_cooldown_atual == 0:
        j_acoes += f'[5] {c["ama"]}Descanso{c["n"]}\n'
    elif j_num_habs_melhorias >= 11 and j_hab5_cooldown_atual > 0:
        j_acoes += f'[5] {c["neg/sub"]}Descanso{c["n"]} ({j_hab5_cooldown_atual})\n'
    elif j_num_habs_melhorias >= 5 and j_hab5_cooldown_atual > 0:
        j_acoes += f'[5] {c["neg"]}Descanso{c["n"]} ({j_hab5_cooldown_atual})\n'
    elif j_num_habs_melhorias >= 5:
        j_acoes += '[5] Descanso\n'
    if j_num_habs_melhorias >= 12 and j_hab6_cooldown == 1:
        j_acoes += f'[6] {c["rox"]}Destruição{c["n"]}\n'
    elif j_num_habs_melhorias >= 12 and j_hab6_cooldown == 0:
        j_acoes += f'[6] {c["neg/sub"]}Destruição{c["n"]}\n'
    elif j_num_habs_melhorias >= 6 and j_hab6_cooldown == 0:
        j_acoes += f'[6] {c["neg"]}Destruição{c["n"]}\n'
    elif j_num_habs_melhorias >= 6:
        j_acoes += '[6] Destruição\n'


    print(f'\n{c["neg"]}SUA VEZ{c["n"]}')
    sleep(1)
    
    if j_vida_atual > j_vida_max:
        j_vida_atual = j_vida_max

    if i_hab5_imune_a_danos == 1:
        print(f'{c["vd"]}A pele do inimigo parece ter voltado ao normal.{c["n"]}')
        sleep(2)
    
   
    if j_atordoado == 0:
        print(f'{c["vm"]}POR ENQUANTO, VOCÊ NÃO CONSEGUE FAZER NADA{c["n"]}')
        sleep(2)
    elif j_atordoado == 1:
        print(f'{c["vd"]}VOCÊ CONSEGUE AGIR AGORA!{c["n"]}')
        sleep(2)

    j_escolha = -1
    print('')
    print(f'{c["vd"]}HP: {j_vida_atual}/{j_vida_max}{c["n"]}')
    if j_atordoado >= 1:
        print(j_acoes)
        while True:
            j_escolha = input('''Escolha a habilidade que quer usar: ''')
            if j_escolha.isalpha() or int(j_escolha) < 0 or int(j_escolha) > j_num_habs_melhorias or (j_escolha=='2' and j_hab2_cooldown_atual>0) or (j_escolha=='3' and j_hab3_cooldown_atual>0) or (j_escolha=='4' and j_hab4_cooldown_atual>0) or (j_escolha=='5' and j_hab5_cooldown_atual>0) or (j_escolha=='6' and j_hab6_cooldown == 0):
                print(f'{c["vm"]}Escolha uma opção válida!{c["n"]}')
            else:
                break
        
        
        if int(j_escolha) == 0:
            print('+15 pontos de chance esquiva por 1 turno!')
            j_chance_esquiva_atual += 15
            sleep(2)
        else:
            j_chance_esquiva_atual = j_chance_esquiva_base

        if int(j_escolha) == 1:
            if randint(1, j_chance_acerto_atual) >= randint(1, i_chance_esquiva_atual) or j_hab6_duracao_atual < 2 + j_sab // 10 * 1:
                if i_hab5_imune_a_danos > 0:
                    i_vida_atual -= j_hab1_dano_atual - i_resistência
                    print(f'{c["az"]}Você acertou um CORTE no inimigo, causando {c["sub"]+str(j_hab1_dano_atual-i_resistência)+c["az"]} pontos de dano.{c["n"]}')
                elif i_hab5_imune_a_danos == 0:
                    print(f'{c["vm"]}Você acerta um {c["az"]+"CORTE"+c["vm"]} no inimigo, mas seu ataque não fez nenhum estrago nele.{c["n"]}')
            else:
                print(f'{c["vm"]}Você golpeia o inimigo com um {c["az"]+"CORTE"+c["vm"]}, mas ele consegue esquivar!{c["n"]}')
            sleep(2)
            
        elif int(j_escolha) == 2:
            print(f'{c["vd"]}Você ganha uma ESQUIVA EXTRA para os próximos {c["sub"]+str(j_hab2_duracao_base)+c["vd"]} golpes que receber!{c["n"]}')
            sleep(2)
            if j_hab2_chance_esquiva_extra > 0:
                print(f'{c["vd"]+c["sub"]+"+20"+c["vd"]} pontos de chance de esquiva pela mesma duração!{c["n"]}')
                sleep(2)
            j_hab2_cooldown_atual = j_hab2_cooldown_base
            j_hab2_duracao_atual = 0
            
        elif int(j_escolha) == 3:
            j_hab3_cooldown_atual = j_hab3_cooldown_base
            j_hab3_num_acertos = 0
            for _ in range(j_hab3_num_golpes):
                if randint(1,j_chance_acerto_atual-j_hab3_chance_acerto_perdida)>=randint(1,i_chance_esquiva_atual):
                    j_hab3_num_acertos+=1
                    i_vida_atual -= j_hab1_dano_atual-i_resistência
            if i_hab5_imune_a_danos>0<j_hab3_num_acertos:
                print(f'{c["pr"]}Você acertou {c["sub"]+str(j_hab3_num_acertos)+c["pr"]} de {c["sub"]+str(j_hab3_num_golpes)+c["pr"]} CORTES, causando {c["sub"]+str((j_hab1_dano_atual-i_resistência)*j_hab3_num_acertos)+c["pr"]} pontos de dano!{c["n"]}')
            elif j_hab3_num_acertos==0:
                print(f'{c["vm"]}O inimigo conseguiu esquivar de todos os CORTES!{c["n"]}')
            elif i_hab5_imune_a_danos==0:
                print(f'{c["vm"]}Você acertou {c["sub"]+str(j_hab3_num_acertos)+c["vm"]} de {c["sub"]+str(j_hab3_num_golpes)+c["vm"]} CORTES, porém nenhum deles surtiu efeito contra o alvo!{c["n"]}')
            sleep(2)

        elif int(j_escolha) == 4:
            print(f'{c["vm"]}Sua habilidade "{j_acoes.split()[3]+c["vm"]}" causará mais dano por {c["sub"]+str(j_hab4_duracao_base)+c["vm"]} turnos!')
            sleep(2)
            j_hab4_cooldown_atual = j_hab4_cooldown_base
            j_hab4_duracao_atual = 0
            j_hab1_dano_atual += j_hab4_aumento_dano_da_hab1

        elif int(j_escolha) == 5:
            j_hab5_duracao_base = randint(j_hab5_duracao_minima, j_hab5_duracao_maxima)
            print(f'{c["ama"]}Durante {c["sub"]+str(j_hab5_duracao_base)+c["ama"]} turnos, você receberá {c["sub"]+str(j_hab5_ganho_resistencia)+c["ama"]} pontos de dano a menos e sua vida será curada em {c["sub"]+str(j_hab5_cura)+c["ama"]} pontos por turno.{c["n"]}')
            sleep(3)
            j_hab5_cooldown_atual = j_hab5_cooldown_base
            j_hab5_duracao_atual = 0
            j_resistencia += j_hab5_ganho_resistencia

        elif int(j_escolha) == 6:
            j_hab6_cooldown = 0
            if i_hab5_imune_a_danos > 0:
                print(f'{c["rox"]}Você, bem, DESTRÓI o inimigo, que recebe {c["sub"]+str(j_hab6_dano)+c["rox"]} pontos de dano.{c["n"]}')
            elif i_hab5_imune_a_danos == 0:
                print(f'{c["vm"]}Você tenta DESTRUIR o inimigo, porém isso não parece ter surtido nenhum efeito nele!{c["n"]}')
            sleep(2)
            print(f'{c["rox"]}Além disso, pelos próximos {c["sub"]+str(j_hab6_duracao_base)+c["rox"]} turnos, o inimigo está atordoado e recebe {c["sub"]+str(j_hab6_diminuicao_resistencia)+c["rox"]} pontos a mais de dano.{c["n"]}')
            sleep(2)
            j_hab6_duracao_atual = 0
            i_atordoado = 0
            i_vida_atual -= j_hab6_dano - i_resistência
            i_resistência -= j_hab6_diminuicao_resistencia



    if i_hab2_duracao_atual < i_hab2_duracao_base and i_vida_atual != i_vida_max:
        j_vida_atual -= i_hab2_dano-j_resistencia
        print(f'{c["az"]}Os ESPINHOS do inimigo te ferem, causando {c["sub"]+str(i_hab2_dano-j_resistencia)+c["az"]} pontos de dano.{c["n"]}')
        sleep(2)
        if j_vida_atual<=0 and j_morrendo=="vivo":
            print(f'Você sente suas forças se esvaindo, sua mente se desconectando. Você está morrendo. Porém, você não pode desistir. {c["neg"]}Dê seu último suspiro.{c["n"]}')# frase_epica(2).exe
            j_morrendo="morto_por_espinho"
            j_hab2_cooldown_atual=j_hab3_cooldown_atual=j_hab4_cooldown_atual=j_hab5_cooldown_atual=j_hab6_duracao_atual=0
            sleep(4)
    if i_hab2_duracao_atual >= i_hab2_duracao_base:
        i_chance_esquiva_atual = i_chance_esquiva_base


    if j_hab2_duracao_atual<j_hab2_duracao_base and j_escolha!=0:
        j_chance_esquiva_atual+=j_hab2_chance_esquiva_extra
    if j_hab4_duracao_atual==j_hab4_duracao_base:
        print(f'{c["vm"]}Sua RAIVA cessou. Por enquanto.{c["n"]}')
        sleep(1)
    if j_hab5_duracao_atual==j_hab5_duracao_base:
        print(f'{c["vm"]}Sua habilidade {c["ama"]+"DESCANSO"+c["vm"]} perdeu o efeito!')
        sleep(1)
    
    j_atordoado+=1


    if i_hab5_imune_a_danos < 2:
        i_hab5_imune_a_danos+=1

    if i_hab2_cooldown_atual > 0 and i_hab2_duracao_atual >= i_hab2_duracao_base:
        i_hab2_cooldown_atual-=1
    if i_hab3_cooldown_atual > 0:
        i_hab3_cooldown_atual-=1
    if i_hab4_cooldown_atual > 0:
        i_hab4_cooldown_atual-=1
    if i_hab6_cooldown_atual > 0:
        i_hab6_cooldown_atual-=1

    if i_vida_atual == i_vida_max:
        i_hab2_duracao_atual += 1
    i_hab3_duracao_atual += 1
    i_hab4_duracao_atual += 1

    if i_hab4_duracao_atual==i_hab4_duracao_base:
        print(f'{c["vd"]}Sua {c["rox"]+"CONFUSÃO"+c["vd"]} passa, ficando mais fácil acertar o inimigo.{c["n"]}')
        sleep(2)
        j_chance_acerto_atual = j_chance_acerto_base

    if i_vida_atual<=0 and i_morrendo=="vivo":
        i_morrendo="morto"
        if j_morrendo=='vivo':
            print(f'Depois de tudo isso, o inimigo está com uma aparência péssima. Ele está morrendo... {c["neg"]}Porém não vai desitir tão facilmente.{c["n"]}')# frase_epica.exe
            i_hab2_cooldown_atual=i_hab3_cooldown_atual=i_hab4_cooldown_atual=i_hab6_cooldown_atual=0
            sleep(4)
    
    if "morto_por_espinho"!=j_morrendo!="vivo" and i_morrendo=="vivo":
        print('')
        print(f'{c["neg"]}Acabou. Você fez tudo o que pôde, mas ainda não foi o suficiente. Você {c["vm"]}Morreu{c["n"]}.')
        sleep(2)
        break
    elif j_morrendo!="vivo"!=i_morrendo:
        print(f'{c["neg"]}Você pode até ter morrido, mas você não está sozinho nessa. Houve um {c["ama"]}empate{c["n"]}.')
        sleep(2)
        break
    if j_morrendo=="morto_por_espinho":
        j_morrendo='morto'

    print(f'\n{c["neg"]}VEZ DO INIMIGO{c["n"]}')
    print(f'HP: {c["vd"]+str(i_vida_atual)}/{str(i_vida_max)+c["n"]}')
    sleep(1)
    if i_vida_atual <= (150+30*i_vit)/2:
        print('O inimigo parece bem machucado...')
        sleep(2)


    i_acoes = '1 '
    if i_hab2_cooldown_atual == 0:
        i_acoes += '2 '
    if i_sab >= 1 and i_hab3_cooldown_atual == 0:
        i_acoes += '3 '
    if i_sab >= 2 and i_hab4_cooldown_atual == 0:
        i_acoes += '4 '
    if i_sab >= 3 and i_hab5_cooldown == 1 and i_vida_atual < 30:
        i_acoes += '5 '
    if i_sab >= 4 and i_hab6_cooldown_atual == 0 and j_vida_atual > i_hab6_margem_max_dano / 2:
        i_acoes += '6 '

    # i_escolha = choice(i_acoes.split())
    i_escolha = input('INIMIGO: ')
    print(i_acoes, i_escolha)
    if i_atordoado < j_hab6_duracao_base:
        print(f'{c["rox"]}POR ENQUANTO, O INIMIGO NÃO CONSEGUE AGIR!{c["n"]}')
        sleep(2)
    elif i_atordoado == j_hab6_duracao_base:
        print(f'{c["vm"]}O INIMIGO CONSEGUE AGIR AGORA!{c["n"]}')
        sleep(2)
    if i_atordoado >= j_hab6_duracao_base:
        if '5' in i_acoes and i_morrendo=="vivo":
            print(f'{c["vd"]}Para o seu espanto, uma parte do corpo do inimigo é RECONSTRUÍDA. Ele acabou de se recuperar de parte do estrago sofrido?{c["n"]}')
            i_vida_atual+=i_hab5_cura
            sleep(2)
            if i_sab>=9:
                print(f'{c["vd"]}Sua pele parece mais resistente do que antes...{c["n"]}')
                sleep(2)
                i_hab5_imune_a_danos=0
            i_hab5_cooldown=0

        elif i_escolha == '1':
            i_teste_acerto = randint(1,i_chance_acerto_atual) - randint(1,j_chance_esquiva_atual)# Se for menor que zero, o jogador esquiva, senão o inimigo acerta.
            i_teste_acerto_extra = randint(1,i_chance_acerto_atual) - randint(1,j_chance_esquiva_atual)# Caso acerte, mais uma chance para o jogador esquivar (efeito da habilidade 2 do jogador)
            if (i_teste_acerto>=0 and j_hab2_duracao_atual>=j_hab2_duracao_base) or (j_atordoado==1) or ((j_hab2_duracao_atual<j_hab2_duracao_base) and (i_teste_acerto>=0<=i_teste_acerto_extra)):
                print(f'{c["vm"]}O inimigo usa suas GARRAS para te atacar, causando {c["sub"]+str(i_hab1_dano-j_resistencia)+c["vm"]} pontos de dano.{c["n"]}')
                j_vida_atual-=i_hab1_dano-j_resistencia
            else:
                print(f'{c["vd"]}O inimigo usa suas {c["vm"]+"GARRAS"+c["vd"]} para te atacar, mas você consegue esquivar!{c["n"]}')
            sleep(2)
        
        elif i_escolha == '2':
            print(f'{c["az"]}ESPINHOS surgem na pele do inimigo. Atacá-lo agora será perigoso!{c["n"]}')
            sleep(2)
            i_chance_esquiva_atual-=i_hab2_perca_chance_esquiva
            i_hab2_duracao_atual=0
            i_hab2_cooldown_atual=i_hab2_duracao_base

        elif i_escolha == '3':
            i_teste_acerto = randint(1,i_chance_acerto_atual+i_hab3_chance_acerto_extra) - randint(1,j_chance_esquiva_atual)# Se for menor que zero, o jogador esquiva, senão o inimigo acerta.
            i_teste_acerto_extra = randint(1,i_chance_acerto_atual+i_hab3_chance_acerto_extra) - randint(1,j_chance_esquiva_atual)# Caso acerte, mais uma chance para o jogador esquivar (efeito da habilidade 2 do jogador)
            if ((i_teste_acerto>=0 and j_hab2_duracao_atual>=j_hab2_duracao_base) or (j_atordoado==1)) or ((j_hab2_duracao_atual<j_hab2_duracao_base) and (i_teste_acerto>=0<=i_teste_acerto_extra)):
                print(f'{c["ama"]}ÁCIDO é espirrado na sua direção, te acertando e causando {c["sub"]+str(i_hab3_dano-j_resistencia)+c["ama"]} pontos de dano.{c["n"]}')
                j_vida_atual -= i_hab3_dano-j_resistencia
                i_hab3_duracao_atual = 0
            else:
                print(f'{c["vd"]}ÁCIDO é espirrado na sua direção, mas você consegue esquivar.{c["n"]}')
            i_hab3_cooldown_atual = i_hab3_cooldown_base
            sleep(2)

        elif i_escolha == '4':
            print(f'{c["rox"]}O inimigo te CONFUNDE, fazendo com que você perca {c["sub"]+str(i_hab4_diminuicao_chance_acerto)+c["rox"]} pontos de chance de acerto.{c["n"]}')
            sleep(2)
            j_chance_acerto_atual -= i_hab4_diminuicao_chance_acerto
            i_hab4_cooldown_atual = i_hab4_cooldown_base
            i_hab4_duracao_atual = 0
            if randint(1, 100) <= i_hab4_chance_atordoamento:
                print(f'{c["rox"]}Você também é ATORDOADO, não podendo agir durante {c["sub"]+"1"+c["rox"]} turno!{c["n"]}')
                sleep(2)
                j_atordoado = 0

        elif i_escolha == '6':
            i_teste_acerto = randint(1,i_chance_acerto_atual)-randint(1,j_chance_esquiva_atual)# Se for menor que zero, o jogador esquiva, senão o inimigo acerta.
            i_teste_acerto_extra = randint(1,i_chance_acerto_atual)-randint(1,j_chance_esquiva_atual)# Caso acerte, mais uma chance para o jogador esquivar (efeito da habilidade 2 do jogador)
            if (i_teste_acerto>=0 and j_hab2_duracao_atual>=j_hab2_duracao_base) or (j_atordoado==1) or ((j_hab2_duracao_atual<j_hab2_duracao_base) and (i_teste_acerto>=0<=i_teste_acerto_extra)):
                i_hab6_dano_atual = randint(i_hab6_margem_min_dano, i_hab6_margem_max_dano)-j_resistencia
                print(f'{c["pr"]}CAOS toma conta de todo o seu ser. Você toma {c["sub"]+str(i_hab6_dano_atual)+c["pr"]} pontos de dano.{c["n"]}')
                j_vida_atual -= i_hab6_dano_atual
            else:
                i_hab6_dano_atual = int(randint(i_hab6_margem_min_dano, i_hab6_margem_max_dano)/2)-j_resistencia
                if i_hab6_dano_atual<0:
                    i_hab6_dano_atual=0
                print(f'{c["pr"]}CAOS toma conta de todo o seu ser, mas você consegue suportar parte da dor. Você toma {c["sub"]+str(i_hab6_dano_atual)+c["pr"]} pontos de dano.{c["n"]}')
                j_vida_atual -= i_hab6_dano_atual
            sleep(2)
            i_hab6_cooldown_atual = i_hab6_cooldown_base


        if j_hab2_duracao_atual<j_hab2_duracao_base and j_atordoado==0:
            j_hab2_duracao_atual+=1
            print(f'{c["vm"]}Você está atordoado, então uma de suas {c["vd"]+"ESQUIVAS EXTRAS"+c["vm"]} é perdida. {c["vd"]+c["sub"]+str(j_hab2_duracao_base-j_hab2_duracao_atual)+c["vd"]} ESQUIVAS EXTRAS restantes.{c["n"]}')
        elif j_hab2_duracao_atual<j_hab2_duracao_base and i_teste_acerto>=0:
            j_hab2_duracao_atual+=1
            print(f'{c["vd"]}ESQUIVA EXTRA UTILIZADA! {c["sub"]+str(j_hab2_duracao_base-j_hab2_duracao_atual)+c["vd"]} ESQUIVAS EXTRAS restantes.{c["n"]}')
            sleep(2)
            if j_hab2_duracao_base-j_hab2_duracao_atual == 0:
                print(f'{c["vm"]}Suas {c["vd"]+"ESQUIVAS EXTRAS"+c["vm"]} acabaram!{c["n"]}')
                sleep(2)
        elif (j_hab2_duracao_atual<j_hab2_duracao_base) and ('2'!=i_escolha!='4' and '5' not in i_acoes) and (j_atordoado==0):
            print(f'{c["vd"]}Você conseguiu esquivar de primeira, então não precisou usar sua SEGUNDA ESQUIVA! {c["sub"]+str(j_hab2_duracao_base-j_hab2_duracao_atual)+c["vd"]} esquivas restantes.{c["n"]}')
            sleep(2)


    if i_hab2_duracao_atual==i_hab2_duracao_base:
        print(f'{c["vd"]}Os {c["az"]+"ESPINHOS"+c["vd"]} no corpo do inimigo desapareceram!{c["n"]}')
        sleep(2)

    i_atordoado+=1

    if j_morrendo==2:
        i_morrendo=2

    if i_morrendo=="morto" and j_morrendo=="vivo":
        print(f'{c["neg"]}Com essa última ação, as forças do inimigo finalmente cessam. Ele morre, e, com isso, você {c["vd"]}Vence{c["n"]}.')
        sleep(2)
        break
    elif j_morrendo!='2' and i_morrendo=="morto":
        print(f'{c["neg"]}O inimigo morre, porém ele decide levar alguém junto, e esse alguém é você. Houve um {c["ama"]}Empate{c["n"]}')
        sleep(2)
        break

    if j_vida_atual<=0 and j_morrendo=="vivo":
        print(f'Você sente suas forças e sua mente se esvaindo. Você está morrendo. Porém, aqui, palavras não importam. {c["neg"]}Qual será sua última ação?{c["n"]}')# frase_epica(2).exe
        j_morrendo="morto"
        j_hab2_cooldown_atual=j_hab3_cooldown_atual=j_hab4_cooldown_atual=j_hab5_cooldown_atual=j_hab6_duracao_atual=0
        sleep(4)