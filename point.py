""" April 25, 2021 """

import pygame
import random
from setup.settings import Settings
from setup.printr import Printr


class Point:

    def __init__(self, win, arr_coord, pixel_coord, centroid):
        pygame.init()
        self.win = win
        self.printr = Printr(self.win)
        self.set = Settings()

        self.arr = arr_coord
        self.pixel = pixel_coord

        self.centroid = centroid
        self.cluster = None

        self.c = self.set.ultra_light_grey
        self.r = 3
        self.centroid_r = 8


    def set_cluster(self, cluster):
        self.cluster = cluster
        self.c = self.set.class_colours[cluster]
        

    def get_cluster(self):
        return self.cluster

    def get_arr_coord(self):
        return self.arr

    def draw(self):
        r = self.r
        if self.centroid:
            r = self.centroid_r

        pygame.draw.circle(self.win, self.c, self.pixel, r, 0)
