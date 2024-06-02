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

<<<<<<< HEAD
  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    for value in self.img:
    	vertical.append(value[::-1])

    return vertical

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    return Picture(None)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    imagen_invertida=[]
    for cadena in self.img:
          cadena_invertida=str("")
          for caracter in cadena:
            if caracter == ".": 
              cadena_invertida=cadena_invertida+str(inverter.get(caracter))
            else :
              cadena_invertida=cadena_invertida+caracter
          print(cadena_invertida)
          imagen_invertida.append(cadena_invertida)
    return Picture(imagen_invertida)
  
=======
>>>>>>> 8d6e8c5537e09899bf420f998016c6925f1344c6
  def join(self, p):
    """funcioin para rpetir la imagen  """
    nuevaImagen = []

    for index, value in enumerate(self.img):
      nuevaImagen.append(list(value) + list(p.img[index]))

    return Picture(nuevaImagen)
  
  
  
  def horizontalRepeat(self, n):
<<<<<<< HEAD
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    nueva_imagen=[]
    for imagenes in self.img:
      nueva_imagen.append(imagenes*n)
    return Picture(nueva_imagen)
=======
    """ realiza la repeticion pero horizontal """
    # aux = self
    for _ in range(n-1):
      aux = aux.join(self) 
    return aux
>>>>>>> 8d6e8c5537e09899bf420f998016c6925f1344c6


