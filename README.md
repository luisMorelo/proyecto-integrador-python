PROYECTO GENERAL
El proyecto de este curso consistirá en un videojuego de texto de recorrer laberintos. Este consistirá de laberintos representados por caracteres ASCII dónde # representará una pared, . un pasillo y P el personaje.

Podrás moverte por el mapa usando las teclas ↑ ↓ ← → de tu teclado.

1. Proyecto Integrador parte 1: 
    -Se crea el archivo main del proyecto
    -Se crea una variable llamada jugador en la que se guarda el nombre del jugador
    -Finalmente se imprime un mensaje de vienvenida con el nombre del jugador digitado 

2. proyecto integrador parte 2:
   Se escribió un bucle infinito leyendo e imprimiento las teclas y sólo termina cuando se presiona la tecla ↑ indicada como UP

3. proyecto integrador parte 3:
   Inicia con un número en 0, lee la tecla `n` del teclado en un bucle, por cada presionada, borrar la terminal y e imprimir el nuevo número hasta el número 50.

4. Proyecto integrador parte 4:
   -Se implementó una función que recibe el mapa de un laberinto en forma de cadena, y lo convierta a matriz de caracteres.
   -Se escribió una función que limpia la pantalla y muestre la matriz (recibe el mapa en    forma  de matriz)
   -Se implementó el main loop en una función (recibe el mapa en forma de matriz)

5. Proyecto integrador parte 5: 
   -Encapsulando el juego en una clase, implementa la clase Juego, ahora el mapa y las posiciones inicial y final son   atributos de esta clase, reescribe todas tus funciones anteriores de forma que sean métodos de la clase y todo esté encapsulado.
   -Instanciar el juego y ejecutarlo desde el main

   -Almacenando mapas en archivos
   -Creé una nueva clase JuegoArchivo la cual hereda de Juego,
   Reescribí el constructor para leer un archivo al azar de una carpeta que contenga los mapas cada vez que se instancia el juego.
   -Se creó un método para leer los datos de estos archivos de mapa y devuelva una cadena que tenga concatenada todas las filas leídas del mapa y las coordenadas de inicio y fin.