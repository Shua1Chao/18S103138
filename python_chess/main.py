#!/usr/bin/env python
import pygame as pg
from src.ui import UI
from src.game import Game
from src.board import Board
from src.player import new_players

SIZE = (800,640)
PLAYERS = ['white', 'black']
TITLE = "python chess"
ICON = "icon.png"

def main(): 
  # init
  pg.init()
  pg.font.init()
  pg.display.set_icon(pg.image.load(ICON))
  pg.display.set_caption(TITLE)
  # setup
  ui = UI((SIZE[0]-SIZE[1], SIZE[1]))
  game = Game(SIZE)
  board = Board(SIZE[1])
  # ready
  players = new_players(PLAYERS)
  # begin
  game.run(ui, board, players)
  # gg
  pg.quit()
  return quit()

if __name__=="__main__":
  main()