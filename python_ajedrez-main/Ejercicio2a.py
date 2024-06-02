from chessPictures import *
<<<<<<< HEAD
from interpreter import draw
from picture import Picture
from colors import *

tab = knight
#llama a la picture creando la primera coluna 
tab = Picture.join(tab, Picture.negative(knight)) 
#llama ala segunda columna 
draw(Picture.up(Picture.negative(tab), tab))
=======
tab = knight
tab = Picture.join(tab, Picture.negative(knight))
tab = Picture.up(Picture.negative(tab), tab)
draw(tab)
>>>>>>> df8f628231e271c37e75bf880b129d6a81d50828
