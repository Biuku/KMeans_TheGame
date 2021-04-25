""" April 25, 2021 """

import pygame
from setup.settings import Settings
from setup.printr import Printr


class Plot:

    def __init__(self, win):
        pygame.init()
        self.win = win
        self.printr = Printr(self.win)
        self.set = Settings()

        self.c1 = self.set.ultra_light_grey
        self.c2 = self.set.light_grey
        self.c3 = self.set.grey
        self.c4 = self.set.dark_grey


    def draw(self):
        self.draw_axes()
        self.draw_x_axis_labels()
        self.draw_y_axis_labels()
        #self.draw_origin()


    """ DRAW PLOT """

    def draw_array(self, pixels):
        for coord in pixels[:,:2]:
            pygame.draw.circle(self.win, self.set.red, coord, 2, 0)


    def draw_axes(self):
        x, y = self.pixel_origin
        right = x + self.pixel_w
        top = y - self.pixel_h

        pygame.draw.line(self.win, self.c4, (x, y), (x, top), 2)
        pygame.draw.line(self.win, self.c4, (x, y), (right, y), 2)


    def draw_x_axis_labels(self):
        ### Draw x scale
        origin_x, y = self.pixel_origin

        for i in range(len(self.pixel_scale)):
            pixel_x = self.pixel_scale[i,0]

            ### Draw dot on axis
            pygame.draw.circle(self.win, self.c1, (pixel_x, y+1), 2, 0)

            ### Draw labels
            x_offset = pixel_x - 5
            y_offset = y + 10

            arr_label = round(self.arr_scale[i,0], 1)
            pixel_label = int(self.pixel_scale[i,0])

            self.printr.axis_label_printr(arr_label, x_offset, y_offset, self.c1)
            self.printr.axis_label_printr(pixel_label, x_offset, y_offset + 15, self.set.blue)


    def draw_y_axis_labels(self):
            ### Print y scale
            x, origin_y = self.pixel_origin

            for i in range(len(self.pixel_scale)):
                pixel_y = self.pixel_scale[i,1]

                ### Draw dot on axis
                pygame.draw.circle(self.win, self.set.grey, (x+1, pixel_y), 2, 0)

                ### Draw labels
                y_offset = pixel_y - 8
                x_offset = x - 30

                arr_label = round(self.arr_scale[i,1], 1)
                pixel_label = int(self.pixel_scale[i,1])

                self.printr.axis_label_printr(arr_label, x_offset, y_offset, self.c1)
                self.printr.axis_label_printr(pixel_label, x_offset, y_offset + 12, self.set.blue)




    """ UTILITY """
    def configure_scales(self, arr, px, w, h):
        self.arr_scale = arr
        self.pixel_scale = px
        self.pixel_origin = (px[0,0], px[0,1])
        self.pixel_w = w
        self.pixel_h = h
