from random import randint
from time import sleep

perguntas = ['''Qual das palavras a seguir se refere a bancos?
Alternativa 1: Acento
Alternativa 2: Assento
Alternativa 3: Açento
Alternativa 4: Nenhuma das alternativas anteriores''',
# 1º pergunta: 2

'''Qual é o nome da radiação responsável pela "evaporação" de buracos negros? 
Alternativa 1: Radiação Hawking
Alternativa 2: Radiação Ultravioleta
Alternativa 3: Raios Gama
Alternativa 4: Raios X''',
# 2º pergunta: 1

'''Em que linguagem de programação esse código foi escrito?
Alternativa 1: C++
Alternativa 2: Java
Alternativa 3: C#
Alternativa 4: Python''',
# 3º pergunta: 4

'''Qual jogo ganhou o prêmio de "Melhor Jogo do Ano" no The Game Awards de 2018?
Alternativa 1: Red Dead Redemption 2
Alternativa 2: Assassin's creed Odyssey
Alternativa 3: Marvel's Spider Man
Alternativa 4: God of War''',
# 4º pergunta: 4

'''Qual foi o 17º presidente do Brasil (de 1951 até 1954)?
Alternativa 1: José Linhares
Alternativa 2: Júlio Prestes
Alternativa 3: Getúlio Vargas
Alternativa 4: Deodoro da Fonseca''',
# 5º pergunta: 3

'''Em que ano o jogo Minecraft foi lançado?
Alternativa 1: 1997
Alternativa 2: 2001
Alternativa 3: 2009
Alternativa 4: 2014''',
# 6º pergunta: 3

'''Qual foi a primeira nação a mandar um homem para a lua?
Alternativa 1: Estados Unidos
Alternativa 2: Índia
Alternativa 3: União Soviética
Alternativa 4: Japão''',
# 7º pergunta: 1

'''Qual é a 5º religião com o maior número de seguidores no mundo inteiro?
Alternativa 1: Islamismo
Alternativa 2: Budismo
Alternativa 3: Judaísmo
Alternativa 4: Hinduísmo''',
# 8º pergunta: 2

'''Qual foi o primeiro animal a ser mandado para o espaço?
Alternativa 1: um pássaro
Alternativa 2: um gato
Alternativa 3: um macaco
Alternativa 4: um cachorro''',
# 9º pergunta: 4

'''Qual é o SEGUNDO país com o maior número de habitantes na Terra?
Alternativa 1: China
Alternativa 2: Estados Unidos
Alternativa 3: Índia
Alternativa 4: Nigéria''',
# 10º pergunta: 3

'''Qual das religiões a seguir NÃO é monoteísta?
Alternativa 1: Judaísmo
Alternativa 2: Islamismo
Alternativa 3: Hinduísmo
Alternativa 4: Cristianismo''',
# 11º pergunta: 3

'''Dentre os sistemas econômicos a seguir, qual deles predominou na Europa Ocidental entre os séculos V e XV?
Alternativa 1: Sistema Feudal
Alternativa 2: Sistema Capitalista
Alternativa 3: Sistema Escravista
Alternativa 4: Sistema Asiático''',
# 12º pergunta: 1

'''Na banda "Mamonas Assassinas", qual era o instrumento tocado pelo integrante Sérgio Reoli?
Alternativa 1: Baixo
Alternativa 2: Bateria
Alternativa 3: Vocal
Alternativa 4: Teclado''',
# 13º pergunta: 2

'''Em 2020, qual era o Produto Interno Bruto (PIB), em dólares, do Brasil?
Alternativa 1: 1,449 trilhão
Alternativa 2: 1,387 trilhão
Alternativa 3: 2,021 trilhões
Alternativa 4: 1,012 trilhão''',
# 14º pergunta: 1

'''Quanto é 1 + 1?
Alternativa 1: 3
Alternativa 2: 1.323.448
Alternativa 3: 11
Alternativa 4: 2''',
# 15º pergunta: 4

'''Qual das seguintes raças de cachorro normalmente tem um pelo todo amarelo/dourado?
Alternativa 1: Golden River
Alternativa 2: Pitbull
Alternativa 3: Shih Tzu
Alternativa 4: Beagle''',
# 16º pergunta: 1

'''Até o ano de 2022, quantos copas do mundo foram ganhas pela Alemanha? 
Alternativa 1: 3
Alternativa 2: 5
Alternativa 3: 4
Alternativa 4: 2''',
# 17º pertunta: 3

'''A Páscoa remonta origem de qual religião?
Alternativa 1: Islamismo
Alternativa 2: Budismo
Alternativa 3: Taoismo
Alternativa 4: Cristianismo''',
# 18º pergunta: 4

'''Qual dos valores abaixo é igual ao valor de Pi(π)? Considerando apenas os primeiros 7 dígitos.
Alternativa 1: 3,141537
Alternativa 2: 3,141592
Alternativa 3: 3,141658
Alternativa 4: 3,141545''',
# 19º pergunta: 2

'''Normalmente, o crânio humano é composto por quantos ossos?
Alternativa 1: 22
Alternativa 2: 20
Alternativa 3: 17
Alternativa 4: 9''',
# 20º pergunta: 1

'''Qual dos seguintes países tem sua bandeira das cores azul e branca?
Alternativa 1: Irã
Alternativa 2: Cuba
Alternativa 3: Grécia
Alternativa 4: Congo''',
# 21º pergunta: 3

'''Ao jogar dois dados de 6 lados, quais são, aproximadamente, as chances dos dois dados caírem no número 6?
Alternativa 1: 0,8%
Alternativa 2: 4,7%
Alternativa 3: 9,5%
Alternativa 4: 2,8%''',
# 22º pergunta: 4

'''De 0 até 100, quantas vezes o número 5 aparece?
Alternativa 1: 20
Alternativa 2: 10
Alternativa 3: 11
Alternativa 4: 12''',
# 23º pergunta: 1

'''Na velocidade da luz, quanto tempo se levaria para ir da Terra até o Sol?
Alternativa 1: 12 minutos e 10 segundos
Alternativa 2: 2 horas e 23 minutos
Alternativa 3: 8 minutos e 20 segundos
Alternativa 4: 1 hora e 09 minutos''',
# 24º pergunta: 3

'''Qual foi a data da morte de Adolf Hitler?
Alternativa 1: 12 de março de 1929
Alternativa 2: 30 de abril de 1930
Alternativa 3: 02 de outubro de 1930
Alternativa 4: 12 de junho de 1929''',
# 25º pergunta: 2

'''O Besouro-Tigre, considerado o mais rápido inseto conhecido, pode atingir uma velocidade de até:
Alternativa 1: 32km/h
Alternativa 2: 2km/h
Alternativa 3: 12km/h
Alternativa 4: 8km/h''',
# 26º pergunta: 4

'''Vamos colocar um pouco de matemática nisso. 155 + 4^4 ÷ 2 = x.
Alternativa 1: x = 250,5
Alternativa 2: x = 283,0
Alternativa 3: x = 305,0
Alternativa 4: x = 265,5''',
# 27º pergunta: 2

'''721 em romano:
Alternativa 1: DCXVII
Alternativa 2: CCXIV
Alternativa 3: DCCXXI
Alternativa 4: DCCLVII''',
# 28º pergunta: 3

'''"Um entre muitos palhaços, ainda assim um palhaço especial". A frase anterior, em inglês, fica:
Alternativa 1: "One among many clowns, yet still a special one"
Alternativa 2: "A among many clowns, yet still special one"
Alternativa 3: "One among very clowns, yet still an one special"
Alternativa 4: "One among many clowns, still but an one special"''',
# 29º pergunta: 1

'''Na língua portuguesa, existem quantas classes gramaticais?
Alternativa 1: 7
Alternativa 2: 10
Alternativa 3: 9
Alternativa 4: 8'''
# 30º pergunta: 2
]
# perguntas  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
respostas = [2, 1, 4, 4, 3, 3, 1, 2, 4, 3, 3, 1, 2, 1, 4, 1, 3, 4, 2, 1, 3, 4, 1, 3, 2, 4, 2, 3, 1, 2]

