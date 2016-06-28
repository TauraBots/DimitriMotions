#!/usr/bin/env python

import sys
import pygame
from pygame.locals import *
from PyDimitri import Dimitri

class motionEditor(object):
    ''' Simple motion editor for Dimitri
    motions.
    '''
    def __init__(self):
        pygame.init()
        self.width = 1024
        self.height = 768
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.dimitri = Dimitri()
        self.font = pygame.font.Font(None, 38)
        self.joints = { \
                'LEFT_FOOT_ROLL':11, \
                'RIGHT_LOWER_LEG':12
                }
    def mainLoop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.display()
    def display(self):
        self.screen.fill((0,0,0))
        self.printText("Test", (5,5))
        pygame.display.flip()
    def printText(self, text, pos, color=(255,255,255)):
        textSurface = self.font.render(text, 1, color)
        rect = textSurface.get_rect()
        rect.x, rect.y = pos
        self.screen.blit(textSurface, rect)

if __name__ == "__main__":
    app = motionEditor()
    app.mainLoop()

