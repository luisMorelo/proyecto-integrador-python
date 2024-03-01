
import os

def borrar_terminal():
    os.system('cls' if os.name=='nt' else 'clear')


def imprimir_numero():
        
    num = 0
    print(num)
    while num<=50:

        letra = input('Presione la tecla "n" : ')

        if letra == 'n':
            borrar_terminal()
        else:
            print('Tecla vacía o incorrecta')
            break

        print(num)
        num +=1


imprimir_numero()
