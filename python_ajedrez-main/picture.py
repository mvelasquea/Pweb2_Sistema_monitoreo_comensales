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

  def join(self, p):
    """funcioin para rpetir la imagen  """
    nuevaImagen = []

    for index, value in enumerate(self.img):
      nuevaImagen.append(list(value) + list(p.img[index]))

    return Picture(nuevaImagen)
  
  
  
  def horizontalRepeat(self, n):
    """ realiza la repeticion pero horizontal """
    aux = self
    for _ in range(n-1):
      aux = aux.join(self) 
    return aux

  
