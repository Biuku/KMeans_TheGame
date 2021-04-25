""" APRIL 25, 2021 """

import pygame
from setup.settings import Settings
from setup.pygameBasics import PygameBasics
from algo import Algo


class Main(PygameBasics):
    def __init__(self):
        pygame.init()
        super().__init__()

        self.win_w, self.win_h  = 1600, 900
        self.win = pygame.display.set_mode((self.win_w, self.win_h), pygame.RESIZABLE)

        self.algo = Algo(self.win)
        self.update_window_size(0) ##

        ## Movement flags
        self.stepping = True
        self.show_cursor = False



    """ EVENTS """

    def left_click_events(self):
        self.show_cursor = not self.show_cursor

    def right_click_events(self):
        pass

    def mouse_button_up_events(self):
        pass

    def keydown_events(self, event):
        if event.key == pygame.K_SPACE:
            self.algo.kmeans_step()

        if event.key == pygame.K_q:
            pygame.quit(), quit()

    def keyup_events(self, event):
        pass


    def update_window_size(self, event):
        """ called from pygameBasics -- elif event.type == pygame.VIDEORESIZE: """
        if event:
            self.win = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        ## When user resizes the window, adjust the w and h values everything else is anchored to
        self.win_w = self.win.get_width()
        self.win_h = self.win.get_height()

        self.algo.update_pixel_anchors(self.win_w, self.win_h)
        self.algo.configure()
        self.algo.configure_plot()


    """ UPDATES """

    def updates(self):
        self.update_window_size(False)
        self.algo.update(self.show_cursor)
        self.draw()


    def draw(self):
        self.win.fill(self.set.background)
        self.draw_page_border()
        self.algo.draw()

        pygame.display.update()


    """ MAIN """

    def main(self):
        while True:
            self.set.clock.tick(self.set.FPS)
            self.events()
            self.updates()

if __name__ == "__main__":
    x = Main()
    x.main()
