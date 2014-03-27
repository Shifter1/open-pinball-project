#!/usr/bin/env python
#
#===============================================================================
#
#                         OOOO
#                       OOOOOOOO
#      PPPPPPPPPPPPP   OOO    OOO   PPPPPPPPPPPPP
#    PPPPPPPPPPPPPP   OOO      OOO   PPPPPPPPPPPPPP
#   PPP         PPP   OOO      OOO   PPP         PPP
#  PPP          PPP   OOO      OOO   PPP          PPP
#  PPP          PPP   OOO      OOO   PPP          PPP
#  PPP          PPP   OOO      OOO   PPP          PPP
#   PPP         PPP   OOO      OOO   PPP         PPP
#    PPPPPPPPPPPPPP   OOO      OOO   PPPPPPPPPPPPPP
#     PPPPPPPPPPPPP   OOO      OOO   PPP
#               PPP   OOO      OOO   PPP
#               PPP   OOO      OOO   PPP
#               PPP   OOO      OOO   PPP
#               PPP    OOO    OOO    PPP
#               PPP     OOOOOOOO     PPP
#              PPPPP      OOOO      PPPPP
#
# @file:   dispThread.py
# @author: Hugh Spahr
# @date:   1/18/2014
#
# @note:   Open Pinball Project
#          Copyright 2014, Hugh Spahr
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#===============================================================================
#
# This is the display thread file that is used to display scores, GI lighting,
# and feature lights
#
#===============================================================================

vers = '00.00.02'

import thread
import pygame
from pygame.locals import *
from rulesData import RulesData
import dispConstIntf
import dispIntf
import errIntf

updDispList = []
updFeatList = []
updGiState = dispConstIntf.LGHT_ON
sndPlyr = []

#Positions for score
#xPos = array('i',[])
#yPos = array('i',[])
xPos = []
yPos = []
clearRect = []

#Positions for simulated lights
featureSimLghtPos = []
featOn = []
clearFeatRect = []
giSimLghtPos = []
clearGiRect = []

simRatio = 1.0
simWidth = 0
simHeight = 0
simLghtRadius = 0
runDispThread = True

orangeColor = (255, 131, 0)
whiteColor = (255, 255, 255)

def updateDisp(player, value, blank):
    global digiFont
    global screen
    global background
    
    screen.blit(background, clearRect[player], clearRect[player])
    if (not blank):
        text = digiFont.render(str(value), 1, orangeColor)
        textpos = text.get_rect()
        textpos.midright = xPos[player], yPos[player]
        screen.blit(text, textpos)
    pygame.display.update(clearRect[player])

def createSndPlyr():
    global sndPlyr
    
    for fileName in RulesData.SND_FILES:
        sndPlyr.append(pygame.mixer.Sound(fileName))

def updateFeatLight(num, state):
    global screen
    global simLghtRadius
    global background
    
    if (num < len(featOn)):
        if (state == dispConstIntf.LGHT_ON) or ((state == dispConstIntf.LGHT_TOGGLE) and (not featOn[num])):
            pygame.draw.circle(screen, whiteColor, (featureSimLghtPos[num][0], featureSimLghtPos[num][1]), simLghtRadius)
            featOn[num] = True
        else:
            screen.blit(background, clearFeatRect[num], clearFeatRect[num])
            featOn[num] = False
        pygame.display.update(clearFeatRect[num])

def giLightOn(on):
    global screen
    global simLghtRadius
    global background
    
    if on:
        for tmpLghtPos in giSimLghtPos:
            pygame.draw.circle(screen, whiteColor, (tmpLghtPos[0], tmpLghtPos[1]), simLghtRadius)
    else:
        for tmpLghtRect in clearGiRect:
            screen.blit(background, tmpLghtRect, tmpLghtRect)
    for tmpLghtRect in clearGiRect:
        pygame.display.update(tmpLghtRect)

def playSound(num):
    global sndPlyr
    
    if (num < len(sndPlyr)):
        sndPlyr[num].play()

