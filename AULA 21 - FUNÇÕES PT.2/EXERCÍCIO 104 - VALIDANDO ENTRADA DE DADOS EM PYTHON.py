'''

CRIE UM PROGRAMA QUE TENHA A FUNÇÃO leiaint(), QUE VAI FUNCIONAR DE FORMA
SEMELHANTE A FUNÇÃO input() DO PYTHON, SÓ QUE FAZENDO A VALIDAÇÃO PARA ACEITAR
APENAS UM VALOR NUMÉRICO.

ex: 
n = leiaint('Digite um n)

'''

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO ! Digite um número inteiro válido.\033[m')
        if ok:
            break

    return valor







# PROGRAMA PRINCIPAL

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar um número {n}')
