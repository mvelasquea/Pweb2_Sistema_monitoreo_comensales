from chessPictures import *
from interpreter import draw
from picture import Picture
from colors import *

tab = knight
#llama a la picture creando la primera coluna 
tab = Picture.join(tab, Picture.negative(knight)) 
#llama ala segunda columna 
draw(Picture.up(Picture.negative(tab), tab))