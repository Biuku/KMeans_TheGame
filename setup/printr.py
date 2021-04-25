""" April 20, 2021 """

import pygame
import math as m
import random as r
from setup.settings import Settings


class Printr:
    def __init__(self, win):
        pygame.init()
        self.win = win
        self.set = Settings()


    def coord_printr(self, data, x, y, c):
        text = self.set.med_font.render(data, True, c)
        self.win.blit( text, (x, y) )


    def axis_label_printr(self, coord, x, y, c):
        text = self.set.med_font.render(str(coord), True, c)
        self.win.blit( text, (x, y) )


    def print_instructions(self, k, step, show_cursor):
        win_w = self.win.get_width()
        win_h = self.win.get_height()
        x =  win_w * 0.88 ## lower number --> leftward
        y =  win_h * 0.06 ## lower number --> upward


        texts = [
            'INSTRUCTIONS',
            '  · a = decrease K',
            '  · d = increase K',
            '',
            'KNN',
            '  · K: ' + str(k),
            '  · Step: ' + str(step),
            '  · SSE: ' ,
            '  · Show cursor: ' + str(show_cursor),

            ]

        for text in texts:
            print_instructions = self.set.med_font.render(text, True, self.set.light_grey)
            self.win.blit( print_instructions, (x, y) )
            y += 22


        line_x = x * 0.97
        top = (win_h * self.set.border_gap) + 2
        bot = win_h * (1 - self.set.border_gap) - 2

        pygame.draw.line(self.win, self.set.dark_grey, (line_x, top), (line_x, bot), 1)
