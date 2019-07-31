import os
import time
import pygame as pg
from pprint import pprint

from src.action import update, actions

class Game():
  display = None
  win_size = (0,0)
  pg_events = [
    'MouseButtonUp', 
    'MouseButtonDown', 
    'MouseMotion' ]
  
  def __init__(self, win_size):
    self.display = pg.display.set_mode(win_size)
    self.win_size = win_size
    self.cursor = pg.mouse.get_cursor()

  def draw(self, board, player):
    if(len(board.squares) == 0):
      self.display.blit(board.draw(), board.surface.get_rect())
    else:
      self.display.blit(board.update(), board.surface.get_rect())
      pp = player.piece # player moving piece
      if(pp): self.display.blit(pp.surface, (pp.x,  pp.y))

  def MouseButtonUp(self, board, event, player):
    if(player.piece):
      action = actions.DROP
    else:
      action = actions.IDLE
    return action

  def MouseButtonDown(self, board, event, player):
    is_leftclick = event.button == 1
    if(is_leftclick and board.square(event.pos).within(event.pos) and not player.piece):
      action = actions.GRAB
    elif(is_leftclick and board.square(None, { 'active': True })):
      action = actions.JUMP
    else:
      action = actions.IDLE
    return action

  def MouseMotion(self, board, event, player):
    is_leftclick = event.buttons[0] == 1
    if(is_leftclick and player.piece):        
      action = actions.DRAG
    elif(board.square(event.pos).within(event.pos)):
      action = actions.HOVER
    else:
      action = actions.CLEAR
    return action

  def run(self, ui, board, players):
    player = players[0]
    clock = pg.time.Clock()
    ui_pos = (board.size[0],0)

    quit = False
    init = True
    self.draw(board, player)
    while not quit:
      clock.tick(60)
      for event in pg.event.get():
        quit = event.type == pg.QUIT
        pg_event = pg.event.event_name(event.type)
        if pg_event in self.pg_events:
          if(board.within(event.pos)):
            input = getattr(self, pg_event)
            action = input(board, event, player)
            if(action != actions.IDLE):
              # update game
              board, player = update(board, player, action, event)
              # draw game
              self.draw(board, player)
              # pg update
              pg.display.flip()
      # debug
      fps = int(clock.get_fps())
      # update ui
      self.display.blit(ui.draw(fps), ui_pos)
