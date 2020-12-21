import pygame
import pygame_gui
from pygame import *
from pygame_gui import *
from pygame.image import *

SIZE = WIDTH, HEIGHT = 1920, 1080
LVl_2 = False


class Menu:

    def __init__(self):

        init()
        display.set_caption('Sweet House')

        self.menu_screen = display.set_mode(SIZE)
        self.menu_surface = Surface(SIZE)

        self.menu_image = image.load('./Materials/image.png')
        self.error_sound = './Materials/erro.mp3'

    def menu(self):

        self.menu_surface.blit(self.menu_image, (0, 0))
        self.menu_screen.blit(self.menu_surface, (0, 0))

    def main_loop(self):

        exit_ = False

        while not exit_:

            self.menu()
            display.flip()

            for event_ in pygame.event.get():  # main events

                if event_.type == QUIT:
                    exit_ = True

                if event_.type == MOUSEBUTTONDOWN:

                    mixer.music.load(self.error_sound)
                    mixer.music.play()

                    exit_2 = False

                    while not exit_2:

                        StartGame().level_1()
                        display.flip()

                        for event_2 in pygame.event.get():  # main events

                            if event_2.type == QUIT:
                                exit_ = True


class StartGame:

    def __init__(self):

        self.level_1_screen = display.set_mode(SIZE)
        self.level_1_surface = Surface(SIZE)

        self.windows_error = image.load('./Materials/bsod_2.jpg')
        self.noise = image.load('./Materials/noise_1.png')

    def level_1(self):

        self.level_1_surface.blit(self.windows_error, (0, 0))
        self.level_1_screen.blit(self.level_1_surface, (0, 0))

        display.flip()

        time.delay(3000)

        self.level_1_surface.blit(self.noise, (0, 0))
        self.level_1_screen.blit(self.level_1_surface, (0, 0))

        self.loop_2()

    def loop_2(self):

        self.level_1_screen.fill((0, 0, 0))

        exit_ = False

        while not exit_:
            self.level_2()
            display.flip()

            for event_ in pygame.event.get():  # main events

                if event_.type == QUIT:
                    exit_ = True

    def level_2(self):
        pass

    def main_loop(self):
        exit_ = False

        while not exit_:
            self.level_1()
            display.flip()

            for event_ in pygame.event.get():  # main events

                if event_.type == QUIT:
                    exit_ = True


if __name__ == '__main__':
    Menu().main_loop()