#Init score displays.  Figures out the size and sets up the clear rects
#to update the displays
def initScoreDisps():
    global digiFont
    global simWidth
    global simHeight
    
    #Make screen HD ratio, video will take up 80% of height/width
    hdRatio = 1920.0/1080.0
    simHeight = int((simWidth/hdRatio) + .5)
    videoRatio = .8
    vidHeight = int((simHeight * videoRatio) + .5)
    vidWidth = int((simWidth * videoRatio) + .5)

    #Check if the requested size can be displayed
    pygame.init()
    infoObject = pygame.display.Info()
    if (simWidth > infoObject.current_w) or (simHeight > infoObject.current_h):
        print "Screen size: %d x %d not supported" % (simWidth, simHeight)
        return(errIntf.BAD_SCREEN_SIZE)

    #Figure out size of score boxes
    plyrScoreHeight = int(((simHeight - vidHeight)/2.0) + .5)
    creditWidth = 2 * plyrScoreHeight
    plyrScoreWidth = int(((simWidth - creditWidth)/2.0) + .5)

    #Calculate y position of rows
    yPosRow1 = vidHeight + int((plyrScoreHeight/2.0) + .5)
    yPosRow2 = yPosRow1 + plyrScoreHeight

    #Calculate x position of player/credit
    xPosCol1 = int((plyrScoreWidth/2.0) + .5)
    xPosCol2 = int((simWidth/2.0) + .5)
    xPosCol3 = plyrScoreWidth + creditWidth + xPosCol1

    #Optimize font size to height to plyrScoreHeight
    fontHeightGoal = int((plyrScoreHeight * .8) + .5)
    fontSize = 10
    fontHeight = 0
    while (fontHeight < fontHeightGoal):
        fontSize += 1
        digiFont = pygame.font.Font("font/digitalFont.ttf", fontSize)
        text = digiFont.render("0", 1, (10, 10, 10))
        fontHeight = text.get_height()
      
    #Figure out the player score width, create position arrays
    text = digiFont.render("8888888888", 1, orangeColor)
    scoreWidth = text.get_width()
    scoreHeight = text.get_height()

    #Player 1
    yPos.append(yPosRow1)
    xPos.append(xPosCol1 + int((text.get_width()/2.0) + .5))

    #Player 2
    yPos.append(yPosRow1)
    xPos.append(xPosCol3 + int((text.get_width()/2.0) + .5))

    #Player 3
    yPos.append(yPosRow2)
    xPos.append(xPosCol1 + int((text.get_width()/2.0) + .5))

    #Player 4
    yPos.append(yPosRow2)
    xPos.append(xPosCol3 + int((text.get_width()/2.0) + .5))

    #Create clear rect for player displays
    for index in range(0,4):
        tmpRect = pygame.Rect(0, 0, scoreWidth, scoreHeight)
        tmpRect.midright = xPos[index], yPos[index]
        clearRect.append(tmpRect)

    #Active Player, single digit
    text = digiFont.render("8", 1, orangeColor)
    yPos.append(yPosRow1)
    xPos.append(xPosCol2 + int((text.get_width()/2.0) + .5))

    #Credits/Ball Num, two digits
    text = digiFont.render("88", 1, orangeColor)
    yPos.append(yPosRow2)
    xPos.append(xPosCol2 + int((text.get_width()/2.0) + .5))
    creditWidth = text.get_width()
    creditHeight = text.get_height()

    #Create clear rect for other displays
    tmpRect = pygame.Rect(0, 0, creditWidth, creditHeight)
    tmpRect.midright = xPos[4], yPos[4]
    clearRect.append(tmpRect)
    tmpRect = pygame.Rect(0, 0, creditWidth, creditHeight)
    tmpRect.midright = xPos[5], yPos[5]
    clearRect.append(tmpRect)

