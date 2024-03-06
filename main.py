import os
from parte_5 import Juego, JuegoArchivo



# Mensaje de bienvenida al usuario para el inicio del juego
print('Bienvenido al juego del laberinto.')
nombre = input('Ingrese su nombre: ')
print(f'{nombre}, el juego está por comenzar. Prepárate.')
input('Presiona Enter para comenzar...')

# Instanciar el juego con mapas aleatorios
path_a_mapas = os.path.join(os.path.dirname(__file__), 'mapas')
juego_archivo = JuegoArchivo(nombre, path_a_mapas)

# Ejecución del juego
juego_archivo.ejecutar()

# Mensaje de finalización del juego
print(f'¡Felicitaciones por terminar el juego, {nombre}!')



'''
#PROYECTO INTEGRADOR PARTE 2
while True:
    print('Ingrese el caracter')
    caracter = readchar.readkey()
    if caracter == readchar.key.UP:
        print(f'Flecha arriba, cerrando el sistema...')
        break 
    elif caracter == readchar.key.DOWN :
        print(f'El caracter introducido fue: Flecha abajo')
    elif caracter == readchar.key.RIGHT:
        print(f'El caracter introducido fue: Flecha derecha')
    elif caracter == readchar.key.LEFT:
        print(f'El caracter introducido fue: Flecha izquierda')
    else:
        print(f'El caracter introducido fue: {caracter}')
    print()
''' 


