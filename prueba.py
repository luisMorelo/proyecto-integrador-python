import readchar


while True:
    print('Ingrese una tecla (o presione "flecha arriba" para salir):')
    caracter = readchar.readkey()

    if caracter == readchar.key.UP:
        print('Saliendo del programa...')
        break
    elif caracter == readchar.key.DOWN :
        print('El caracter introducido fue: Flecha abajo')
    elif caracter == readchar.key.RIGHT:
        print('El caracter introducido fue: Flecha derecha')
    elif caracter == readchar.key.LEFT:
        print('El caracter introducido fue: Flecha izquierda')
    else:
        print(f'El caracter introducido fue: {caracter}')

    #print('Una prueba de paciencia')