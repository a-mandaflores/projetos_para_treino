#Conversor de unidade:

from os import system, name

def limpar_tela():

    if name == 'nt':
        _ = system('cls')
    
    else:
        _ = system('clear')


def conversor():

    limpar_tela()
    
    print('Bem vindo ao conversor de unidade ')
    print('Escolha a unidade que gostaria de converter')

    print('\n1 - Celsius para Fahrenheit')
    print('2 - Fahrenheit para Celsius')
    print('3 - Quilômetros para Milhas')
    print('4 - Milhas para Quilômetros')
    print('5 - Finalizar operações')

    continuar = True

    while continuar:
        try:

            entrada_escolhida = int(input('\nQual a conversão desejada: (1/2/3/4/5) '))
                    

            if entrada_escolhida == 1:
                celcius = int(input('Quantos graus C para conversão: '))
                calc = (celcius * 9/5) + 32
                print(calc)

                nova_conversao = input('Gotaria de fazer uma nova conversão (s/n)')
                if nova_conversao == 'n':
                    continuar = False
                    print('O programa esta sendo finalizado. ')
                else: 
                    continuar = True

            elif entrada_escolhida == 2:
                fahrenheit = float(input('Quantos graus F para conversão: '))
                calc = (fahrenheit - 32) * 5/9
                print(int(calc))

                nova_conversao = input('Gotaria de fazer uma nova conversão (s/n)')
                if nova_conversao == 'n':
                    continuar = False
                    print('O programa esta sendo finalizado. ')
                else: 
                    continuar = True

            elif entrada_escolhida == 3:
                quilometros = int(input('Quantos graus KM para conversão: '))
                calc = quilometros * 0.62137119
                print(calc)

                nova_conversao = input('Gotaria de fazer uma nova conversão (s/n)')
                if nova_conversao == 'n':
                    continuar = False
                    print('O programa esta sendo finalizado. ')
                else: 
                    continuar = True

            elif entrada_escolhida == 4:
                milhas = float(input('Quantos graus Milhas para conversão: '))
                calc = milhas * 1.60934
                print(calc)

                nova_conversao = input('Gotaria de fazer uma nova conversão (s/n)')
                if nova_conversao == 'n':
                    continuar = False
                    print('O programa esta sendo finalizado. ')
                else: 
                    continuar = True

            elif entrada_escolhida > 5:
                print('O dado não é valido, precisa ser entre 1, 2, 3, 4 ou 5 ')

                nova_conversao = input('Gotaria de continuar (s/n)')
                if nova_conversao == 'n':
                    continuar = False
                    print('O programa esta sendo finalizado. ')
                else: 
                    continuar = True
            else:
                continuar = False
                print('O programa esta sendo finalizado. ')

        except:
            print('Entrada invalida, escolha um numero valido')

    
        

print(conversor())

