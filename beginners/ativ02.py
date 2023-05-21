#2. Gerador de senhas:
from os import system, name
import string
import random

print('Gerador de senha.')

def limpar_tela():

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def gerador():

    limpar_tela()

    comprimento = int(input('Quantos caracteres pode ter a senha? '))
    caracteres = string.ascii_letters + string.digits + string.punctuation

    senha_nova = ''.join(random.choice(caracteres) for _ in range(comprimento)) 
    
    print('Sua nova senha é:', senha_nova)




print(gerador())


