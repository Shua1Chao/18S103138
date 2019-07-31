import os
import pygame as pg
from pygame import Surface

class Piece(pg.sprite.Sprite):
  def __init__(self, props):
    for k, v in props.items():
      setattr(self, k, v)

    pg.sprite.Sprite.__init__(self)
    piece_path = os.path.join('images', self.color + self.role + '.png')
    piece_png = pg.image.load(piece_path)
    piece_rect = piece_png.get_rect()
    self.piece_png = pg.transform.smoothscale(piece_png, (self.size, self.size))
    self.surface = Surface((self.size, self.size), pg.SRCALPHA)

  def draw(self):
    self.surface.blit(self.piece_png, (0,0))
    return self
