from colors import *

class Picture:
  def __init__(self, img):
    self.img = img

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    for value in self.img:
      vertical.append(value[::-1])

    return Picture(vertical)


  def horizontalMirror(self):

    """ Devuelve el espejo horizontal de la imagen """
    horizontal = []
    for value in reversed(self.img):
      horizontal.append(value[::1])
    return Picture(horizontal)


  def negative(self):
    """ Devuelve el negativo de la imagen """
    nuevaImagen = []
    for value in self.img:
      row = []
      for caracter in value:
        row.append(self._invColor(caracter))
      nuevaImagen.append(row)    
    return Picture(nuevaImagen)


  def join(self, p):
    """ pone la imagen al lado derecho usando el argumento p """
    nuevaImagen = []

    for index, value in enumerate(self.img):
      nuevaImagen.append(list(value) + list(p.img[index]))

    return Picture(nuevaImagen)
  
  def up(self, p):
    """Devuelve a la figura encima de la actual """
    nuevaImagen = []
    #copiar todo p a nueva imange
    for value in p.img:
      nuevaImagen.append(value[::1])
    
    for value in self.img:
      nuevaImagen.append(value[::1])
    return Picture(nuevaImagen)


  def under(self, p):
    """ Devuelve una nueva y lla pone ensima de la actual"""
    nuevaImagen = []
    for value in self.img:
        nuevaImagen.append(list(value))

    for i, value in enumerate(p.img):
      for j, caracter in enumerate(value):
        if(nuevaImagen[i][j] == ' '):
          nuevaImagen[i][j] = caracter
        

    return Picture(nuevaImagen)
    
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    aux = self
    for _ in range(n-1):
      aux = aux.join(self) 
    return aux


  def verticalRepeat(self, n):
    """Devuelve una nueva figura repitiendo la figura actual debajo, la cantidad
de veces que indique el valor de n"""
    aux = self
    for _ in range(n-1):
      aux = aux.up(self) 
    return aux

  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""

    """
    00 01 02 03 0n
    10 11 12 13 1n
    20 21 22 23 2n 
    30 31 32 33 3n
    n0 n1 n2 n3 nn

    n0 30 20 10 00
    n1 31 21 11 01
    n2 32 22 12 02
    n3 33 23 13 03
    nn 3n 2n 1n 0n

    -> The index ij -> n - j, i
    """

    #generar la matriz de carateres original!
    matrizOriginal = []
    for value in self.img:
      matrizOriginal.append(value)

    #actualizamos cada valor en la matriz
    size = len(matrizOriginal)
    matrizRotate = [['' for _ in range(size)] for _ in range(size)]     #crea una matriz vacia!

    print("El tamaño de esa matriz es: ", size)
    for i in range(len(matrizOriginal)):
      for j in range(len(matrizOriginal[i])):
        print("Indices de rotate: ", size - j - 1, " y ", i)
        print("Se accede al caracter: ", matrizRotate[size - j - 1][i])
        matrizRotate[size - j - 1][i] =  matrizOriginal[i][j]


    return Picture(matrizRotate)
