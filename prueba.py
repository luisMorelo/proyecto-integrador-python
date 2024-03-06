import os
import random

'''
archivo = os.listdir("./mapas")

print(archivo)

#Para elegir un elemento aleatorio

mapa_aleatorio = random.choice(archivo)

print('Lista aleatoria', mapa_aleatorio)

self.cordenada_final = (len(mapa) - 2, len(mapa[0]) - 1)


path_completo = f"{'./mapas'}/{mapa_aleatorio}"

print(f'este es el path completo {path_completo}') 
'''
archivos_de_mapas = os.listdir("./mapas")
nombre_archivo = random.choice(archivos_de_mapas)
path_completo = os.path.join("./mapas", nombre_archivo)

with open(path_completo, 'r') as archivo:
    contenido_mapa = archivo.read()

        # Leer datos de inicio y fin desde la primera fila
primer_fila = contenido_mapa.strip().split('\n')[0]
puntos = list(map(int, primer_fila.split()))
        
punto_inicial = (puntos[0], puntos[1])
punto_final = (puntos[2], puntos[3])

print('voy a imprimir las coordenadas', punto_final)
