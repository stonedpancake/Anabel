import sys
from random import randint

import pygame
from pygame import display, font, Color, time, QUIT, KEYDOWN, K_ESCAPE, K_DELETE, mixer
from pygame.constants import K_RIGHT


class InfoAnimation:

    def __init__(self):
        pygame.init()

        self.screen = display.set_mode((1920, 1080))
        self.screen.fill((0, 0, 0))
        self.font = font.Font('./Materials/Kingthings Trypewriter 2.ttf', 24)
        self.typing_sound = './Materials/typing_sound.mp3'

        self.S = self.font.render('S', True, Color('white'))
        self.w = self.font.render('w', True, Color('white'))
        self.e = self.font.render('e', True, Color('white'))
        self.e = self.font.render('e', True, Color('white'))
        self.t = self.font.render('t ', True, Color('white'))

        self.H = self.font.render('H', True, Color('white'))
        self.o = self.font.render('o', True, Color('white'))
        self.u = self.font.render('u', True, Color('white'))
        self.s = self.font.render('s', True, Color('white'))
        self.e = self.font.render('e ', True, Color('white'))

        self.i = self.font.render('i', True, Color('white'))
        self.s = self.font.render('s ', True, Color('white'))

        self.a = self.font.render('a ', True, Color('white'))

        self.g = self.font.render('g', True, Color('white'))
        self.a = self.font.render('a', True, Color('white'))
        self.m = self.font.render('m', True, Color('white'))
        self.e = self.font.render('e ', True, Color('white'))

        self.w = self.font.render('w', True, Color('white'))
        self.i = self.font.render('i', True, Color('white'))
        self.t = self.font.render('t', True, Color('white'))
        self.h = self.font.render('h ', True, Color('white'))

        self.n = self.font.render('n', True, Color('white'))
        self.o = self.font.render('o ', True, Color('white'))

        self.r = self.font.render('r', True, Color('white'))
        self.u = self.font.render('u', True, Color('white'))
        self.l = self.font.render('l', True, Color('white'))
        self.e = self.font.render('e', True, Color('white'))
        self.s = self.font.render('s ', True, Color('white'))

        self.Y = self.font.render('Y', True, Color('white'))
        self.o = self.font.render('o', True, Color('white'))
        self.u = self.font.render('u ', True, Color('white'))

        self.c = self.font.render('c', True, Color('white'))
        self.a = self.font.render('a', True, Color('white'))
        self.n = self.font.render('n', True, Color('white'))
        self.ap = self.font.render("'", True, Color('white'))
        self.t = self.font.render('t ', True, Color('white'))

        self.k = self.font.render('k', True, Color('white'))
        self.n = self.font.render('n', True, Color('white'))
        self.o = self.font.render('o', True, Color('white'))
        self.w = self.font.render('w ', True, Color('white'))

        self.e = self.font.render('e', True, Color('white'))
        self.x = self.font.render('x', True, Color('white'))
        self.a = self.font.render('a', True, Color('white'))
        self.c = self.font.render('c', True, Color('white'))
        self.t = self.font.render('t', True, Color('white'))
        self.l = self.font.render('l', True, Color('white'))
        self.y = self.font.render('y ', True, Color('white'))

        self.w = self.font.render('w', True, Color('white'))
        self.h = self.font.render('h', True, Color('white'))
        self.a = self.font.render('a', True, Color('white'))
        self.t = self.font.render('t ', True, Color('white'))

        self.g = self.font.render('g', True, Color('white'))
        self.o = self.font.render('o', True, Color('white'))
        self.n = self.font.render('n', True, Color('white'))
        self.n = self.font.render('n', True, Color('white'))
        self.a = self.font.render('a ', True, Color('white'))

        self.h = self.font.render('h', True, Color('white'))
        self.a = self.font.render('a', True, Color('white'))
        self.p = self.font.render('p', True, Color('white'))
        self.p = self.font.render('p', True, Color('white'))
        self.e = self.font.render('e', True, Color('white'))
        self.n = self.font.render('n', True, Color('white'))
        self.e = self.font.render('e', True, Color('white'))
        self.d = self.font.render('d', True, Color('white'))

        self.L = self.font.render('L', True, Color('white'))
        self.i = self.font.render('i', True, Color('white'))
        self.k = self.font.render('k', True, Color('white'))
        self.e = self.font.render('e', True, Color('white'))
        self.n = self.font.render('n', True, Color('white'))
        self.o = self.font.render('o', True, Color('white'))
        self.w = self.font.render('w', True, Color('white'))
        self.dot = self.font.render('.', True, Color('white'))

        self.info_text = self.font.render("Sweet House is a game with no rules. You can't know exactly what gonna happened.", True, Color('white'))
        self.like_text = self.font.render("Like now.", True, Color('white'))

    def info(self):

        mixer.music.load(self.typing_sound)
        mixer.music.play()

        self.screen.blit(self.S, (420, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.w, (440, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.e, (460, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.e, (480, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.t, (500, 100))
        time.delay(100)
        display.flip()

        self.screen.blit(self.H, (520, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.o, (540, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.u, (560, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.s, (580, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.e, (600, 100))
        time.delay(100)
        display.flip()

        self.screen.blit(self.i, (620, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.s, (640, 100))
        time.delay(100)
        display.flip()

        self.screen.blit(self.a, (660, 100))
        time.delay(100)
        display.flip()

        self.screen.blit(self.g, (680, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.a, (700, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.m, (720, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.e, (740, 100))
        time.delay(100)
        display.flip()

        self.screen.blit(self.w, (760, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.i, (780, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.t, (800, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.h, (820, 100))
        time.delay(100)
        display.flip()

        self.screen.blit(self.n, (840, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.o, (860, 100))
        time.delay(100)
        display.flip()

        self.screen.blit(self.r, (880, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.u, (900, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.l, (920, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.e, (940, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.s, (960, 100))
        time.delay(100)
        display.flip()

        self.screen.blit(self.Y, (980, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.o, (1000, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.u, (1020, 100))
        time.delay(100)
        display.flip()

        self.screen.blit(self.c, (1040, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.a, (1060, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.n, (1080, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.ap, (1090, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.t, (1100, 100))
        time.delay(100)
        display.flip()

        self.screen.blit(self.k, (1120, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.n, (1140, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.o, (1160, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.w, (1180, 100))
        time.delay(100)
        display.flip()

        self.screen.blit(self.e, (1200, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.x, (1220, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.a, (1240, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.c, (1260, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.t, (1280, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.l, (1300, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.y, (1320, 100))
        time.delay(100)
        display.flip()

        self.screen.blit(self.w, (1340, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.h, (1360, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.a, (1380, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.t, (1400, 100))
        time.delay(100)
        display.flip()

        self.screen.blit(self.g, (1420, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.o, (1440, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.n, (1460, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.n, (1480, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.a, (1500, 100))
        time.delay(100)
        display.flip()

        self.screen.blit(self.h, (1520, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.a, (1540, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.p, (1560, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.p, (1580, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.e, (1600, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.n, (1620, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.e, (1640, 100))
        time.delay(100)
        display.flip()
        self.screen.blit(self.d, (1660, 100))
        display.flip()

        mixer.music.pause()
        time.delay(1000)

        self.like_now()

    def like_now(self):

        mixer.music.play()

        self.screen.blit(self.L, (920, 155))
        time.delay(100)
        display.flip()
        self.screen.blit(self.i, (940, 155))
        time.delay(100)
        display.flip()
        self.screen.blit(self.k, (960, 155))
        time.delay(100)
        display.flip()
        self.screen.blit(self.e, (980, 155))
        time.delay(100)
        display.flip()

        self.screen.blit(self.n, (1020, 155))
        time.delay(100)
        display.flip()
        self.screen.blit(self.o, (1040, 155))
        time.delay(100)
        display.flip()
        self.screen.blit(self.w, (1060, 155))
        time.delay(100)
        display.flip()
        self.screen.blit(self.dot, (1070, 155))
        time.delay(100)
        display.flip()

        mixer.music.stop()

        time.delay(2000)

        self.screen.fill((0, 0, 0))

        self.screen.blit(self.info_text, (420, 100))
        self.screen.blit(self.like_text, (900, 155))

        display.flip()

        time.delay(4000)

        StartDialog().question()


class StartDialog:

    def __init__(self):

        self.screen = display.set_mode((1920, 1080))
        self.screen.fill((0, 0, 0))
        self.font = font.Font('./Materials/Kingthings Trypewriter 2.ttf', 24)
        self.typing_sound = './Materials/typing_sound.mp3'

        self.D = self.font.render('D', True, Color('white'))
        self.o = self.font.render('o', True, Color('white'))

        self.y = self.font.render('y', True, Color('white'))
        self.o = self.font.render('o', True, Color('white'))
        self.u = self.font.render('u', True, Color('white'))

        self.w = self.font.render('w', True, Color('white'))
        self.a = self.font.render('a', True, Color('white'))
        self.n = self.font.render('n', True, Color('white'))
        self.t = self.font.render('t', True, Color('white'))

        self.t = self.font.render('t', True, Color('white'))
        self.o = self.font.render('o', True, Color('white'))

        self.t = self.font.render('t', True, Color('white'))
        self.a = self.font.render('a', True, Color('white'))
        self.l = self.font.render('l', True, Color('white'))
        self.k = self.font.render('k', True, Color('white'))

        self.que = self.font.render('?', True, Color('white'))

        self.Y = self.font.render('Y', True, Color('white'))
        self.e = self.font.render('e', True, Color('white'))
        self.s = self.font.render('s', True, Color('white'))
        self.slash = self.font.render('/', True, Color('white'))
        self.N = self.font.render('N', True, Color('white'))
        self.o = self.font.render('o', True, Color('white'))

        self.talk_que = self.font.render('Do you want to talk?', True, Color('white'))

    def question(self):
        self.screen.blit(self.D, (randint(300, 1700), randint(100, 900)))
        display.flip()
        time.delay(1000)

        self.screen.blit(self.o, (randint(300, 1700), randint(100, 900)))
        display.flip()
        time.delay(1000)

        self.screen.blit(self.y, (randint(300, 1700), randint(100, 900)))
        display.flip()
        time.delay(1000)

        self.screen.blit(self.o, (randint(300, 1700), randint(100, 900)))
        display.flip()
        time.delay(1000)

        self.screen.blit(self.u, (randint(300, 1700), randint(100, 900)))
        display.flip()
        time.delay(1000)

        self.screen.blit(self.w, (randint(300, 1700), randint(100, 900)))
        display.flip()
        time.delay(1000)

        self.screen.blit(self.a, (randint(300, 1700), randint(100, 900)))
        display.flip()
        time.delay(1000)

        self.screen.blit(self.n, (randint(300, 1700), randint(100, 900)))
        display.flip()
        time.delay(1000)

        self.screen.blit(self.t, (randint(300, 1700), randint(100, 900)))
        display.flip()
        time.delay(1000)

        self.screen.blit(self.t, (randint(300, 1700), randint(100, 900)))
        display.flip()
        time.delay(1000)

        self.screen.blit(self.o, (randint(300, 1700), randint(100, 900)))
        display.flip()
        time.delay(1000)

        self.screen.blit(self.t, (randint(300, 1700), randint(100, 900)))
        display.flip()
        time.delay(1000)

        self.screen.blit(self.a, (randint(300, 1700), randint(100, 900)))
        display.flip()
        time.delay(1000)

        self.screen.blit(self.l, (randint(300, 1700), randint(100, 900)))
        display.flip()
        time.delay(1000)

        self.screen.blit(self.k, (randint(300, 1700), randint(100, 900)))
        display.flip()
        time.delay(1000)

        self.screen.blit(self.que, (randint(300, 1700), randint(100, 900)))
        display.flip()

        time.delay(2500)

        self.answer_text()

    def answer_text(self):
        self.screen.fill((0, 0, 0))

        self.screen.blit(self.talk_que, (820, 510))
        display.flip()
        time.delay(1000)

        self.screen.blit(self.Y, (900, 540))
        display.flip()
        time.delay(1000)

        self.screen.blit(self.e, (920, 540))
        display.flip()
        time.delay(1000)

        self.screen.blit(self.s, (940, 540))
        display.flip()
        time.delay(1000)

        self.screen.blit(self.slash, (960, 540))
        display.flip()
        time.delay(1000)

        self.screen.blit(self.N, (980, 540))
        display.flip()
        time.delay(1000)

        self.screen.blit(self.o, (1000, 540))
        display.flip()
        time.delay(1000)


class Dialog:

    def __init__(self):
        self.screen = display.set_mode((1920, 1080))
        self.screen.fill((0, 0, 0))
        self.font = font.Font('./Materials/Kingthings Trypewriter 2.ttf', 24)
        self.typing_sound = './Materials/typing_sound.mp3'


class Keyboard(Dialog):

    def __init__(self):
        super().__init__()

        for event_ in pygame.event.get():

            if event_.type == KEYDOWN:

                if event_.key == K_RIGHT:
                    pass
