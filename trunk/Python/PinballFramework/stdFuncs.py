#!/usr/bin/env python
#
#===============================================================================
#
#                           OOOO
#                         OOOOOOOO
#        PPPPPPPPPPPPP   OOO    OOO   PPPPPPPPPPPPP
#      PPPPPPPPPPPPPP   OOO      OOO   PPPPPPPPPPPPPP
#     PPP         PPP   OOO      OOO   PPP         PPP
#    PPP          PPP   OOO      OOO   PPP          PPP
#    PPP          PPP   OOO      OOO   PPP          PPP
#    PPP          PPP   OOO      OOO   PPP          PPP
#     PPP         PPP   OOO      OOO   PPP         PPP
#      PPPPPPPPPPPPPP   OOO      OOO   PPPPPPPPPPPPPP
#       PPPPPPPPPPPPP   OOO      OOO   PPP
#                 PPP   OOO      OOO   PPP
#                 PPP   OOO      OOO   PPP
#                 PPP   OOO      OOO   PPP
#                 PPP    OOO    OOO    PPP
#                 PPP     OOOOOOOO     PPP
#                PPPPP      OOOO      PPPPP
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
##
# @file    stdFuncs.py
# @author  Hugh Spahr
# @date    4/19/2014
#
# @note    Open Pinball Project
# @note    Copyright 2014, Hugh Spahr
#
# @brief These are the standard functions for the pinball framework.

#===============================================================================

from gameData import GameData
from hwobjs.ledBrd import LedBrd
from rules.rulesData import RulesData
from dispConstIntf import DispConst

