import pygame as pg

class UI():
    def __init__(self, ui_size):
        self.size = ui_size
        self.font = pg.font.Font(None, 30)
        self.ui = pg.Surface(self.size)

    def draw(self, clock_fps = 0):
        fps = self.font.render(str(clock_fps), True, pg.Color('white'))
        self.ui.fill((0,0,0))
        self.ui.blit(fps, (20,20))
        return self.ui