#Init feature lights.  Figures out the size and sets up the clear rects
#to update the feature lights
def initFeatureLights():
    global simLghtRadius
    global simRatio
    
    simLghtRadius = int((float(RulesData.LGHT_RADIUS) * simRatio) + .5)
    for tmpLghtPos in RulesData.FEATURE_LGHT_POS:
        tmpLghtXPos = int((float(tmpLghtPos[0]) * simRatio) + .5)
        tmpLghtYPos = int((float(tmpLghtPos[1]) * simRatio) + .5)
        featureSimLghtPos.append((tmpLghtXPos, tmpLghtYPos))
        featOn.append(False)
        tmpRect = pygame.Rect(tmpLghtXPos - simLghtRadius, tmpLghtYPos - simLghtRadius, simLghtRadius * 2, simLghtRadius * 2)
        clearFeatRect.append(tmpRect)

#Init general illumination lights.  Figures out the size and sets up the clear rects
#to update the general illumination lights
def initGenIllumLights():
    global simLghtRadius
    global simRatio
    
    simLghtRadius = int((float(RulesData.LGHT_RADIUS) * simRatio) + .5)
    for tmpLghtPos in RulesData.GI_LGHT_POS:
        tmpLghtXPos = int((float(tmpLghtPos[0]) * simRatio) + .5)
        tmpLghtYPos = int((float(tmpLghtPos[1]) * simRatio) + .5)
        giSimLghtPos.append((tmpLghtXPos, tmpLghtYPos))
        tmpRect = pygame.Rect(tmpLghtXPos - simLghtRadius, tmpLghtYPos - simLghtRadius, simLghtRadius * 2, simLghtRadius * 2)
        clearGiRect.append(tmpRect)

#Create the display screen
def createScreen(mode):
    global screen
    global simWidth
    global simHeight
    global background

    print "simWidth, simHeight:  %d, %d" % (simWidth, simHeight)
    screen=pygame.display.set_mode((simWidth, simHeight),mode, 24)
    clock = pygame.time.Clock()

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    # Show score positions
    text = digiFont.render("8888888888", 1, orangeColor)
    for index in range(0,4):
        textpos = text.get_rect()
        textpos.midright = xPos[index], yPos[index]
        screen.blit(text, textpos)

    # Show player/credit positions
    text = digiFont.render("8", 1, orangeColor)
    textpos = text.get_rect()
    textpos.midright = xPos[dispConstIntf.DISP_PLAYER_NUM], yPos[dispConstIntf.DISP_PLAYER_NUM]
    screen.blit(text, textpos)
    text = digiFont.render("88", 1, orangeColor)
    textpos = text.get_rect()
    textpos.midright = xPos[dispConstIntf.DISP_CREDIT_BALL_NUM], yPos[dispConstIntf.DISP_CREDIT_BALL_NUM]
    screen.blit(text, textpos)

    #Show screen
    pygame.display.update()

    # run the game loop
    score = [0, 0, 0, 0]

    #Playing a sound
    pygame.mixer.init()
    createSndPlyr()
    giLightOn(True)

#Init display
def init(passedSimWidth, actWidth, fullScr):
    global simWidth
    global simRatio

    simWidth = passedSimWidth
    mode = pygame.NOFRAME
    if fullScr:
        mode |= pygame.FULLSCREEN
    simRatio = float(simWidth)/float(actWidth)
    pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag

    initScoreDisps()
    initFeatureLights()
    initGenIllumLights()
    createScreen(mode)
    return(errIntf.CMD_OK)

def start():
    thread.start_new_thread(dispThread, ("Disp Thread",))

def dispExit():
    global runDispThread
    
    runDispThread = False

def dispThread(unused):
    global runDispThread
    global updDispList
    global updFeatList
    
    clock = pygame.time.Clock()
    while runDispThread:
        for tmpUpdDisp in updDispList:
            updateDisp(tmpUpdDisp[0], tmpUpdDisp[1], tmpUpdDisp[2])
        updDispList = []
        for tmpUpdFeat in updFeatList:
            updateFeatLight(tmpUpdFeat[0], tmpUpdFeat[1])
        updFeatList = []
        #Disp thread processing
        clock.tick(100)
