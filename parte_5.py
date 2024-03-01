import os
import readchar


class Juego:
    def __init__(self, mapa, cordenada_inicial, cordenada_final):
        self.mapa = mapa
        self.cordenada_inicial = cordenada_inicial
        self.cordenada_final = cordenada_final

        
    #1 Convierte el string del mapa en una matriz de caracteres 
    def convetir_mapa(self):
        self.mapa = self.mapa.split("\n")
        self.mapa = [list(fila) for fila in self.mapa]
        return self.mapa
        
        
    #2 Borra la consola y muestra el mapa que recibe en forma de matriz
    def borrar_mostrar_mapa(self):
        os.system('cls' if os.name=='nt' else 'clear')
        for fila in self.mapa:
            print(' '.join(fila))

        
    #3 Implementación del main loop en una función
    def main_loop(self):

            
        cordenada_inicial = (len(mapa[0][0])-1, len(mapa[0][0])-1)
        cordenada_final = (len(mapa)-1), (len(mapa[0])-1)

        px = 0
        py = 0

        posicion_jugador_p = self.mapa[px][py] 
        self.mapa[px][px] = 'P'

            
        while (px,py) != self.cordenada_final:

            #Separa la matríz y la muestra sin llaves ni corchetes 
            self.borrar_mostrar_mapa(self)

            print('Dirija al jugador P con las fechas izquierda, derecha, arriba y abajo')
            caracter = readchar.readkey()


            if caracter == readchar.key.UP: #flecha hacia arriba
                p_arriba = px - 1

                #Verificamos que no se salga del self.mapa y que no sea una pared (Un numeral)
                if p_arriba < 0 or p_arriba > 21 or self.mapa[p_arriba][py] == '#':
                    posicion_jugador_p = self.mapa[px][py] 
                    self.mapa[px][py] = 'P'
                else:
                    posicion_jugador_p = self.mapa[p_arriba][py]
                    self.mapa[p_arriba][py] = 'P'
                    self.mapa[px][py] = '.'
                    px = p_arriba
                #Muestra el self.self.mapa 
                self.borrar_mostrar_mapa()

            if caracter == readchar.key.DOWN: #flecha hacia abajo
                p_abajo = px + 1

                #Verificamos que no se salga del self.self.mapa y que no sea una pared (Un numeral)
                if p_abajo < 0 or p_abajo > 21 or self.mapa[p_abajo][py] == '#':
                    posicion_jugador_p = self.mapa[px][py] 
                    self.mapa[px][py] = 'P'
                else:
                    posicion_jugador_p = self.mapa[p_abajo][py]
                    self.mapa[p_abajo][py] = 'P'
                    self.mapa[px][py] = '.'
                    px = p_abajo
                #Muestra el self.self.mapa
                self.borrar_mostrar_mapa() 
                

            if caracter == readchar.key.RIGHT: #flecha derecha
                p_derecha = py + 1

                #Verificamos que no se salga del self.self.mapa y que no sea una pared (Un numeral)
                if p_derecha < 0 or p_derecha > 21 or self.mapa[px][p_derecha] == '#':
                    posicion_jugador_p = self.mapa[px][py] 
                    self.mapa[px][py] = 'P'
                else:
                    posicion_jugador_p = self.mapa[px][p_derecha]
                    self.mapa[px][p_derecha] = 'P'
                    self.mapa[px][py] = '.'
                    py = p_derecha
                
                #Muestra el self.self.mapa
                self.borrar_mostrar_mapa()
                    

            if caracter == readchar.key.LEFT: #flecha izquierda
                p_izquierda = py - 1

                #Verificamos que no se salga del self.self.mapa y que no sea una pared (Un numeral)
                if p_izquierda < 0 or p_izquierda > 21 or self.mapa[px][p_izquierda] == '#':
                    posicion_jugador_p = self.mapa[px][py] 
                    self.mapa[px][py] = 'P'
                else:
                    posicion_jugador_p = self.mapa[px][p_izquierda]
                    self.mapa[px][p_izquierda] = 'P'
                    self.mapa[px][py] = '.'
                    py = p_izquierda
                #Muestra el self.self.mapa 
                self.borrar_mostrar_mapa()


            if (px,py) == self.cordenada_final:
                print(f'Felicitaciones ganaste, haz llegado hasta el final!')

mapa = """..###################
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

# Instanciamos la clase y ejecutamos el juego
juego = Juego(mapa, (0, 0), (21, 21))
juego.main_loop()