import json

class Tablero:
  def __init__(self, listaV, listaH):
    self.nfil = len(listaV)
    self.ncol = len(listaH)
    self.listaV = listaV
    self.listaH = listaH

    cuadricula = [[[]]]
    for f in range(self.nfil):
      cuadricula.append([])
      for c in range(self.ncol):
        cuadricula[f].append([])
        cuadricula[f][c].append(False)
        cuadricula[f][c].append(False)

    self.cuadricula = cuadricula 

  @staticmethod
  def desdeJson(file):
    dic = json.load(file)
    return Tablero(**dic)

  @staticmethod
  def validar(tablero):
    #TODO: Algoritmo para descifrar las posiciones requeridas para ganar y marcarlas en la cuadricula
    return tablero

  @staticmethod
  def reiniciar(tablero):
    #TODO: Algoritmo para descifrar las posiciones requeridas para ganar y marcarlas en la cuadricula
    return tablero