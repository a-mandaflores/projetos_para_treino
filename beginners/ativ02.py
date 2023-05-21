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
    lista_senha_nova = []

    comprimento = int(input('Quantos caracteres pode ter a senha? '))
    senha = 0
    while senha < comprimento:
        caracteres = ['!', '@', '.']

        if caracteres in lista_senha_nova:
            inserir_senha = random.choice(string.ascii_letters)
            lista_senha_nova.append(inserir_senha)
        else:
            lista_senha_nova.append(random.choice(caracteres))
        
        senha += 1

    senha_nova = ''.join(lista_senha_nova)
    
    print('Sua nova senha é:', senha_nova)




print(gerador())


