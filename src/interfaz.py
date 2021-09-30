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

def tamSubListaMasGrande(listaDeListas):
    max = 0
    for lista in listaDeListas:
        if(len(lista) > max):
            max = len(lista)
    
    return max

def mostrarTablero(tablero):
    maxV = tamSubListaMasGrande(tablero.listaV)
    maxH = tamSubListaMasGrande(tablero.listaH)

    print("\n", end = "")
    for c in range(tablero.ncol):
        if(c == 0):
            print((" " * (maxV + 1)) + "+---", end = "")
        else:
            print("+---", end = "")
    print("+", end = "")
    for i in range(maxH):
        print("\n", end = "")
        j = 0
        for c in range((tablero.ncol * 4) + 1):
            if(c == 0 or c % 4 == 0):
                if(c == 0):
                    print((" " * (maxV + 1)) + "|", end = "")
                else:
                    print("|", end = "")
            elif(c % 2 == 0 and not c % 4 == 0):
                if(i < len(tablero.listaH[j])):
                    print(tablero.listaH[j][i], end = "")
                else:
                    print(" ", end = "")
                j+=1
            else:
                print(" ", end = "")
    print("\n", end = "")
    for c in range(tablero.ncol):
        if(c == 0):
            print("+" + ("-" * maxV) + "+---", end = "")
        else:
            print("+---", end = "")
    print("+", end = "")
    for k in range(tablero.nfil):
        print("\n", end = "")
        for c in range((tablero.ncol * 4) + 1):
            if(c == 0 or c % 4 == 0):
                if(c == 0):
                    print("|", end = "")
                    for entero in tablero.listaV[k]:
                        diferencia = maxV - len(tablero.listaV[k]) 
                        if(diferencia == 0):
                            print(str(entero), end = "")
                        elif(diferencia > 0):
                            print((" " * diferencia) + str(entero), end = "")
                    print("|", end = "")
                else:
                    print("|", end = "")
            elif(c % 2 == 0 and not c % 4 == 0):
                print(" ", end = "")
            else:
                print(" ", end = "")
        print("\n", end = "")
        for c in range(tablero.ncol):
            if(c == 0):
                print("+" + ("-" * maxV) + "+---", end = "")
            else:
                print("+---", end = "")
        print("+", end = "")




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

    salir = False
    while(salir != True):
        mostrarTablero(Tablero.desdeJson(file))

        nfil = input("\n\n\t\tDigita el numero de fila: ")
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