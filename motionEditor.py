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
        self.font = pygame.font.Font(None, 18)
        self.joints = { \
                'LEFT_FOOT_ROLL':11, \
                'RIGHT_LOWER_LEG':12
                }
        self.cursor = (0,0)
    def mainLoop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.display()
    def display(self):
        self.screen.fill((0,0,0))
        for i,joint in enumerate(self.joints.keys()):
            self.printText(str(self.joints[joint])+' '+joint, (5,25+15*i))
        for i in range(20):
            self.printText(str(i), (200+40*i,5))
        pygame.display.flip()
    def printText(self, text, pos, color=(255,255,255)):
        textSurface = self.font.render(text, 1, color)
        rect = textSurface.get_rect()
        rect.x, rect.y = pos
        self.screen.blit(textSurface, rect)

if __name__ == "__main__":
    app = motionEditor()
    app.mainLoop()

