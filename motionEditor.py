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
                'RIGHT_LOWER_LEG':12 \
                'RIGHT_FOOT_PITCH' : 13 \
                'LEFT_FOOT_PITCH' : 14 \
                'LEFT_LOWER_LEG_SEA' : 111 \
                'RIGHT_LOWER_LEG_SEA' : 112 \
                'LEFT_UPPER_LEG_SEA' : 113 \
                'RIGHT_UPPER_LEG_SEA' : 114 \
                'LEFT_LEG_ROLL' : 23\
                'RIGHT_LEG_ROLL' : 24 \
                'LEFT_LEG_PITCH' : 25 \
                'RIGHT_LEG_PITCH' : 26 \
                'LEFT_LEG_YAW' : 27 \
                'RIGHT_LEG_YAW' : 28 \
                'LEFT_ARM_ROLL' : 31 \
                'RIGHT_ARM_ROLL' : 32 \
                'LEFT_ARM_PITCH' : 33 \
                'RIGHT_ARM_PITCH' : 34 \
                'LEFT_ARM_YAW' : 35 \
                'RIGHT_ARM_YAW' : 36 \
                'LEFT_ELBOW' : 41 \
                'RIGHT_ELBOW' : 42 \
                'WAIST_ROLL': 51 \
                'WAIST_PITCH' : 52 \
                'WAIST_YAW' : 53 \
                'NECK_PITCH' : 61 \
                'NECK_YAW' : 62 \
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


