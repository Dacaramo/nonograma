import json

class Tablero:
  def __init__(self, listaV, listaH):
    self.nfil = len(listaV)
    self.ncol = len(listaH)
    self.listaV = listaV
    self.listaH = listaH
    self.cuadricula = [[]] #[.][.][0] -> Lo que debería ir - [.][.][1] -> Lo que el usuario coloca

  @staticmethod
  def desdeJson(file):
    dic = json.load(file)
    return Tablero(**dic)

  def llenarCuadricula(cuadricula):
    #TODO: Algoritmo para descifrar las posiciones requeridas para ganar y marcarlas en la cuadricula
    return cuadricula