import pygame as pg
from pygame import Surface
from math import floor
from pprint import pprint
from itertools import product

from src.basic import is_even
from src.square import Square
from src.piece import Piece
from src.FEN import fromFEN

LIGHT = (255,255,255)
DARK = (50,50,50)

START_BOARD = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

class Board:
  squares = []

  def __init__(self, size):
    self.size = (size, size)
    self.sq_size = int(self.size[1]/8)
    self.surface = Surface(self.size)

  def within(self, pos):
    return pos[0] < self.size[0] and pos[1] < self.size[1]

  def clear(self):
    for row in self.squares:
      for sq in row:
        sq.fresh = False
        sq.hover = False

  def square(self, pos = None, query = None):
    squar = None
    if(pos):
      point = lambda i: floor(pos[i]/self.sq_size)
      squar = self.squares[(int)(point(1))][(int)(point(0))]
    if(query):
      match = True
      for k, v in query.items():
        if(squar):
          match = v and getattr(squar, k)
        else:
          for rank in self.squares:
            for sq in rank:
              squar = sq if v and getattr(sq, k) else None
              if(squar):
                break
            if(squar):
              break

      squar = squar if match else None
    return squar

  def update(self):
    for row in self.squares:
      row_blits = []
      for sq in row:
        if(not sq.fresh):
          sq.draw()
        row_blits.append((sq.surface, (sq.x, sq.y)))
      self.surface.blits(row_blits)
    return self.surface

  def draw(self, square = None):
    sq_pad = 8
    font_size = 14

    fen_model = fromFEN(START_BOARD)

    if(len(self.squares) == 0):
      for r in range(0, len(fen_model)):
        rank = fen_model[r]
        row = []
        for s in range(0, len(rank)):
          sq = rank[s]
          _x = sq['_x']
          _y = sq['_y']
          tx = self.sq_size*_x
          ty = self.sq_size*_y
          toggle_color = is_even(_x+1) ^ is_even(_y+1)

          sq_piece = None
          if(sq['piece']):
            sq_piece = Piece({
              '_x' : _x,
              '_y' : _y,
              'x': tx, 
              'y': ty,
              'size': self.sq_size - (sq_pad*2),
              'role': sq['piece']['role'],
              'color': sq['piece']['color'],
              'path': []
            })
          square = Square({
            'size': self.sq_size,
            '_x' : _x,
            '_y' : _y,
            'x' : tx, 
            'y' : ty,
            'pad': sq_pad, 
            'font_size': font_size, 
            'piece': sq_piece,
            'color': DARK if toggle_color else LIGHT,
            'text_color': LIGHT if toggle_color else DARK,
            'label': str(chr(73-(_y+1))) + str(_x+1),
            'file': str(_x+1) if _y == 7 else None,
            'rank': str(chr(73-(_y+1))) if _x == 0 else None,
            'settings': { 
              'draw_coords': False,
              'draw_rankfile': True
            }
          })
          square.draw()
          row.append(square)
        self.squares.append(row)
        row_blits = list(map(lambda s: (s.surface, (s.x, s.y)), row))
        self.surface.blits(row_blits)

    return self.surface

    
