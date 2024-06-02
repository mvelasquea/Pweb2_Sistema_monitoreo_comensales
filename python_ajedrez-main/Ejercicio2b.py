from chessPictures import *
from interpreter import draw
from picture import Picture
from colors import *

tab = knight
tab = Picture.join(tab, Picture.negative(knight))
tab = Picture.up(Picture.verticalMirror(tab), tab)
draw(tab)