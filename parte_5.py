import os
import random
import readchar

class Juego:
    def __init__(self, jugador, mapa, cordenada_inicial, cordenada_final ):
        # Constructor de la clase Juego
        self.jugador = jugador
        self.mapa = mapa
        self.cordenada_inicial = cordenada_inicial
        self.cordenada_final = cordenada_final
        self.px, self.py = 0, 0
        self.mapa[self.px][self.py] = 'P'  # Coloca al jugador en la posición inicial

    def borrar_mostrar_mapa(self):
        # Método para borrar la pantalla y mostrar el mapa actualizado
        os.system('cls' if os.name=='nt' else 'clear')
        for fila in self.mapa:
            print(' '.join(fila))

    def mover_jugador(self, direccion):
        # Método para mover al jugador en el mapa
        if direccion == 'up':
            nueva_px = self.px - 1
            if nueva_px >= 0 and self.mapa[nueva_px][self.py] != '#':
                self.mapa[self.px][self.py] = '.'  # Borra la posición anterior del jugador
                self.px = nueva_px
        elif direccion == 'down':
            nueva_px = self.px + 1
            if nueva_px < len(self.mapa) and self.mapa[nueva_px][self.py] != '#':
                self.mapa[self.px][self.py] = '.'  # Borra la posición anterior del jugador
                self.px = nueva_px
        elif direccion == 'right':
            nueva_py = self.py + 1
            if nueva_py < len(self.mapa[0]) and self.mapa[self.px][nueva_py] != '#':
                self.mapa[self.px][self.py] = '.'  # Borra la posición anterior del jugador
                self.py = nueva_py
        elif direccion == 'left':
            nueva_py = self.py - 1
            if nueva_py >= 0 and self.mapa[self.px][nueva_py] != '#':
                self.mapa[self.px][self.py] = '.'  # Borra la posición anterior del jugador
                self.py = nueva_py

        self.mapa[self.px][self.py] = 'P'  # Actualiza la posición del jugador en el mapa

    def main_loop(self):
        # Bucle principal del juego
        print(f'¡Bienvenido {self.jugador}!')  # Mensaje de bienvenida
        input("Presiona Enter para comenzar...")
        
        while (self.px, self.py) != self.cordenada_final:
            self.borrar_mostrar_mapa()  # Borra la pantalla y muestra el mapa actualizado
            print('Dirija al jugador P con las teclas: ↑ ↓ → ←')
            caracter = readchar.readkey()  # Lee la tecla presionada por el jugador

            # Mueve al jugador en la dirección correspondiente
            if caracter == readchar.key.UP:
                self.mover_jugador('up')
            elif caracter == readchar.key.DOWN:
                self.mover_jugador('down')
            elif caracter == readchar.key.RIGHT:
                self.mover_jugador('right')
            elif caracter == readchar.key.LEFT:
                self.mover_jugador('left')

        self.borrar_mostrar_mapa()  # Muestra el mapa final una vez que se llega al final del laberinto
        print(f'¡Felicitaciones {self.jugador}! ¡Has llegado al final!')

class JuegoArchivo(Juego):
    def __init__(self, jugador, path_a_mapas):
        mapa, cordenada_inicial, cordenada_final = self.elegir_mapa_aleatorio(path_a_mapas)
        super().__init__(jugador, mapa, cordenada_inicial, cordenada_final)

    def elegir_mapa_aleatorio(self, path_a_mapas):
        archivos_de_mapas = os.listdir(path_a_mapas)
        nombre_archivo = random.choice(archivos_de_mapas)
        path_completo = os.path.join(path_a_mapas, nombre_archivo)

        with open(path_completo, 'r') as archivo:
            contenido_mapa = archivo.read()

        # Leer datos de inicio y fin desde la primera fila
        primer_fila = contenido_mapa.strip().split('\n')[0]
        puntos = list(map(int, primer_fila.split()))

        cordenada_inicial = (puntos[0], puntos[1])
        cordenada_final = (puntos[2], puntos[3])

        # Procesar las filas del mapa
        filas_mapa = [list(fila) for fila in contenido_mapa.strip().split('\n')[1:]]

        return filas_mapa, cordenada_inicial, cordenada_final

    def ejecutar(self):
        self.main_loop()