acerta_pergunta = ['Belo portugês!',
# 1º pergunta
'Um pouco de física pode ser útil.',
# 2º pergunta
'Olhando o código fica fácil, não é?',
# 3º pergunta
'Alguns dizem que Read Dead Redemption 2 deveria ter ganho.',
# 4º pergunta
'Com certeza um dos presidentes que o Brasil teve.',
# 5º pergunta
'Já faz mais de 10 anos...',
# 6º pergunta
'foram 2 pessoas no voo Apolo 11!',
# 7º pergunta
'Ouvi dizer que tem umas lições de vida bem úteis.',
# 8º pergunta
'Laika era o nome dela!',
# 9º pergunta
'Só cerca de 1/5 da populção mundial.',
# 10º pergunta
'Com mais de 3 mil deuses adorados!',
# 11º pergunta
'Amplamente utilizado em diversos países no passado.',
# 12º pergunta
'Ele amava tocar bateria.',
# 13º pergunta
'Em reais, equivale à R$6.955,2.',
# 14º pergunta
'Pelo visto temos um gênio da matemática aqui!',
# 15º pergunta
'Também conhecido por ser extremamante dócil (e caro).',
# 16º pergunta
'Quase tantas copas quanto o Brasil (só quase).',
# 17º pergunta
'Que, na próxima páscoa, você ganhe muitas ovadas! Não pera.',
# 18º pergunta
'Tem muitos dígitos a mais. Muitos.',
# 19º pergunta
'Ossos do cérebro não inclusos.',
# 20º pergunta
'Um dos não muitos países que não tem 3 cores na bandeira.',
# 21º pergunta
'Em uma sessão de RPG de mesa, essa situação (talvez) seria bastante gratificante',
# 22º pergunta
'Agora pense de 0 a 1.000.',
# 23º pergunta
'Mesmo sendo rápida, a luz ainda atrasa uns minutos.',
# 24º pergunta
'Morto por suicído.',
# 25º pergunta
'Parece lento, mas para um inseto não.',
# 26º pergunta
'Deve ter demorado bastante.',
# 27º pergunta
'Números no formato de letras é algo meio estranho.',
# 28º pergunta
'AMOGUS',
# 29º pergunta
'Deve ser demorado aprender tudo isso. Um pouco.']
# 30º pergunta

