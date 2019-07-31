import os
import pygame as pg

_HAND_CURSOR = (
"        XX      ",
"    XX X..XXX   ",
"   X..XX..X.XX  ",
"   X..XX..X.X.X ",
"   X..XX..X.X.X ",
"   X..XX..X.X.X ",
" XX X..X..X.X.X ",
"X..XX.........X ",
"X...X.........X ",
" X.....X.X.X..X ",
"  X....X.X.X..X ",
"  X....X.X.X.X  ",
"   X...X.X.X.X  ",
"    XXXXXXXXX   ",
"     X......X   ",
"     XXXXXXXX   ")
_HCURS, _HMASK = pg.cursors.compile(_HAND_CURSOR, ".", "X")
HAND_CURSOR = ((16, 16), (5, 1), _HCURS, _HMASK)

_GRAB_CURSOR = (
"                ",
"                ",
"                ",
"    xXX XX X X  ",
"   X...X..X.X.X ",
"   X...X..X.X.X ",
"    X.........X ",
"  XXX.........X ",
" X..X.........X ",
" X.....X.X.X..X ",
" X.....X.X.X..X ",
"  X....X.X.X.X  ",
"   X...X.X.X.X  ",
"    XXXXXXXXX   ",
"     X......X   ",
"     XXXXXXXX   ")
_GCURS, _GMASK = pg.cursors.compile(_GRAB_CURSOR, ".", "X")
GRAB_CURSOR = ((16, 16), (5, 1), _GCURS, _GMASK)

DEFAULT_CURSOR = ((16, 16), (0, 0), (0, 0, 64, 0, 96, 0, 112, 0, 120, 0, 124, 0, 126, 0, 127, 0, 127, 128, 124, 0, 108, 0, 70, 0, 6, 0, 3, 0, 3, 0, 0, 0), (192, 0, 224, 0, 240, 0, 248, 0, 252, 0, 254, 0, 255, 0, 255, 128, 255, 192, 255, 224, 254, 0, 239, 0, 207, 0, 135, 128, 7, 128, 3, 0))
