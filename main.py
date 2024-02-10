import readchar

jugador = input('Digite el nombre del jugador: ')

print(f'¡Vienvenido {jugador}!')


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
