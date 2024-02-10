import os

import readchar


laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

jugador = input('Digite el nombre del jugador: ')

print(f'¡Vienvenido {jugador}!')

#1 Convierte el string del mapa en una matriz de caracteres 
def convetir_mapa(mapa: str):
    mapa = mapa.split("\n")
    mapa = [list(fila) for fila in mapa]
    return mapa

#2 Borra la consola y muestra el mapa que recibe en forma de matriz
def borrar_mostrar_mapa(mapa):
    os.system('cls' if os.name=='nt' else 'clear')
    for fila in mapa:
        print(' '.join(fila))
    

#3 Implementación del main loop en una función
def main_loop(mapa):
    
    cordenada_inicial = (len(mapa[0][0])-1, len(mapa[0][0])-1)
    cordenada_final = (len(mapa)-1), (len(mapa[0])-1)

    px = 0
    py = 0

    posicion_jugador_p = mapa[px][py] 
    mapa[px][px] = 'P'

        
    while (px,py) != cordenada_final:
        
        os.system('cls' if os.name=='nt' else 'clear')

        #Separa la matríz y la muestra sin llaves ni corchetes 
        borrar_mostrar_mapa(mapa)

        print('Dirija al jugador P con las fechas izquierda, derecha, arriba y abajo')
        caracter = readchar.readkey()


        if caracter == readchar.key.UP: #flecha hacia arriba
            p_arriba = px - 1

            #Verificamos que no se salga del mapa y que no sea una pared (Un numeral)
            if p_arriba < 0 or p_arriba > 21 or mapa[p_arriba][py] == '#':
                posicion_jugador_p = mapa[px][py] 
                mapa[px][py] = 'P'
            else:
                posicion_jugador_p = mapa[p_arriba][py]
                mapa[p_arriba][py] = 'P'
                mapa[px][py] = '.'
                px = p_arriba
            #Muestra el mapa 
            borrar_mostrar_mapa(mapa)

        if caracter == readchar.key.DOWN: #flecha hacia abajo
            p_abajo = px + 1

            #Verificamos que no se salga del mapa y que no sea una pared (Un numeral)
            if p_abajo < 0 or p_abajo > 21 or mapa[p_abajo][py] == '#':
                posicion_jugador_p = mapa[px][py] 
                mapa[px][py] = 'P'
            else:
                posicion_jugador_p = mapa[p_abajo][py]
                mapa[p_abajo][py] = 'P'
                mapa[px][py] = '.'
                px = p_abajo
            #Muestra el mapa
            borrar_mostrar_mapa(mapa) 
            

        if caracter == readchar.key.RIGHT: #flecha derecha
            p_derecha = py + 1

            #Verificamos que no se salga del mapa y que no sea una pared (Un numeral)
            if p_derecha < 0 or p_derecha > 21 or mapa[px][p_derecha] == '#':
                posicion_jugador_p = mapa[px][py] 
                mapa[px][py] = 'P'
            else:
                posicion_jugador_p = mapa[px][p_derecha]
                mapa[px][p_derecha] = 'P'
                mapa[px][py] = '.'
                py = p_derecha
            
            #Muestra el mapa
            borrar_mostrar_mapa(mapa)
                

        if caracter == readchar.key.LEFT: #flecha izquierda
            p_izquierda = py - 1

            #Verificamos que no se salga del mapa y que no sea una pared (Un numeral)
            if p_izquierda < 0 or p_izquierda > 21 or mapa[px][p_izquierda] == '#':
                posicion_jugador_p = mapa[px][py] 
                mapa[px][py] = 'P'
            else:
                posicion_jugador_p = mapa[px][p_izquierda]
                mapa[px][p_izquierda] = 'P'
                mapa[px][py] = '.'
                py = p_izquierda
            #Muestra el mapa 
            borrar_mostrar_mapa(mapa)


        if (px,py) == cordenada_final:
            print(f'Felicitaciones {jugador} ganaste, haz llegado hasta el final!')


    

main_loop(convetir_mapa(laberinto))