erra_pergunta = ['Confuso, não?',
# 1º pergunta
'Infelizmente não é uma radiação tão conhecida.',
# 2º pergunta
'Dá pra só olhar o código. A não ser que você não entenda do assunto',
# 3º pergunta
'Esse não, mas foi indicado para o prêmio.',
# 4º pergunta
'Só mais um dos muitos presitentes do Brasil.',
# 5º pergunta
'Tá perto, mas não tão perto.',
# 6º pergunta
'Essa não conseguiu, mas tentou.',
# 7º pergunta
'Dica: não tem dica.',
# 8º pergunta
'Não foi esse, mas poderia ser uma boa opção...',
# 9º pergunta
'Tá quente.',
# 10º pergunta
'Para caso não saiba: monoteísta: acredita em um único Deus.',
# 11º pergunta
'Esse também é bastante antigo.',
# 12º pergunta
'Poderia ser interessante ver ele tocando esse instrumento.',
# 13º pergunta
'Mesmo não sendo esse, ainda é bastante dinheiro, não?',
# 14º pergunta
'Pelo visto coloquei uma pergunta difícil demais aqui...',
# 15º pergunta
'Todos são fofos de qualquer forma.',
# 16º pergunta
'Dica: menos que o Brasil (hehe).',
# 17º pergunta
'Se fosse nessa religião, qual seria o mascote?',
# 18º pergunta
'Imagina se eu tivesse pedido todos os dígitos.',
# 19º pergunta
'É só 1: o da cabeça.',
# 20º pergunta
'Sério, por que todo mundo gosta tanto de 3 poucas cores na bandeira?',
# 21º pergunta
'Ainda são bem baixas. Duvido conseguir essa sorte de primeira.',
# 22º pergunta
'Não esqueça de contar as casas da unidade e dezena.',
# 23º pergunta
'Velocidade da luz no vácuo: 299.792,458 km por segundo. Distância do sol: 150 milhões km. v = Δs/Δt.',
# 24º pergunta
'Com certeza não foi ano passado.',
# 25º pergunta
'Dica: menor que a velocidade do som.',
# 26º pergunta
'Contas simples podem ficar bem complicadas quando grandes.',
# 27º pergunta
'I = 1; V = 5; X = 10; L = 50; C = 100; D = 500.',
# 28º pergunta
'Inglês é até bem diferente de português, então pode ser um pouco confuso mesmo.',
# 29º pergunta
'Alguns menos conhecidos: preposição, interjeição e conjunção.']
# 30º pergunta

