from interpreter import draw
from chessPictures import *
tab = knight
tab = Picture.join(tab, Picture.negative(knight))
tab = Picture.up(Picture.negative(tab), tab)
draw(tab)