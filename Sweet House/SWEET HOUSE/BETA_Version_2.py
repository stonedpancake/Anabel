import sys
import pygame
import pygame_gui
from pygame import *
from pygame.image import load
import text_animation
import YesNo
import Keyboard
import Anabel

SIZE = WIDTH, HEIGHT = 1920, 1080


class Main:

    def __init__(self):

        init()
        display.set_caption('Sweet House')
        self.screen = display.set_mode(SIZE)

        self.menu_image = image.load('./Materials/image.png')
        self.error_sound = './Materials/erro.mp3'

    def menu(self):

        self.screen.blit(self.menu_image, (0, 0))

    def main_loop(self):

        exit_ = False

        while not exit_:

            self.menu()
            display.flip()

            for event_ in pygame.event.get():  # main events

                if event_.type == QUIT:
                    exit_ = True

                if event_.type == KEYDOWN:

                    if event_.key == K_ESCAPE:
                        exit_ = True

                if event_.type == MOUSEBUTTONDOWN:

                    mixer.music.load(self.error_sound)
                    mixer.music.play()

                    exit_2 = False

                    while not exit_2:

                        StartGame().main_loop()
                        display.flip()

                        for event_2 in pygame.event.get():  # main events

                            if event_2.type == QUIT:
                                exit_ = True

                            if event_2.type == KEYDOWN:

                                if event_2.key == K_ESCAPE:
                                    exit_2 = True

                                if event_2.key == K_DELETE:
                                    sys.exit()


class StartGame:

    def __init__(self):
        self.screen = display.set_mode(SIZE)

        self.windows_error = image.load('./Materials/bsod_2.jpg')
        self.noise = image.load('./Materials/noise_1.png')
        self.noise_sound = './Materials/noise_sound.mp3'

    def level_1(self):

        self.screen.blit(self.windows_error, (0, 0))
        display.flip()

        mouse.set_visible(False)
        time.delay(3000)

        mixer.music.load(self.noise_sound)
        mixer.music.play()

        self.screen.blit(self.noise, (0, 0))
        display.flip()

        time.delay(1000)

        self.loop_2()

    def loop_2(self):

        self.screen.fill((0, 0, 0))
        display.flip()

        time.delay(1000)

        exit_ = False

        while not exit_:

            Typing().main_loop()
            display.flip()

            for event_ in pygame.event.get():  # main events

                if event_.type == QUIT:
                    exit_ = True

                if event_.type == KEYDOWN:

                    if event_.key == K_ESCAPE:
                        exit_ = True

                    if event_.key == K_DELETE:
                        sys.exit()

    def level_2(self):

        self.screen.fill((0, 0, 0))
        # self.screen.blit(self.text, (930, 530))

    def main_loop(self):
        exit_ = False

        while not exit_:

            self.level_1()
            display.flip()

            for event_ in pygame.event.get():  # main events

                if event_.type == QUIT:
                    exit_ = True

                if event_.type == KEYDOWN:

                    if event_.key == K_ESCAPE:
                        exit_ = True

                    if event_.key == K_DELETE:
                        sys.exit()


class Typing:

    def __init__(self):
        self.screen = display.set_mode(SIZE)
        self.font = font.Font('./Materials/Kingthings Trypewriter 2.ttf', 24)

    def play(self):

        '''while Keyboard.Keyboard().keyboard() is not False:
            Keyboard.Keyboard().keyboard()'''

    def main_loop(self):

        text_animation.InfoAnimation().welcome()

        exit_ = False

        while not exit_:

            for event_ in pygame.event.get():  # main events

                if event_.type == QUIT:
                    exit_ = True

                if event_.type == KEYDOWN:

                    if event_.key == K_ESCAPE:
                        exit_ = True

                    if event_.key == K_DELETE:
                        sys.exit()

                    if event_.key == K_LEFT:
                        # self.screen.fill((0, 0, 0))
                        self.play()
                        display.flip()

                    if event_.key == K_RIGHT:
                        text_animation.InfoAnimation().info()
                        display.flip()


if __name__ == '__main__':
    Main().main_loop()
