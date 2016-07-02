#!/usr/bin/env python

import sys, os
import pygame
from pygame.locals import *
from PyDimitri import Dimitri, Motion
from PyDimitri.PyDynamixel import Joint
from copy import deepcopy
from math import pi

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
        self.step = 20
        self.joints = { \
                'RIGHT_FOOT_ROLL':11, \
                'LEFT_FOOT_ROLL':11, \
                'RIGHT_FOOT_PITCH' : 13, \
                'LEFT_FOOT_PITCH' : 14, \
		'RIGHT_LOWER_LEG' : 15, \
		'LEFT_LOWER_LEG' : 16, \
		'RIGHT_UPPER_LEG' : 21, \
		'LEFT_UPPER_LEG' : 22, \
                'RIGHT_LEG_ROLL' : 23, \
                'LEFT_LEG_ROLL' : 24, \
                'RIGHT_LEG_PITCH' : 25, \
                'LEFT_LEG_PITCH' : 26, \
                'RIGHT_LEG_YAW' : 27, \
                'LEFT_LEG_YAW' : 28, \
                'RIGHT_ARM_ROLL' : 31, \
                'LEFT_ARM_ROLL' : 32, \
                'RIGHT_ARM_PITCH' : 33, \
                'LEFT_ARM_PITCH' : 34, \
                'RIGHT_ARM_YAW' : 35, \
                'LEFT_ARM_YAW' : 36, \
                'RIGHT_ELBOW' : 41, \
                'LEFT_ELBOW' : 42, \
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
        self.motion = Motion()
        if os.path.isfile(filename):
            self.motion.read(filename)
        else:
            self.motion.keyframes.append({i:0.0 for i in self.inv_joints.keys()})


    def playMotion(self):
        #ToDo: implement later
        pass

    def readFromServo(self, servoID):
        angle = Dimitri.joints[servoID].receiveCurrAngle()
        print angle
        return angle
        #return Joint.receiveAngle()

    def mainLoop(self):

        def getRow(r):
            return self.inv_joints.keys()[r]

        def outOfBounds(col):
            return (len(self.motion.keyframes) <= col)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    c,r = self.cursor
                    joint_id = getRow(r)
                    if event.key == pygame.K_UP:
                        r = (r - 1) % ROWS
                        self.cursor = c,r
                    elif event.key == pygame.K_DOWN:
                        r = (r + 1) % ROWS
                        self.cursor = c,r
                    elif event.key == pygame.K_LEFT:
                        c = (c - 1) % COLS
                        self.cursor = c,r
                    elif event.key == pygame.K_RIGHT:
                        c = (c + 1) % COLS
                        self.cursor = c,r
                    elif event.key == pygame.K_F10:
                        self.motion.save(self.filename)


                    #calls jesus' help and saves
                    elif event.key == pygame.K_RETURN:
                        curr = len(self.motion.keyframes)-1
                        while len(self.motion.keyframes) <= c:
                            self.motion.keyframes.append(deepcopy(self.motion.keyframes[-1]))
                        for i in range(curr, c):
                            #0 = frame time.
                            self.motion.keyframes[i+1][0] = 20* self.motion.period + self.motion.keyframes[i][0]

                    #exits the editor
                    elif event.key == pygame.K_ESCAPE:
                        sys.exit()

                    #Press "z" to put angle from servo on current position
                    elif event.key == pygame.K_z:
                        self.motion.keyframes[c][joint_id] = self.readFromServo(joint_id)

                    elif event.key == pygame.K_p:
                        self.playMotion()

                    if not outOfBounds(c):
                        #increment / decrement part
                        if event.key == pygame.K_q:
                            self.motion.keyframes[c][joint_id] += 100.0
                        elif event.key == pygame.K_a:
                            self.motion.keyframes[c][joint_id] -= 100
                        elif event.key == pygame.K_w:
                            self.motion.keyframes[c][joint_id] += 10
                        elif event.key == pygame.K_s:
                            self.motion.keyframes[c][joint_id] -= 10
                        elif event.key == pygame.K_e:
                            self.motion.keyframes[c][joint_id] += 1
                        elif event.key == pygame.K_d:
                            self.motion.keyframes[c][joint_id] -= 1

                        # hit backspace to delete current frame
                        elif event.key == pygame.K_BACKSPACE:
                            if len(self.motion.keyframes) is not 1:
                                self.motion.keyframes.__delitem__(c)
                                for i in range(len(self.motion.keyframes)):
                                    self.motion.keyframes[i][0] = i * self.motion.period *self.step
                                if(outOfBounds(c)):
                                    self.cursor = c-1, r
                            else:
                                #try to put all content of array to 0
                                for a in range(253):
                                    try:
                                        self.motion.keyframes[c][a] = 0.0
                                    except IndexError:
                                        print 'Index not in array'


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
                try:
                  joint_id = joint_ids[j]
                except IndexError:
                  pass
	        self.printText('%3.0f' % (180*self.motion.keyframes[i][joint_id]/pi), (200+40*i,25+15*j), color)
        pygame.display.flip()
    def printText(self, text, pos, color=(255,255,255)):
        textSurface = self.font.render(text, 1, color)
        rect = textSurface.get_rect()
        rect.x, rect.y = pos
        self.screen.blit(textSurface, rect)

if __name__ == "__main__":
    app = motionEditor(sys.argv[1])
    app.mainLoop()