pt_jogador1 = 0
jogador1 = '\033[1;36mJogador 1\033[m'
pt_jogador2 = 0
jogador2 = '\033[1;35mJogador 2\033[m'
pt_jogador3 = 0
jogador3 = '\033[1;33mJogador 3\033[m'

num_jogadores = int(input('Digite quantos jogadores deseja que participem do jogo (de 1 a 3): '))

if num_jogadores < 1 and num_jogadores > 3:
    print('\033[1;31mNÚMERO INVÁLIDO. Só são permitidos de 1 a 3 jogadores.\033[m')

if num_jogadores == 1:
    print('\033[1;36mO jogo está prestes a começar!')
    print('Serão feitas 10 perguntas. Acerte o máximo que conseguir!\033[m')
    sleep(1.5)

    pergunta = randint(0, 29)
    chute = int(input(f'''\033[1;34m1º pergunta:\033[m {perguntas[pergunta]}
Digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print(f'\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador1 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]
    
    pergunta = randint(0, 28)
    chute = int(input(f'''\033[1;34m2º pergunta:\033[m {perguntas[pergunta]}
Digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador1 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 27)
    chute = int(input(f'''\033[1;34m3º pergunta:\033[m {perguntas[pergunta]}
Digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador1 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta] 

    pergunta = randint(0, 26)
    chute = int(input(f'''\033[1;34m4º pergunta:\033[m {perguntas[pergunta]}
Digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador1 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 25)
    chute = int(input(f'''\033[1;34m5º pergunta:\033[m {perguntas[pergunta]}
Digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador1 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 24)
    chute = int(input(f'''\033[1;34m6º pergunta:\033[m {perguntas[pergunta]}
Digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador1 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 23)
    chute = int(input(f'''\033[1;34m7º pergunta:\033[m {perguntas[pergunta]}
Digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador1 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 22)
    chute = int(input(f'''\033[1;34m8º pergunta:\033[m {perguntas[pergunta]}
Digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador1 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 21)
    chute = int(input(f'''\033[1;34m9º pergunta:\033[m {perguntas[pergunta]}
Digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador1 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 20)
    chute = int(input(f'''\033[1;34m10º e ÚLTIMA perguntna pergunta:\033[m {perguntas[pergunta]}
Digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador1 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    print('\033[1mFIM DAS PERTUNTAS. Calculando pontos...')
    sleep(0.5)
    print('...')
    sleep(0.5)
    print('...')
    sleep(0.5)
    print('...')
    print('\033[m')
    sleep(2)

    print(f'\033[1mAs perguntas acabaram. Você acertou um total de {pt_jogador1} de 10 perguntas ')
    if pt_jogador1 == 10:
        print('\033[1;32mImpressionante! Você conseguiu acertar todas as perguntas. Meus Parabéns!\033[m')
    if 5 <= pt_jogador1 < 10:
        print('\033[1;34mVocê conseguiu acertar várias perguntas. Bom trabalho!\033[m')
    if 0 < pt_jogador1 < 5:
        print('\033[1mParece você não acertou muitas perguntas. Mais sorte na próxima!\033[m')
    if pt_jogador1 == 0:
        print('\033[1;31mPelo visto você não acertou nenhuma pergunta. Talvez devesse estudar mais antes de tentar responder essas perguntas de novo.\033[m')


if num_jogadores == 2:
    print('\033[1;36mOs jogos estão prestes a começar!')
    print('Serão feitas 15 perguntas. Alterne a vez dos jogadores a cada pergunta.\033[m')
    sleep(1.5)

    pergunta = randint(0, 29)
    chute = int(input(f'''\033[1;34m1º pergunta:\033[m {perguntas[pergunta]}
{jogador1}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador1 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 28)
    chute = int(input(f'''\033[1;34m2º pergunta:\033[m {perguntas[pergunta]}
{jogador2}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador2 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 27)
    chute = int(input(f'''\033[1;34m3º pergunta:\033[m {perguntas[pergunta]}
{jogador1}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador1 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 26)
    chute = int(input(f'''\033[1;34m4º pergunta:\033[m {perguntas[pergunta]}
{jogador2}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador2 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 25)
    chute = int(input(f'''\033[1;34m5º pergunta:\033[m {perguntas[pergunta]}
{jogador1}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador1 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 24)
    chute = int(input(f'''\033[1;34m6º pergunta:\033[m {perguntas[pergunta]}
{jogador2}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador2 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 23)
    chute = int(input(f'''\033[1;34m7º pergunta:\033[m {perguntas[pergunta]}
{jogador1}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador1 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 22)
    chute = int(input(f'''\033[1;34m8º pergunta:\033[m {perguntas[pergunta]}
{jogador2}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador2 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 21)
    chute = int(input(f'''\033[1;34m9º pergunta:\033[m {perguntas[pergunta]}
{jogador1}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador1 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 20)
    chute = int(input(f'''\033[1;34m10º pergunta:\033[m {perguntas[pergunta]}
{jogador2}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador2 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 19)
    chute = int(input(f'''\033[1;34m11º pergunta:\033[m {perguntas[pergunta]}
{jogador1}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador1 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 18)
    chute = int(input(f'''\033[1;34m12º pergunta:\033[m {perguntas[pergunta]}
{jogador2}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador2 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 17)
    chute = int(input(f'''\033[1;34m13º pergunta:\033[m {perguntas[pergunta]}
{jogador1}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador1 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 16)
    chute = int(input(f'''\033[1;34m14º pergunta:\033[m {perguntas[pergunta]}
{jogador2}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador2 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 15)
    chute = int(input(f'''\033[1;34m15º pergunta:\033[m {perguntas[pergunta]}
{jogador1}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador1 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 14)
    chute = int(input(f'''\033[1;34m16º e ÚLTIMA pergunta:\033[m {perguntas[pergunta]}
{jogador2}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador2 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    print('\033[1mFIM DAS PERTUNTAS. Calculando pontos...')
    sleep(1)
    print('...')
    sleep(1)
    print('...')
    sleep(1)
    print('...')
    print('\033[m')
    sleep(2)


    if pt_jogador1 > pt_jogador2:
        primeiro = jogador1
        maior = pt_jogador1
        segundo = jogador2
        menor = pt_jogador2
    if pt_jogador2 > pt_jogador1:
        primeiro = jogador2
        maior = pt_jogador2
        segundo = jogador1
        menor = pt_jogador1
    
    if pt_jogador1 != pt_jogador2:
        print(f'''Vencedor: {primeiro} com \033[1;32m{maior} pontos\033[m.
Perdedor: {segundo} com \033[1;31m{menor} pontos\033[m.''')
    if pt_jogador1 == pt_jogador2:
        print(f'Houve um \033[1;33mempate\033[m, com ambos os jogadores acertando \033[1;33m{pt_jogador1} perguntas\033[m.')


if num_jogadores == 3:
    print('\033[1;36mOs jogos estão prestes a começar!')
    print('Serão feitas 21 perguntas. Revezem a chance dos jogadores a cada pergunta.\033[m')
    sleep(1.5)

    pergunta = randint(0, 29)
    chute = int(input(f'''\033[1;34m1º pergunta:\033[m {perguntas[pergunta]}
{jogador1}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador1 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 28)
    chute = int(input(f'''\033[1;34m2º pergunta:\033[m {perguntas[pergunta]}
{jogador2}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador2 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 27)
    chute = int(input(f'''\033[1;34m3º pergunta:\033[m {perguntas[pergunta]}
{jogador3}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador3 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 26)
    chute = int(input(f'''\033[1;34m4º pergunta:\033[m {perguntas[pergunta]}
{jogador1}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador1 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 25)
    chute = int(input(f'''\033[1;34m5º pergunta:\033[m {perguntas[pergunta]}
{jogador2}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador2 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 24)
    chute = int(input(f'''\033[1;34m6º pergunta:\033[m {perguntas[pergunta]}
{jogador3}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador3 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 23)
    chute = int(input(f'''\033[1;34m7º pergunta:\033[m {perguntas[pergunta]}
{jogador1}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador1 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 22)
    chute = int(input(f'''\033[1;34m8º pergunta:\033[m {perguntas[pergunta]}
{jogador2}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador2 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 21)
    chute = int(input(f'''\033[1;34m9º pergunta:\033[m {perguntas[pergunta]}
{jogador3}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador3 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]
    
    pergunta = randint(0, 20)
    chute = int(input(f'''\033[1;34m10º pergunta:\033[m {perguntas[pergunta]}
{jogador1}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador1 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 19)
    chute = int(input(f'''\033[1;34m11º pergunta:\033[m {perguntas[pergunta]}
{jogador2}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador2 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 18)
    chute = int(input(f'''\033[1;34m12º pergunta:\033[m {perguntas[pergunta]}
{jogador3}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador3 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 15)
    chute = int(input(f'''\033[1;34m13º pergunta:\033[m {perguntas[pergunta]}
{jogador1}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador1 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 14)
    chute = int(input(f'''\033[1;34m14º pergunta:\033[m {perguntas[pergunta]}
{jogador2}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador2 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 13)
    chute = int(input(f'''\033[1;34m15º pergunta:\033[m {perguntas[pergunta]}
{jogador3}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador3 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 12)
    chute = int(input(f'''\033[1;34m16º pergunta:\033[m {perguntas[pergunta]}
{jogador1}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador1 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 11)
    chute = int(input(f'''\033[1;34m17º pergunta:\033[m {perguntas[pergunta]}
{jogador2}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador2 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 10)
    chute = int(input(f'''\033[1;34m18º pergunta:\033[m {perguntas[pergunta]}
{jogador3}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador3 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 9)
    chute = int(input(f'''\033[1;34m19º pergunta:\033[m {perguntas[pergunta]}
{jogador1}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador1 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 8)
    chute = int(input(f'''\033[1;34m20º pergunta:\033[m {perguntas[pergunta]}
{jogador2}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador2 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    pergunta = randint(0, 7)
    chute = int(input(f'''\033[1;34m21º e ÚLTIMA pergunta:\033[m {perguntas[pergunta]}
{jogador3}, digite o número da alternativa: '''))
    if chute == respostas[pergunta]:
        print('\033[1;32mResposta correta!\033[m')
        print(f'\033[1;32m{acerta_pergunta[pergunta]}\033[m')
        pt_jogador3 += 1
    else:
        print('\033[1;31mResposta incorreta!\033[m')
        print(f'\033[1;31m{erra_pergunta[pergunta]}\033[m')
    sleep(2.5)
    del perguntas[pergunta]
    del respostas[pergunta]
    del acerta_pergunta[pergunta]
    del erra_pergunta[pergunta]

    print('\033[1mFIM DAS PERTUNTAS. Calculando pontos...')
    sleep(1)
    print('...')
    sleep(1)
    print('...')
    sleep(1)
    print('...')
    print('\033[m')
    sleep(2)

    primeiro = jogador1
    maior = pt_jogador1
    if pt_jogador1 < pt_jogador2 > pt_jogador3:
        primeiro = jogador2
        maior = pt_jogador1
    if pt_jogador1 < pt_jogador3 > pt_jogador2:
        primeiro = jogador3
        maior = pt_jogador3

    terceiro = jogador1
    menor = pt_jogador1
    if pt_jogador1 > pt_jogador2 < pt_jogador3:
        terceiro = jogador2
        menor = pt_jogador2
    if pt_jogador1 > pt_jogador3 < pt_jogador2:
        terceiro = jogador3
        menor = pt_jogador3
    
    segundo = jogador1
    meio = pt_jogador1
    if maior == pt_jogador1 and menor == pt_jogador3 or maior == pt_jogador3 and menor == pt_jogador1:
        segundo = jogador2
        meio = pt_jogador2
    if maior == pt_jogador1 and menor == pt_jogador2 or maior == pt_jogador2 and menor == pt_jogador1:
        segundo = jogador3
        meio = pt_jogador3


    if pt_jogador1 == pt_jogador2 and pt_jogador1 != pt_jogador3 != pt_jogador2:
        if pt_jogador1 > pt_jogador3:
            print(f'\033[1;32m1º lugar: {jogador1} e {jogador2}, ambos com \033[1;32m{pt_jogador1} pontos\033[m.')
            print(f'\033[1;34m2º lugar: {jogador3} com \033[1;34m{pt_jogador3} pontos\033[m.')

        if pt_jogador1 < pt_jogador3:
            print(f'\033[1;32m1º lugar\033[m: {jogador3} com \033[1;32m{pt_jogador3} pontos\033[m.')
            print(f'\033[1;34m2º lugar\033[m: {jogador1} e {jogador2}, ambos com \033[1;34m{pt_jogador1} pontos\033[m.')

    if pt_jogador1 == pt_jogador3 and pt_jogador1 != pt_jogador2 != pt_jogador3:
        if pt_jogador1 > pt_jogador2:
            print(f'\033[1;32m1º lugar\033[m: {jogador1} e {jogador3}, ambos com \033[1;32m{pt_jogador1} pontos\033[m.')
            print(f'\033[1;34m2º lugar\033[m: {jogador2} com \033[1;34m{pt_jogador2} pontos\033[m.')

        if pt_jogador1 < pt_jogador2:
            print(f'\033[1;32m1º lugar\033[m: {jogador2} com \033[1;32m{pt_jogador2} pontos\033[m.')
            print(f'\033[1;34m2º lugar\033[m: {jogador1} e {jogador3}, ambos com \033[1;34m{pt_jogador1} pontos\033[m.')

    if pt_jogador2 == pt_jogador3 and pt_jogador2 != pt_jogador1 != pt_jogador3:
        if pt_jogador2 > pt_jogador1:
            print(f'\033[1;32m1º lugar\033[m: {jogador2} e {jogador3}, ambos com \033[1;32m{pt_jogador2} pontos\033[m.')
            print(f'\033[1;34m2º lugar\033[m: {jogador1} com \033[1;34m{pt_jogador1} pontos\033[m.')

        if pt_jogador2 < pt_jogador1:
            print(f'\033[1;32m1º lugar\033[m: {jogador1} com \033[1;32m{pt_jogador1} pontos\033[m.')
            print(f'\033[1;34m2º lugar\033[m: {jogador2} e {jogador3}, ambos com \033[1;34m{pt_jogador2} pontos\033[m.')

    if pt_jogador1 == pt_jogador2 == pt_jogador3 == pt_jogador1:
        print(f'\033[1mHOUVE UM EMPATE\033[m. Todos os jogadores acertaram \033[1;35m{pt_jogador1} perguntas\033[m.')


    if pt_jogador1 != pt_jogador2 != pt_jogador3 != pt_jogador1:
        print(f'\033[1;32m1º lugar\033[m: {primeiro} com \033[1;32m{maior} pontos\033[m.')
        print(f'\033[1;34m2º lugar\033[m: {segundo} com \033[1;34m{meio} pontos\033[m.')
        print(f'\033[1;31m3º lugar\033[m: {terceiro} com \033[1;31m{menor} pontos\033[m.')
    