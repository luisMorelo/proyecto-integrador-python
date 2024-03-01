import readchar
from parte_5 import Juego


jugador = input('Digite el nombre del jugador aquie n el main: ')

print(f'¡Vienvenido {jugador}!')


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
from parte_5 import Juego

def main():
    # Definir el mapa y las coordenadas iniciales y finales
    mapa = "#########\n#.......#\n#.......#\n#.......#\n#.......#\n#.......#\n#.......#\n#########"
    coordenada_inicial = (1, 1)
    coordenada_final = (7, 7)

    # Crear una instancia de la clase Juego
    juego = Juego(mapa, coordenada_inicial, coordenada_final)
    
    # Llamar al método main_loop()
    juego.main_loop()

if __name__ == "__main__":
    main()
