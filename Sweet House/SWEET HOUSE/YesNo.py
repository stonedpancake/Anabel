import sys

import pygame
from pygame import display, time, Color, font
from pygame.constants import QUIT, KEYDOWN, K_RIGHT, K_LEFT, K_ESCAPE, K_DELETE


class YesNo:

    def __init__(self, que):

        self.screen = display.set_mode((1920, 1080))
        self.font = font.Font('./Materials/Kingthings Trypewriter 2.ttf', 24)

        self.que = self.font.render(f'{que}?', True, Color('white'))
        self.yes_no = self.font.render(f'Yes/No', True, Color('white'))

        # центрирование по длине

        self.que_pos = None

    def text(self):

        self.screen.fill((0, 0, 0))

        time.delay(1500)

        self.screen.blit(self.que, (840, 510))
        display.flip()
        time.delay(1000)

        self.screen.blit(self.yes_no, (900, 540))
        display.flip()
        time.delay(1000)

        return self.wait_answer()

    def wait_answer(self):

        while True:

            for event_ in pygame.event.get():

                if event_.type == QUIT:
                    return None

                if event_.type == KEYDOWN:

                    if event_.key == K_ESCAPE:
                        return None

                    if event_.key == K_DELETE:
                        sys.exit()

                    if event_.key == K_RIGHT:
                        return False

                    if event_.key == K_LEFT:
                        return True
