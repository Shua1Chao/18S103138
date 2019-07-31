import pygame as pg
from cursors import (
  HAND_CURSOR, 
  GRAB_CURSOR, 
  DEFAULT_CURSOR )

class Actions():
  IDLE  = 0
  HOVER = 1
  GRAB  = 2
  DRAG  = 3
  DROP  = 4
  JUMP  = 6
  CLEAR = 7

actions = Actions()

def drag_piece(pos, piece):
  piece_rect = piece.piece_png.get_rect()
  piece.x = pos[0] - piece_rect[2]/2
  piece.y = pos[1] - piece_rect[3]/2
  return piece

def update(board, player, action, event):
  square = board.square(event.pos)

  update_cursor(action)

  if(action == actions.HOVER):
    board.clear()
    square.hover = True
    square.fresh = False

  elif(action == actions.GRAB):
    player.piece = drag_piece(event.pos, square.remove_piece())
    player.piece.path.append(square)
    square.hover = False

  elif(action == actions.DRAG):
    player.piece = drag_piece(event.pos, player.piece)

  elif(action == actions.DROP):
    square.place_piece(player.piece)
    if(len(player.piece.path) > 0 and player.piece.path[-1] == square):
      player.piece.path.pop()
      board.clear()
      square.active = True      
    else: 
      square.active = False
      square.hover = False
    player.piece = None

  elif(action == actions.JUMP):
    actuar = board.square(None, { 'active': True })
    square.place_piece(actuar.piece)
    square.hover = True
    square.fresh = False
    actuar.active = False
    actuar.hover = False
    actuar.fresh = False
    actuar.piece = None

  elif(action == actions.CLEAR):
    board.clear()

  return board, player

def update_cursor(action):
  if(action == actions.HOVER):
    cursor = HAND_CURSOR
  elif(action == actions.GRAB \
    or action == actions.DRAG):
    cursor = GRAB_CURSOR
  elif(action == actions.DROP \
    or action == actions.JUMP):
    cursor = HAND_CURSOR
  else:
    cursor = DEFAULT_CURSOR

  pg.mouse.set_cursor(*cursor)
    