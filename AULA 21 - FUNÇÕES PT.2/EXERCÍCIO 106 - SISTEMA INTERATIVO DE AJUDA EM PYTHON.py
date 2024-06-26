'''

FAÇA UM MINI-SSTEMA QUE UTILIZE O INTERACTIVE HELP DO PYTHON.
O USUÁRIO VAI DIGITAR O COMANDO E O MANUAL VAI APARECER. 
QUANDO O USUÁRIO DIGITAR A PALAVRA FIM, O PROGRAMA SE ENCERRARÁ.

OBS: USE CORES

'''

from time import sleep

# CORES

c = ('\033[m',       # 0 - sem cores
    '\033[0;30;41m', # 1 - vermelho
    '\033[0;30;42m', # 2 - verde
    '\033[0;30;43m', # 3 - amarelo
    '\033[0;30;44m', # 4 - azul
    '\033[0;30;45m', # 5 - roxo
    '\033[7;30'      # 6 - branco
    );







def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(1.2)


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(0.8)



# PROGRAMA PRINCIPAL

comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM' :
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)
