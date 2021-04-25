""" April 22, 2021 """

import pygame
import numpy as np
from setup.settings import Settings


class Arr:

    def __init__(self):
        pygame.init()
        self.set = Settings()

        self.origin_gap_left = 0.07 + self.set.border_gap## lower = left
        self.origin_gap_bottom = 0.12 + self.set.border_gap ## lower = up

        self.arr = np.load('data/blobs150_54_2-2.npy')
        self.axis_labels = 15

        self.update_pixel_anchors(1600, 900)
        self.configure()


    """ A. CONFIGURE ARRAYS AND AXIS SCALES FOR 3 UNITS: ARR, NORM_ARR, AND PIXELS """

    def configure(self):
        ### On initialization and when resizing ###

        self.arr_scale = self.configure_arr_scale()
        self.pixel_scale = self.configure_pixel_scale()
        self.configure_conversion_factors()


    """ A2. Configure scales """

    def configure_arr_scale(self):
        n = self.axis_labels
        x, y = self.arr[:,0], self.arr[:,1]

        x_scale = np.linspace( 0, x.max(), n ).reshape(n, 1)
        y_scale = np.linspace( 0, y.max(), n ).reshape(n, 1)

        return np.concatenate((x_scale, y_scale), axis = 1)

    ### PIXELS
    def configure_pixel_scale(self):
        n = self.axis_labels
        x_min, y_max = self.pixel_origin
        x_max = x_min + self.pixel_w
        y_min = y_max - self.pixel_h ## pixel y: 'min' = more 'up'

        x = np.linspace( x_min, x_max, n ).reshape(n, 1)
        y = np.linspace( y_max, y_min, n ).reshape(n, 1)

        return np.concatenate( (x, y), axis = 1)


    """ A3. CONVERSION STUFF """
    def configure_conversion_factors(self):
        i = 7

        arr_x, arr_y = self.arr_scale[i, 0], self.arr_scale[i, 1]
        px_x, px_y = self.pixel_scale[i, 0], self.pixel_scale[i, 1]

        px_x_min, px_y_max = self.pixel_origin

        self.x_to_arr = arr_x / (px_x - px_x_min)
        self.y_to_arr = arr_y / (px_y_max - px_y)

        # Reverse direction = inverse
        self.x_to_pixels = 1 / self.x_to_arr
        self.y_to_pixels = 1 / self.y_to_arr


    def convert_pixel_to_arr(self, pixel_coord):
        """ Converts x, y pixel coordinates to original arr units """
        x, y = pixel_coord
        px_x_min, px_y_max = self.pixel_origin

        x -= px_x_min
        y = px_y_max - y

        x *= self.x_to_arr
        y *= self.y_to_arr

        return x, y


    def convert_arr_to_pixels(self, arr_coord):
        """ Convert from normalized arr units to pygame-useful pixel units """

        x, y = arr_coord

        x *= self.x_to_pixels
        y *= self.y_to_pixels

        px_x_min, px_y_max = self.pixel_origin

        x += px_x_min
        y = px_y_max - y

        return int(x), int(y) ## Pixel values should be int


    """ A4. SCREEN SIZE ADJUSTMENTS """

    def update_pixel_anchors(self, win_w, win_h):
        ### When the screen resizes, update the size anchors for the graph ###

        ## Pixel width and height
        self.pixel_w = win_w * 0.7
        self.pixel_h = win_h * 0.7

        ## Pixel origin
        x = win_w * self.origin_gap_left
        y = win_h * (1-self.origin_gap_bottom)
        self.pixel_origin = (x, y)
