#!/usr/bin/env python

import sys
import pygame
from pygame.locals import *
from PyDimitri import Dimitri

COLS = 20
ROWS = 27

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
                'RIGHT_LOWER_LEG':12, \
                'RIGHT_FOOT_PITCH' : 13, \
                'LEFT_FOOT_PITCH' : 14, \
                'LEFT_LOWER_LEG_SEA' : 111, \
                'RIGHT_LOWER_LEG_SEA' : 112, \
                'LEFT_UPPER_LEG_SEA' : 113, \
                'RIGHT_UPPER_LEG_SEA' : 114, \
                'LEFT_LEG_ROLL' : 23, \
                'RIGHT_LEG_ROLL' : 24, \
                'LEFT_LEG_PITCH' : 25, \
                'RIGHT_LEG_PITCH' : 26, \
                'LEFT_LEG_YAW' : 27, \
                'RIGHT_LEG_YAW' : 28, \
                'LEFT_ARM_ROLL' : 31, \
                'RIGHT_ARM_ROLL' : 32, \
                'LEFT_ARM_PITCH' : 33, \
                'RIGHT_ARM_PITCH' : 34, \
                'LEFT_ARM_YAW' : 35, \
                'RIGHT_ARM_YAW' : 36, \
                'LEFT_ELBOW' : 41, \
                'RIGHT_ELBOW' : 42, \
                'WAIST_ROLL': 51, \
                'WAIST_PITCH' : 52, \
                'WAIST_YAW' : 53, \
                'NECK_PITCH' : 61, \
                'NECK_YAW' : 62 \
                }
        self.inv_joints = {v: k for k, v in self.joints.items()}
        self.cursor = (0,0)
    def mainLoop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        c,r = self.cursor
                        r = (r - 1) % ROWS
                        self.cursor = c,r
                    elif event.key == pygame.K_DOWN:
                        c,r = self.cursor
                        r = (r + 1) % ROWS
                        self.cursor = c,r
                    elif event.key == pygame.K_LEFT:
                        c,r = self.cursor
                        c = (c - 1) % COLS
                        self.cursor = c,r
                    elif event.key == pygame.K_RIGHT:
                        c,r = self.cursor
                        c = (c + 1) % COLS
                        self.cursor = c,r
            self.display()
    def display(self):
        self.screen.fill((0,0,0))
        normal_color = (127,127,127)
        highlight_color = (255,255,255)
        c,r = self.cursor
        for i,joint in enumerate(self.inv_joints.keys()):
            if i == r:
                color = highlight_color
            else:
                color = normal_color
            self.printText(str(joint)+' '+self.inv_joints[joint], (5,25+15*i), color)
        for i in range(20):
            if i == c:
                color = highlight_color
            else:
                color = normal_color
            self.printText(str(i), (200+40*i,5), color)
        pygame.display.flip()
    def printText(self, text, pos, color=(255,255,255)):
        textSurface = self.font.render(text, 1, color)
        rect = textSurface.get_rect()
        rect.x, rect.y = pos
        self.screen.blit(textSurface, rect)

if __name__ == "__main__":
    app = motionEditor()
    app.mainLoop()


