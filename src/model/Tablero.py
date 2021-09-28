class Tablero:
  def __init__(self, listaV, listaH):
    self.nfil = len(listaV)
    self.ncol = len(listaH)
    self.listaV = listaV
    self.listaH = listaH