from random import choice
from time import sleep
print('\033[34m-><-\033[m' * 13)
print('\033[33mEstou pensando em um numero entre 0 e 5. adivinhe!!\033[m')
print('\033[34m-><-\033[m' * 13)
n = int(input('Qual numero eu pensei?'))
print('\033[37mPROCESSANDO...\033[m')
sleep(2)
numeros = [0, 1, 2, 3, 4, 5]
escolido = choice(numeros)
if n == escolido :
    print('\033[32mPRABÉNS\033[m você escolheu \033[43m{:^3}\033[m. O mesmo numero que eu pensei!!'.format(escolido))
else:
    print('\033[31mVOCÊ PERDEU!!\033[m Eu pensei no numero \033[43m{:^3}\033[m'.format(escolido))
