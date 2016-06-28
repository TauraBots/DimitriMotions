#!/usr/bin/env python

import sys, os
import pygame
from pygame.locals import *
from PyDimitri import Dimitri
from motion import motion
from copy import deepcopy

COLS = 20
ROWS = 28

class motionEditor(object):
    ''' Simple motion editor for Dimitri
    motions.
    '''
    def __init__(self, filename):
        pygame.init()
        self.width = 1024
        self.height = 500
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
                'NECK_YAW' : 62, \
                'DURATION' : 0 \
                }
        self.inv_joints = {v: k for k, v in self.joints.items()}
        self.cursor = (0,0)
        self.filename = filename
        self.motion = motion()
        if os.path.isfile(filename):
            self.motion.read(filename)
        else:
            self.motion.keyframes.append({i:0.0 for i in self.inv_joints.keys()})
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
                    elif event.key == pygame.K_F10:
                        self.motion.save(self.filename)
                    elif event.key == pygame.K_RETURN:
                        c,r = self.cursor
                        while len(self.motion.keyframes) <= c:
                            self.motion.keyframes.append(deepcopy(self.motion.keyframes[-1]))
                    elif event.key == pygame.K_q:
                        joint_id = self.inv_joints.keys()[r]
                        self.motion.keyframes[c][joint_id] += 100.0
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
        for i in range(COLS):
            if i == c:
                color = highlight_color
            else:
                color = normal_color
            self.printText(str(i), (200+40*i,5), color)
            joint_ids = self.inv_joints.keys()
            if i < len(self.motion.keyframes):
                for j in range(ROWS):
                    if i == c and j == r:
                        color = highlight_color
                    else:
                        color = normal_color
                    joint_id = joint_ids[j]
                    self.printText(str(self.motion.keyframes[i][joint_id]), (200+40*i,25+15*j), color)
        pygame.display.flip()
    def printText(self, text, pos, color=(255,255,255)):
        textSurface = self.font.render(text, 1, color)
        rect = textSurface.get_rect()
        rect.x, rect.y = pos
        self.screen.blit(textSurface, rect)

if __name__ == "__main__":
    app = motionEditor(sys.argv[1])
    app.mainLoop()


