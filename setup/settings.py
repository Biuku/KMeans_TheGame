""" April 22, 2021 """

import pygame


class Settings:

    def __init__(self):

        ## Set gap in % from edge of pygame window to page border
        self.border_gap = 0.02

        self.clock = pygame.time.Clock()
        self.FPS = 120

        ### Colours
        self.white, self.black = (255, 255, 255), (0, 0, 0)
        self.ultra_light_grey = (240, 240, 240)
        self.light_grey, self.grey, self.dark_grey = (221, 221, 221), (150,150,150), (45, 45, 45)

        self.blue, self.light_blue = (190, 170, 255), (210, 210, 255)
        self.red, self.light_red = (255, 0, 0), (255, 175, 175)
        self.green, self.orange, self.blue_green = (0, 159, 115), (222, 160, 0), (118, 173, 215)

        self.class_colours = [self.green, self.orange, self.blue_green, self.red]

        ## Colour styles
        self.object1_538 = (217, 240, 222)
        self.object2_538 = (255, 234, 217)

        self.background = (10, 10, 10) #self.black

        ### Fonts
        self.small_font = pygame.font.SysFont('lucidasans', 10)
        self.med_font = pygame.font.SysFont('lucidasans', 11)
        self.large_font = pygame.font.SysFont('lucidasans', 12)
