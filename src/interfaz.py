from sys import dont_write_bytecode
from model.Tablero import Tablero
from types import SimpleNamespace
import json
import os

def mostrarInstrucciones():
    print("\n+------------------------------------------------------------------------------------------------+")
    print("| Marca con una X las casillas según los números que aparecen en el exterior del tablero.        |\n" +
          "| Los números de la parte superior afectan a cada columna y los de la izquierda afectan a        |\n" +
          "| las filas. Estas secuencias de números indican la longitud de las líneas continuas de          |\n" +
          "| casillas rellenas que hay en una fila o columna dada. Así, por ejemplo, si encontramos la      |\n" +
          "| secuencia 5 3 en una fila, nos indica que tenemos dos bloques separados, uno compuesto         |\n" +
          "| por de 3 casillas contiguas con una X y el otro formado por 5 casillas consecutivas con una X. |")
    print("+------------------------------------------------------------------------------------------------+")

def mostrarTablero(tablero):
    print("listaV -> ", tablero.listaV)
    print("listaH -> ", tablero.listaH)

def jugar():
    print("\t\t\nEscojer un tablero de juego\n\n" 
            + "\t1)Tablero 1\n" 
            + "\t2)Tablero 2\n" 
            + "\t3)Tablero 3\n")
    opc = input("\t\tOPC: ")

    if(opc == "1"):
        PATH = os.path.join(os.path.dirname(__file__), 'tablero1.json')
    elif(opc == "2"):
        PATH = os.path.join(os.path.dirname(__file__), 'tablero2.json')
    elif(opc == "3"):
        PATH = os.path.join(os.path.dirname(__file__), 'tablero3.json')

    file = open(PATH, "r")

    mostrarTablero(Tablero.desdeJson(json.dumps(file.read())))

    nfil = input("\n\t\tDigita el numero de fila: ")
    ncol = input("\n\t\tDigita el numero de columna: ")

#######################################################

salir = False
while (not salir):
    print("\t\t\n-- Bienvenido a N°N°GRAMAS --\n\n" 
            + "\t1)Instrucciones\n" 
            + "\t2)Jugar\n" 
            + "\t3)Salir\n")
    opc = input("\t\tOPC: ")

    if(opc == "1"):
        mostrarInstrucciones()
    elif(opc == "2"):
        jugar()
    elif(opc == "3"):
        salir = True