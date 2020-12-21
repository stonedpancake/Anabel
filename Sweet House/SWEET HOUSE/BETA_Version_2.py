import sys
import pygame
import pygame_gui
from pygame import *
from pygame_gui import *
from pygame.image import *
import text_animation

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
        self.typing_sound = './Materials/typing_sound.mp3'

        self.w = self.font.render('w', True, Color('white'))
        self.e = self.font.render('e', True, Color('white'))
        self.l = self.font.render('l', True, Color('white'))
        self.c = self.font.render('c', True, Color('white'))
        self.o = self.font.render('o', True, Color('white'))
        self.m = self.font.render('m', True, Color('white'))
        self.e = self.font.render('e', True, Color('white'))

        self.p = self.font.render('p', True, Color('white'))
        self.l = self.font.render('l', True, Color('white'))
        self.a = self.font.render('a', True, Color('white'))
        self.y = self.font.render('y', True, Color('white'))

        self.slash = self.font.render('/', True, Color('white'))

        self.i = self.font.render('i', True, Color('white'))
        self.n = self.font.render('n', True, Color('white'))
        self.f = self.font.render('f', True, Color('white'))
        self.o = self.font.render('o', True, Color('white'))

        self.info_text = self.font.render("Sweet House is a game with no rules. You can't know exactly what gonna happened.",
                                          True, Color('white'))

    def welcome(self):

        mixer.music.load(self.typing_sound)
        mixer.music.play()

        self.screen.blit(self.w, (930, 530))
        display.flip()
        time.delay(400)

        self.screen.blit(self.e, (950, 530))
        display.flip()
        time.delay(400)

        self.screen.blit(self.l, (970, 530))
        display.flip()
        time.delay(400)

        self.screen.blit(self.c, (990, 530))
        display.flip()
        time.delay(400)

        self.screen.blit(self.o, (1010, 530))
        display.flip()
        time.delay(400)

        self.screen.blit(self.m, (1030, 530))
        display.flip()
        time.delay(400)

        self.screen.blit(self.e, (1050, 530))
        display.flip()
        time.delay(400)

        self.text_play()

    def text_play(self):

        self.screen.blit(self.p, (900, 580))
        display.flip()
        time.delay(400)

        self.screen.blit(self.l, (920, 580))
        display.flip()
        time.delay(400)

        self.screen.blit(self.a, (940, 580))
        display.flip()
        time.delay(400)

        self.screen.blit(self.y, (960, 580))
        display.flip()
        time.delay(400)

        self.text_info()

    def text_info(self):

        self.screen.blit(self.slash, (1000, 580))
        display.flip()
        time.delay(400)

        self.screen.blit(self.i, (1040, 580))
        display.flip()
        time.delay(400)

        self.screen.blit(self.n, (1060, 580))
        display.flip()
        time.delay(400)

        self.screen.blit(self.f, (1080, 580))
        display.flip()
        time.delay(400)

        self.screen.blit(self.o, (1100, 580))
        display.flip()

        mixer.music.stop()

        self.loop()

    def play(self):
        pass

    def info(self):

        text_animation.InfoAnimation().main_loop()

    def loop(self):

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
                        self.play()
                        display.flip()

                    if event_.key == K_RIGHT:
                        self.info()
                        display.flip()

    def main_loop(self):
        exit_ = False

        while not exit_:

            self.welcome()
            display.flip()

            for event_ in pygame.event.get():  # main events

                if event_.type == QUIT:
                    exit_ = True

                if event_.type == KEYDOWN:

                    if event_.key == K_ESCAPE:
                        exit_ = True

                    if event_.key == K_DELETE:
                        sys.exit()


if __name__ == '__main__':
    Main().main_loop()
