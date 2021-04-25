""" April 24, 2021 """

import pygame
import math as m
import numpy as np
import random
from setup.printr import Printr
from arr import Arr
from plot import Plot
from point import Point


class Algo(Arr):
    def __init__(self, win):
        pygame.init()

        self.win = win
        super().__init__()

        self.printr = Printr(self.win)
        self.plot = Plot(self.win)

        self.k = 3
        self.build_points()
        self.centroids = None
        self.step = 0

        ## Flags
        self.step2a = True
        self.step1 = True
        self.show_cursor = False


    def update(self, show_cursor):
        self.show_cursor = show_cursor


    def draw(self):
        self.plot.draw()

        for point in self.points:
            point.draw()

        if self.centroids:
            for centroid in self.centroids:
                centroid.draw()

        self.draw_cursor()

        self.printr.print_instructions(self.k, self.step, self.show_cursor)


    def kmeans_step(self):
        if self.step1:
            self.kmeans_step1()
            self.step1 = False

        else:
            if self.step2a:
                self.compute_centroids()
            else:
                self.assign_clusters()

            self.step2a = not self.step2a

        self.step += 1


    def kmeans_step1(self):
        for point in self.points:
            cluster = random.choices( range(self.k) )[0]
            point.set_cluster(cluster)


    def compute_centroids(self):
        """
        This is step 2a
        1. Get the arr_x and arr_y means for each cluster
        2. Assign a new point to this spot -- this is the cluster centroid
        """
        ### Build shell for means
        self.centroids = [ [0,0] for x in range(self.k)]
        count = [0, 0, 0]

        ### Iterate through all points and compute their means to their cluster
        for point in self.points:
            cluster = point.get_cluster()
            x, y = point.get_arr_coord()
            self.centroids[cluster][0] += x
            self.centroids[cluster][1] += y

            count[cluster] += 1

        for i, coord in enumerate(self.centroids):
            x = coord[0] / count[i]
            y = coord[1] / count[i]

            px, py = self.convert_arr_to_pixels( (x, y) )

            centroid = Point(self.win, (x, y), (px, py), True)
            centroid.set_cluster(i)

            ## Replace the coordinates with a point object as the centroid
            self.centroids[i] = centroid


    def assign_clusters(self):
        """
        This is step 2b
        1. Iterate through each point and calculate its distance to each centroid
        2. Assign it to the cluster associated with its nearest centroid
        """
        for point in self.points:
            x, y = point.get_arr_coord()
            mn = m.inf
            cluster = None

            for centroid in self.centroids:
                new_cluster = centroid.get_cluster()

                x1, y1 = centroid.get_arr_coord()
                euclid = m.sqrt( (x1-x)**2 + (y1-y)**2 )

                if euclid < mn:
                    mn = euclid
                    cluster = new_cluster

            point.set_cluster(cluster)


    def configure_plot(self):
        self.plot.configure_scales(self.arr_scale, self.pixel_scale, self.pixel_w, self.pixel_h)


    def build_points(self):
        self.points = []
        arr = self.arr[:,:2]

        for arr_coord in arr:
            centroid = False
            pixel_coord = self.convert_arr_to_pixels(arr_coord)
            point = Point(self.win, arr_coord, pixel_coord, centroid)
            self.points.append( point )


    def draw_cursor(self):
        if self.show_cursor:
            mx, my = pygame.mouse.get_pos()
            pygame.draw.circle(self.win, self.set.grey, (mx, my), 8, 0)

            self.draw_cursor_coord(mx, my)


    def draw_cursor_coord(self, mx, my):
        arr_x, arr_y = self.convert_pixel_to_arr((mx, my))
        arr_x, arr_y = round(arr_x, 1), round(arr_y, 1)

        arr_coord = "(" + str(arr_x) + ", "  + str(arr_y) + ")"
        px_coord = "(" + str(mx) + "," + str(my) + ")"

        mx += 8 + 12
        self.printr.coord_printr(arr_coord, mx, my, self.set.grey)
        self.printr.coord_printr(px_coord, mx, my+15, self.set.blue)