## Standard functions class.
#
#  Class that holds all the standard functions.
class StdFuncs():
    
    ## Check input bit
    #
    #  Check if a bit from an input card is currently set.
    #
    #  @param  self          [in]   Object reference
    #  @param  cardBitPos    [in]   input card index and bit position
    #  @return True if set 
    def CheckInpBit(self, cardBitPos):
        cardNum = (cardBitPos >> 16) & 0xf
        bitPos = cardBitPos & 0xffff
        if ((GameData.currInpStatus[cardNum] & bitPos) != 0):
            return True
        else:
            return False

    ## Check solenoid bit
    #
    #  Check if a bit from a solenoid card is currently set.
    #
    #  @param  self          [in]   Object reference
    #  @param  cardBitPos    [in]   solenoid card index and bit position
    #  @return True if set 
    def CheckSolBit(self, cardBitPos):
        cardNum = (cardBitPos >> 16) & 0xf
        bitPos = cardBitPos & 0xffff
        if ((GameData.currSolStatus[cardNum] & bitPos) != 0):
            return True
        else:
            return False

    ## Check LED bit
    #
    #  Check if an LED bit is set.
    #
    #  @param  self          [in]   Object reference
    #  @param  cardBitPos    [in]   LED card index and bit position
    #  @return True if set 
    def CheckLedBit(self, cardBitPos):
        cardNum = (cardBitPos >> 16) & 0xf
        bitPos = cardBitPos & 0xffff
        if ((LedBrd.currLedData[cardNum] & bitPos) != 0):
            return True
        else:
            return False

    ## Disable solenoids
    #
    #  Send a command to disable the solenoids
    #
    #  @param  self          [in]   Object reference
    #  @return None 
    def Disable_Solenoids(self):
        #HRS:  Finish
        pass
    
    ## Enable solenoids
    #
    #  Send a command to enable the solenoids
    #
    #  @param  self          [in]   Object reference
    #  @return None 
    def Enable_Solenoids(self):
        #HRS:  Finish
        pass
    
    ## Kick solenoid
    #
    #  Send a command to kick a solenoid
    #
    #  @param  self          [in]   Object reference
    #  @param  cardBitPos    [in]   solenoid card index and bit position
    #  @return None 
    def Kick(self, cardBitPos):
        #HRS:  Finish
        pass

    ## Start a timer
    #
    #  Start a timer
    #
    #  @param  self          [in]   Object reference
    #  @param  timeout       [in]   bit position of the timer
    #  @return None 
    def Start(self, timeout):
        #HRS:  Finish
        pass
    
    ## Check for expired timeout
    #
    #  Look if expired timeout bit is set
    #
    #  @param  self          [in]   Object reference
    #  @param  timeout       [in]   bit position of the timer
    #  @return True if expired 
    def Expired(self, timeout):
        if ((GameData.expiredTimers & timeout) != 0):
            return True
        else:
            return False
    
    ## Rotate LED left
    #
    #  Rotate a group of LEDs to the left.
    #
    #  @param  self          [in]   Object reference
    #  @param  rotMask       [in]   Card number and mask of LEDs to rotate
    #  @return True if set
    #  @note The LEDs must be contiguous and not span cards
    def Led_Rot_Left(self, rotMask):
        #Currently rotated bits must be next to each other and on same card
        cardNum = (rotMask >> 16) & 0xf
        index = 0
        firstBit = 0
        lastBit = 0
        foundFirstBit = False
        foundLastBit = False
        while ((index < 8) and (foundLastBit == False)):
            if (((1 << index) & rotMask) != 0):
                if not foundFirstBit:
                    firstBit = index
                    foundFirstBit = True
            else:
                if foundFirstBit:
                    lastBit = index
                    foundLastBit = True
            index += 1
        if (foundFirstBit and foundLastBit):
            tmpLed = LedBrd.currLedData[cardNum] << 1
            if ((tmpLed & (1 << lastBit)) != 0):
                tmpLed |= (1 << firstBit)
            tmpLed &= rotMask
            LedBrd.currLedData[cardNum] = (LedBrd.currLedData[cardNum] & ~rotMask) | tmpLed

    ## Rotate variable left
    #
    #  Rotate a variable to the left.
    #
    #  @param  self          [in]   Object reference
    #  @param  rotMask       [in]   Mask to rotate
    #  @param  data          [in]   Data to be rotated
    #  @return Rotated value
    #  @note The rotMask bits must be contiguous
    def Var_Rot_Left(self, rotMask, data):
        index = 0
        firstBit = 0
        lastBit = 0
        foundFirstBit = False
        foundLastBit = False
        while ((index < 8) and (foundLastBit == False)):
            if (((1 << index) & rotMask) != 0):
                if not foundFirstBit:
                    firstBit = index
                    foundFirstBit = True
            else:
                if foundFirstBit:
                    lastBit = index
                    foundLastBit = True
            index += 1
        if (foundFirstBit and foundLastBit):
            tmpData = data << 1
            if ((tmpData & (1 << lastBit)) != 0):
                tmpData |= (1 << firstBit)
            tmpData &= rotMask
            return tmpData
        else:
            return 0
                
    ## Rotate LED right
    #
    #  Rotate a group of LEDs to the right.
    #
    #  @param  self          [in]   Object reference
    #  @param  rotMask       [in]   Card number and mask of LEDs to rotate
    #  @return True if set
    #  @note The LEDs must be contiguous and not span cards
    def Led_Rot_Right(self, rotMask):
        #Currently rotated bits must be next to each other and on same card
        cardNum = (rotMask >> 16) & 0xf
        index = 0
        firstBit = 0
        lastBit = 0
        foundFirstBit = False
        foundLastBit = False
        while ((index < 8) and (foundLastBit == False)):
            if (((1 << index) & rotMask) != 0):
                if not foundFirstBit:
                    firstBit = index
                    foundFirstBit = True
            else:
                if foundFirstBit:
                    lastBit = index
                    foundLastBit = True
            index += 1
        if (foundFirstBit and foundLastBit):
            tmpLed = LedBrd.currLedData[cardNum] & rotMask
            if ((LedBrd.currLedData[cardNum] & (1 << firstBit)) != 0):
                tmpLed |= (1 << lastBit)
            tmpLed = (tmpLed >> 1) & rotMask
            LedBrd.currLedData[cardNum] = (LedBrd.currLedData[cardNum] & ~rotMask) | tmpLed

    ## Rotate variable right
    #
    #  Rotate a variable to the right.
    #
    #  @param  self          [in]   Object reference
    #  @param  rotMask       [in]   Mask to rotate
    #  @param  data          [in]   Data to be rotated
    #  @return Rotated value
    #  @note The rotMask bits must be contiguous
    def Var_Rot_Right(self, rotMask, data):
        index = 0
        firstBit = 0
        lastBit = 0
        foundFirstBit = False
        foundLastBit = False
        while ((index < 8) and (foundLastBit == False)):
            if (((1 << index) & rotMask) != 0):
                if not foundFirstBit:
                    firstBit = index
                    foundFirstBit = True
            else:
                if foundFirstBit:
                    lastBit = index
                    foundLastBit = True
            index += 1
        if (foundFirstBit and foundLastBit):
            tmpData = data & rotMask
            if ((data & (1 << firstBit)) != 0):
                tmpData |= (1 << lastBit)
            tmpData = (tmpData >> 1) & rotMask
            return tmpData
        else:
            return 0

    ## Turn LEDs on
    #
    #  Turn on a group of LEDs
    #
    #  @param  self          [in]   Object reference
    #  @param  cardBitPos    [in]   Card number and mask of LEDs to turn on
    #  @return None
    def Led_On(self, cardBitPos):
        cardNum = (cardBitPos >> 16) & 0xf
        bitPos = cardBitPos & 0xff
        LedBrd.currLedData[cardNum] |= bitPos
        LedBrd.currBlinkLeds[cardNum] &= ~bitPos

    ## Turn LEDs off
    #
    #  Turn off a group of LEDs
    #
    #  @param  self          [in]   Object reference
    #  @param  cardBitPos    [in]   Card number and mask of LEDs to turn off
    #  @return None
    def Led_Off(self, cardBitPos):
        cardNum = (cardBitPos >> 16) & 0xf
        bitPos = cardBitPos & 0xff
        LedBrd.currLedData[cardNum] &= ~bitPos
        LedBrd.currBlinkLeds[cardNum] &= ~bitPos

    ## Set a group of LEDs to a certain state
    #
    #  Set a group of LEDs to an absolute state
    #
    #  @param  self          [in]   Object reference
    #  @param  cardBitPos    [in]   Card number and mask of LEDs to change
    #  @param  data          [in]   Data with new state of LEDs
    #  @return None
    def Led_Set(self, cardBitPos, data):
        cardNum = (cardBitPos >> 16) & 0xf
        mask = cardBitPos & 0xff
        LedBrd.currLedData[cardNum] &= ~mask
        LedBrd.currLedData[cardNum] |= data
        LedBrd.currBlinkLeds[cardNum] &= ~mask

    ## Set a group of LEDs to blink
    #
    #  Set a group of LEDs to blink rapidly
    #
    #  @param  self          [in]   Object reference
    #  @param  cardBitPos    [in]   Card number and mask of LEDs to change
    #  @return None
    def Led_Blink_100(self, cardBitPos):
        cardNum = (cardBitPos >> 16) & 0xf
        bitPos = cardBitPos & 0xff
        LedBrd.currBlinkLeds[cardNum] |= bitPos 
        
    ## Play a sound
    #
    #  Play a sound
    #
    #  @param  self          [in]   Object reference
    #  @param  soundIdx      [in]   Sound index
    #  @return None
    def Sounds(self, soundIdx):
        #HRS:  Finish
        pass

    ## Wait
    #
    #  Wait a certain number of milliseconds
    #
    #  @param  self          [in]   Object reference
    #  @param  delay         [in]   Delay in ms
    #  @return None
    def Wait(self, delay):
        #HRS:  Finish
        pass
    
    ## Blank score displays
    #
    #  @param  self          [in]   Object reference
    #  @return None
    def BlankScoreDisps(self):
        for index in range(RulesData.MAX_NUM_PLYRS):
            GameData.score[DispConst.DISP_PLAYER1 + index] = DispConst.DISP_BLANK

    ## Blank player num display
    #
    #  @param  self          [in]   Object reference
    #  @return None
    def BlankPlyrNumDisp(self):
        GameData.currPlayer = DispConst.DISP_BLANK
