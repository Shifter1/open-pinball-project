#!/usr/bin/env python
#
# Warning - This is an auto-generated file.  All changes to this file will
# be overwritten next time GenPyCode.py is re-run.  Do not change this file
# unless you want to start hand editing the files.
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
# @file    rulesFunc.py
# @author  AutoGenerated
# @date    02/07/2015
#
# @note    Open Pinball Project
# @note    Copyright 2014, Hugh Spahr
#
# @brief These are the rules function names.  The rules functions can call
#    other rules functions, or be called in chains.  The generator saves
#    the file as rulesFunc.py.gen.  The pinball framework uses rulesFunc.py.
#    This insures a newly generated file won't accidentally overwrite a
#    user modified rules file.

#===============================================================================

from inpBitNames import InpBitNames
from solBitNames import SolBitNames
from ledBitNames import LedBitNames
from timers import Timers
from rulesData import RulesData
from sounds import Sounds
from bgndSounds import BgndMusic
from states import State
from images import Images
from dispConstIntf import DispConst

## Rules functions class.
#  Contains all the rules that are specific this this set of pinball rules.

class RulesFunc:
    LEFT_FLIPPER = 0x01
    RIGHT_FLIPPER = 0x02
    prev_flipper = 0
    LFT_TRGT_1 = 0x01
    LFT_TRGT_2 = 0x02
    RGHT_TRGT_1 = 0x04
    RGHT_TRGT_2 = 0x08
    TRGT_MSK = 0x0f
    curr_targets = 0
    tilted = False
    kick_retries = 0
    prev_flipper = 0
    
    ## Initialize rulesFuncs class
    #
    #  Initialize rules functions class
    #
    #  @param  self          [in]   Object reference
    #  @param  gameData      [in]   Object reference
    #  @return None
    def __init__(self, gameData):
        RulesFunc.GameData = gameData

    ## Function Proc_Tilt
    #
    #  @param  self          [in]   Object reference
    #  @return None
    def Proc_Tilt(self):
        pass
#        if (RulesFunc.GameData.StdFuncs.CheckInpBit(InpBitNames.TILT_SWITCH)):
#            RulesFunc.GameData.StdFuncs.Disable_Solenoids()
#            RulesFunc.GameData.gameMode = State.MODE_TILT

    ## Function Proc_Flipper
    #
    #  @param  self          [in]   Object reference
    #  @return None
    def Proc_Flipper(self):
        if (RulesFunc.GameData.StdFuncs.CheckSolBit(SolBitNames.SOL_LFT_FLIPPER)):
            if ((RulesFunc.prev_flipper & self.LEFT_FLIPPER) == 0):
                # Ordered LED bits incorrectly when wiring, so left flipper rotates right 
                RulesFunc.GameData.StdFuncs.Led_Rot_Right(LedBitNames.LED_INLN_LFT | LedBitNames.LED_INLN_CTR | LedBitNames.LED_INLN_RGHT)
                RulesFunc.GameData.inlaneLights[RulesFunc.GameData.currPlayer] = RulesFunc.GameData.StdFuncs.Var_Rot_Left(  \
                    LedBitNames.LED_INLN_LFT | LedBitNames.LED_INLN_CTR | LedBitNames.LED_INLN_RGHT, RulesFunc.GameData.inlaneLights[RulesFunc.GameData.currPlayer])
                RulesFunc.prev_flipper |= self.LEFT_FLIPPER
        else:
            RulesFunc.prev_flipper &= ~self.LEFT_FLIPPER
        if (RulesFunc.GameData.StdFuncs.CheckSolBit(SolBitNames.SOL_RGHT_FLIPPER)):
            if ((RulesFunc.prev_flipper & self.RIGHT_FLIPPER) == 0):
                # Ordered LED bits incorrectly when wiring, so right flipper rotates left 
                RulesFunc.GameData.StdFuncs.Led_Rot_Left(LedBitNames.LED_INLN_LFT | LedBitNames.LED_INLN_CTR | LedBitNames.LED_INLN_RGHT)
                RulesFunc.GameData.inlaneLights[RulesFunc.GameData.currPlayer] = RulesFunc.GameData.StdFuncs.Var_Rot_Right(  \
                    LedBitNames.LED_INLN_LFT | LedBitNames.LED_INLN_CTR | LedBitNames.LED_INLN_RGHT, RulesFunc.GameData.inlaneLights[RulesFunc.GameData.currPlayer])
                RulesFunc.prev_flipper |= self.RIGHT_FLIPPER
        else:
            RulesFunc.prev_flipper &= ~self.RIGHT_FLIPPER

    ## Function Proc_Inlane
    #
    #  @param  self          [in]   Object reference
    #  @return None
    def Proc_Inlane(self):
        if (RulesFunc.GameData.StdFuncs.CheckInpBit(InpBitNames.INP_UPPER_LFT_ROLLOVER) and \
                not RulesFunc.GameData.StdFuncs.CheckLedBit(LedBitNames.LED_INLN_LFT)):
            RulesFunc.GameData.StdFuncs.Led_On(LedBitNames.LED_INLN_LFT)
            RulesFunc.GameData.inlaneLights[RulesFunc.GameData.currPlayer] |= LedBitNames.LED_INLN_LFT
        if (RulesFunc.GameData.StdFuncs.CheckInpBit(InpBitNames.INP_UPPER_CTR_ROLLOVER) and \
                not RulesFunc.GameData.StdFuncs.CheckLedBit(LedBitNames.LED_INLN_CTR)):
            RulesFunc.GameData.StdFuncs.Led_On(LedBitNames.LED_INLN_CTR)
            RulesFunc.GameData.inlaneLights[RulesFunc.GameData.currPlayer] |= LedBitNames.LED_INLN_CTR
        if (RulesFunc.GameData.StdFuncs.CheckInpBit(InpBitNames.INP_UPPER_RGHT_ROLLOVER) and \
                not RulesFunc.GameData.StdFuncs.CheckLedBit(LedBitNames.LED_INLN_RGHT)):
            RulesFunc.GameData.StdFuncs.Led_On(LedBitNames.LED_INLN_RGHT)
            RulesFunc.GameData.inlaneLights[RulesFunc.GameData.currPlayer] |= LedBitNames.LED_INLN_RGHT
        if (RulesFunc.GameData.inlaneLights[RulesFunc.GameData.currPlayer] & (LedBitNames.LED_INLN_LFT | LedBitNames.LED_INLN_CTR | LedBitNames.LED_INLN_RGHT)) == LedBitNames.LED_INLN_LFT | LedBitNames.LED_INLN_CTR | LedBitNames.LED_INLN_RGHT:
            print "Inlanes Complete!!"
            RulesFunc.GameData.score[RulesFunc.GameData.currPlayer] += 10
            RulesFunc.GameData.inlaneLights[RulesFunc.GameData.currPlayer] = 0
            RulesFunc.GameData.StdFuncs.Led_Off(LedBitNames.LED_INLN_LFT | LedBitNames.LED_INLN_CTR | LedBitNames.LED_INLN_RGHT)

    ## Function Proc_Targets
    #
    #  @param  self          [in]   Object reference
    #  @return None
    def Proc_Targets(self):
        if RulesFunc.GameData.StdFuncs.CheckInpBit(InpBitNames.INP_UPPER_LFT_TOP_TRGT):
            self.curr_targets |= self.LFT_TRGT_1 
        if RulesFunc.GameData.StdFuncs.CheckInpBit(InpBitNames.INP_UPPER_LFT_BTM_TRGT):
            self.curr_targets |= self.LFT_TRGT_2 
        if RulesFunc.GameData.StdFuncs.CheckInpBit(InpBitNames.INP_CTR_RGHT_ROLLOVER):
            RulesFunc.GameData.StdFuncs.Led_On(LedBitNames.LED_ROLL_RGHT)
            self.curr_targets |= self.RGHT_TRGT_1 
        if RulesFunc.GameData.StdFuncs.CheckInpBit(InpBitNames.INP_CTR_CTR_ROLLOVER):
            RulesFunc.GameData.StdFuncs.Led_On(LedBitNames.LED_ROLL_CTR)
            self.curr_targets |= self.RGHT_TRGT_2 
        if RulesFunc.GameData.StdFuncs.CheckInpBit(InpBitNames.INP_CTR_LFT_ROLLOVER):
            RulesFunc.GameData.StdFuncs.Led_On(LedBitNames.LED_ROLL_LFT)
            self.curr_targets |= self.RGHT_TRGT_2 
        if (self.curr_targets & (self.TRGT_MSK)) == self.TRGT_MSK:
            RulesFunc.GameData.gameMode = State.MODE_TARGETS_COMPLETE

    ## Process spinner input
    #
    #  Needs special processing since it is used for bonus and
    #  jackpot scoring.
    #
    #  @param  self          [in]   Object reference
    #  @return None
    def Proc_Spinner(self):
        if RulesFunc.GameData.StdFuncs.CheckInpBit(InpBitNames.INP_SPINNER):
            RulesFunc.GameData.numSpinners += 1
            
    ## Function Proc_Kickout_Hole
    #
    #  @param  self          [in]   Object reference
    #  @return None
    def Proc_Kickout_Hole(self):
        if (RulesFunc.GameData.StdFuncs.CheckSolBit(SolBitNames.SOL_KICKOUT_HOLE)):
            RulesFunc.GameData.StdFuncs.Kick(SolBitNames.SOL_KICKOUT_HOLE)

    ## Function Proc_Ball_Drain
    #
    #  @param  self          [in]   Object reference
    #  @return None
    def Proc_Ball_Drain(self):
        if (RulesFunc.GameData.StdFuncs.CheckSolBit(SolBitNames.SOL_BALL_IN_PLAY)):
            RulesFunc.GameData.gameMode = State.MODE_END_OF_BALL

    ## Function Proc_Tilt_Init
    #
    #  @param  self          [in]   Object reference
    #  @return None
    def Proc_Tilt_Init(self):
        self.tilted = True
        if (RulesFunc.GameData.StdFuncs.CheckSolBit(SolBitNames.SOL_KICKOUT_HOLE)):
            RulesFunc.GameData.StdFuncs.Kick(SolBitNames.SOL_KICKOUT_HOLE)
            self.kick_retries = 0
            RulesFunc.GameData.StdFuncs.Start(Timers.TIMEOUT_KICKOUT_TIMER)
        RulesFunc.GameData.StdFuncs.Start(Timers.TIMEOUT_BALL_LOCATE)

    ## Function Proc_Tilt_State
    #
    #  @param  self          [in]   Object reference
    #  @return None
    def Proc_Tilt_State(self):
        if (RulesFunc.GameData.StdFuncs.CheckSolBit(SolBitNames.SOL_BALL_IN_PLAY)):
            RulesFunc.GameData.StdFuncs.Enable_Solenoids()
            RulesFunc.GameData.gameMode = State.MODE_END_OF_BALL
        if (RulesFunc.GameData.StdFuncs.Expired(Timers.TIMEOUT_KICKOUT_TIMER)):
            if (RulesFunc.GameData.StdFuncs.CheckSolBit(SolBitNames.SOL_KICKOUT_HOLE)):
                self.kick_retries += 1
                if (self.kick_retries > 5):
                    RulesFunc.GameData.gameMode = State.MODE_ERROR
                    print "Can't clear kickout hole"
                RulesFunc.GameData.StdFuncs.Start(Timers.TIMEOUT_KICKOUT_TIMER)
                RulesFunc.GameData.StdFuncs.Kick(SolBitNames.SOL_KICKOUT_HOLE)
        if (RulesFunc.GameData.StdFuncs.Expired(Timers.TIMEOUT_BALL_LOCATE)):
            RulesFunc.GameData.gameMode = State.MODE_ERROR
            print "Lost Ball"

    ## Function Proc_Init
    #
    #  @param  self          [in]   Object reference
    #  @return None
    def Proc_Init(self):
        RulesFunc.GameData.StdFuncs.Disable_Solenoids()
        RulesFunc.GameData.creditBallNumDisp = RulesFunc.GameData.credits
        RulesFunc.GameData.gameMode = State.MODE_ATTRACT

    ## Function Proc_Add_Coin
    #
    #  @param  self          [in]   Object reference
    #  @return None
    def Proc_Add_Coin(self):
        if RulesFunc.GameData.StdFuncs.CheckInpBit(InpBitNames.INP_COIN_DROP):
            RulesFunc.GameData.creditsInRow += 1
            RulesFunc.GameData.partCreditsNum += 1
            if (RulesFunc.GameData.creditsInRow == RulesFunc.GameData.extraCredit):
                RulesFunc.GameData.credits += 1
                if RulesFunc.GameData.gameMode == State.MODE_PRESS_START:
                    RulesFunc.GameData.creditBallNumDisp = RulesFunc.GameData.credits
                RulesFunc.GameData.creditsInRow = 0
                RulesFunc.GameData.partCreditsNum = 0
            if (RulesFunc.GameData.partCreditsNum == RulesFunc.GameData.partCreditsDenom):
                RulesFunc.GameData.credits += 1
                if RulesFunc.GameData.gameMode == State.MODE_PRESS_START:
                    RulesFunc.GameData.creditBallNumDisp = RulesFunc.GameData.credits
                RulesFunc.GameData.partCreditsNum = 0
        if RulesFunc.GameData.StdFuncs.CheckInpBit(InpBitNames.INP_START):
            RulesFunc.GameData.creditsInRow = 0

    ## Function Proc_Press_Start
    #
    #  @param  self          [in]   Object reference
    #  @return None
    def Proc_Press_Start(self):
        if RulesFunc.GameData.StdFuncs.CheckInpBit(InpBitNames.INP_START) and (RulesFunc.GameData.ballNum == 0):
            if (RulesFunc.GameData.gameMode == State.MODE_ATTRACT):
                RulesFunc.GameData.currPlayer = 0
                RulesFunc.GameData.currPlyrDisp = 1
                RulesFunc.GameData.creditBallNumDisp = 1
                RulesFunc.GameData.gameMode = State.MODE_START_GAME
                RulesFunc.GameData.blankDisp[DispConst.DISP_PLAYER_NUM] = False
                RulesFunc.GameData.blankDisp[DispConst.DISP_CREDIT_BALL_NUM] = False
            if (RulesFunc.GameData.numPlayers < RulesFunc.GameData.GameConst.MAX_NUM_PLYRS):
                RulesFunc.GameData.score[RulesFunc.GameData.numPlayers] = 0
                RulesFunc.GameData.blankDisp[DispConst.DISP_PLAYER1 + RulesFunc.GameData.numPlayers] = False
                RulesFunc.GameData.numPlayers += 1
                RulesFunc.GameData.updDisp |= 0x3f

    ## Function Proc_Press_Start_Init
    #
    #  @param  self          [in]   Object reference
    #  @return None
    def Proc_Press_Start_Init(self):
        pass

    ## Function Proc_Start_and_Coin
    #
    #  @param  self          [in]   Object reference
    #  @return None
    def Proc_Start_and_Coin(self):
        self.Proc_Press_Start()

    ## Function Proc_Init_Game
    #
    #  @param  self          [in]   Object reference
    #  @return None
    def Proc_Init_Game(self):
        RulesFunc.GameData.StdFuncs.BgndImage(Images.IMAGE_SALOON)
        RulesFunc.GameData.ballNum = 0
        RulesFunc.GameData.bonusMult = 1
        for i in xrange(RulesFunc.GameData.GameConst.MAX_NUM_PLYRS):
            RulesFunc.GameData.inlaneLights[i] = 0

    ## Function Proc_Start_Game
    #
    #  @param  self          [in]   Object reference
    #  @return None
    def Proc_Start_Game(self):
        RulesFunc.GameData.gameMode = State.MODE_BALL_IN_PLAY

    ## Function Proc_Start_Ball_Init
    #
    #  @param  self          [in]   Object reference
    #  @return None
    def Proc_Start_Ball_Init(self):
        RulesFunc.GameData.StdFuncs.Start(Timers.TIMEOUT_KICKOUT_TIMER)
        RulesFunc.GameData.StdFuncs.Kick(SolBitNames.SOL_BALL_IN_PLAY)
        RulesFunc.GameData.kick_retries = 0

    ## Function Proc_Start_Ball_Start
    #
    #  @param  self          [in]   Object reference
    #  @return None
    def Proc_Start_Ball_Start(self):
        # unused since no switch in the plunger lane
        pass

    ## Function Proc_Ball_In_Play_Init
    #
    #  @param  self          [in]   Object reference
    #  @return None
    def Proc_Ball_In_Play_Init(self):
        RulesFunc.GameData.StdFuncs.Led_Off(LedBitNames.LED6_ALL_BITS_MSK)
        RulesFunc.GameData.StdFuncs.Led_Blink_100(LedBitNames.LED_INLN_CTR)
        RulesFunc.prev_flipper = 0
        RulesFunc.GameData.targets = 0
        RulesFunc.GameData.tilted = 0
        RulesFunc.GameData.scoreLvl = 0
        RulesFunc.GameData.numSpinners = 0

    ## Function Proc_Ball_In_Play_Start
    #
    #  @param  self          [in]   Object reference
    #  @return None
    def Proc_Ball_In_Play_Start(self):
        if RulesFunc.GameData.StdFuncs.CheckInpBit(InpBitNames.INP_UPPER_LFT_ROLLOVER):
            RulesFunc.GameData.StdFuncs.Led_On(LedBitNames.LED_INLN_LFT)
            RulesFunc.GameData.StdFuncs.Led_Blink_Off(LedBitNames.LED_INLN_CTR)
            RulesFunc.GameData.inlaneLights[RulesFunc.GameData.currPlayer] |= LedBitNames.LED_INLN_LFT
            RulesFunc.GameData.gameMode = State.MODE_NORMAL_PLAY
        if RulesFunc.GameData.StdFuncs.CheckInpBit(InpBitNames.INP_UPPER_RGHT_ROLLOVER):
            RulesFunc.GameData.StdFuncs.Led_On(LedBitNames.LED_INLN_RGHT)
            RulesFunc.GameData.StdFuncs.Led_Blink_Off(LedBitNames.LED_INLN_CTR)
            RulesFunc.GameData.inlaneLights[RulesFunc.GameData.currPlayer] |= LedBitNames.LED_INLN_RGHT
            RulesFunc.GameData.gameMode = State.MODE_NORMAL_PLAY
        if RulesFunc.GameData.StdFuncs.CheckInpBit(InpBitNames.INP_UPPER_CTR_ROLLOVER):
            RulesFunc.GameData.StdFuncs.Led_On(LedBitNames.LED_INLN_CTR)
            RulesFunc.GameData.StdFuncs.Led_Blink_Off(LedBitNames.LED_INLN_CTR)
            RulesFunc.GameData.inlaneLights[RulesFunc.GameData.currPlayer] |= LedBitNames.LED_INLN_CTR
            RulesFunc.GameData.StdFuncs.Sounds(Sounds.SOUND_NICE_SHOOTIN_TEX)
            print "Skill Shot"
            RulesFunc.GameData.score[RulesFunc.GameData.currPlayer] += 9
            RulesFunc.GameData.gameMode = State.MODE_NORMAL_PLAY
        if RulesFunc.GameData.gameMode == State.MODE_NORMAL_PLAY:
            RulesFunc.GameData.scoring = True
            #RulesFunc.GameData.StdFuncs.PlayBgnd(BgndMusic.SOUND_BGNDTRACK)

    ## Function Proc_Normal_Play_Init
    #
    #  @param  self          [in]   Object reference
    #  @return None
    def Proc_Normal_Play_Init(self):
        RulesFunc.GameData.StdFuncs.Led_Set(LedBitNames.LED_INLN_LFT | LedBitNames.LED_INLN_CTR | LedBitNames.LED_INLN_RGHT, RulesFunc.GameData.inlaneLights[RulesFunc.GameData.currPlayer])

    ## Function Proc_Normal_Play
    #
    #  @param  self          [in]   Object reference
    #  @return None
    def Proc_Normal_Play(self):
        self.Proc_Tilt()
        self.Proc_Flipper()
        self.Proc_Inlane()
        self.Proc_Targets()
        self.Proc_Spinner()
        self.Proc_Kickout_Hole()
        self.Proc_Start_and_Coin()
        self.Proc_Ball_Drain()

    ## Function Proc_End_Of_Ball
    #
    #  @param  self          [in]   Object reference
    #  @return None
    def Proc_End_Of_Ball(self):
        if not self.tilted:
            print "Bonus %d x %d" % (RulesFunc.GameData.bonusMult, RulesFunc.GameData.numSpinners)
            RulesFunc.GameData.score[RulesFunc.GameData.currPlayer] += (RulesFunc.GameData.bonusMult * RulesFunc.GameData.numSpinners)
            RulesFunc.GameData.StdFuncs.Wait(3000)
        RulesFunc.GameData.bonusMult = 1
        RulesFunc.GameData.scoreLvl = 0
        RulesFunc.GameData.numSpinners = 0
        RulesFunc.GameData.scoring = False
        RulesFunc.GameData.currPlayer += 1
        RulesFunc.GameData.currPlyrDisp += 1
        if (RulesFunc.GameData.currPlayer >= RulesFunc.GameData.numPlayers):
            RulesFunc.GameData.currPlayer = 0
            RulesFunc.GameData.currPlyrDisp = 1
            RulesFunc.GameData.ballNum += 1
            if (RulesFunc.GameData.ballNum >= RulesFunc.GameData.GameConst.BALLS_PER_GAME):
                print "Game over"
                RulesFunc.GameData.creditBallNumDisp = RulesFunc.GameData.credits
                RulesFunc.GameData.StdFuncs.StopBgnd();
                RulesFunc.GameData.StdFuncs.Wait(3000)
                RulesFunc.GameData.ballNum = 0
                RulesFunc.GameData.numPlayers = 0
                if (RulesFunc.GameData.credits == 0):
                    RulesFunc.GameData.gameMode = State.MODE_ATTRACT
                else:
                    RulesFunc.GameData.gameMode = State.MODE_PRESS_START
            else:
                print "Player %d, Ball %d" % (RulesFunc.GameData.currPlayer + 1, RulesFunc.GameData.ballNum + 1) 
                RulesFunc.GameData.gameMode = State.MODE_BALL_IN_PLAY
                RulesFunc.GameData.creditBallNumDisp = RulesFunc.GameData.ballNum + 1
        else:
            print "Player %d, Ball %d" % (RulesFunc.GameData.currPlayer + 1, RulesFunc.GameData.ballNum + 1) 
            RulesFunc.GameData.gameMode = State.MODE_BALL_IN_PLAY

    ## Function Proc_Inlane_Comp
    #
    #  @param  self          [in]   Object reference
    #  @return None
    def Proc_Inlane_Comp(self):
        pass

    ## Function Proc_Targets_Comp_Init
    #
    #  @param  self          [in]   Object reference
    #  @return None
    def Proc_Targets_Comp_Init(self):
        RulesFunc.GameData.StdFuncs.Led_Blink_100(LedBitNames.LED_SHOOT_AGAIN)
        RulesFunc.GameData.scoreLvl = 1
        self.curr_targets = 0
        RulesFunc.GameData.StdFuncs.Led_Off( \
            LedBitNames.LED_DT_1 | LedBitNames.LED_DT_2 | LedBitNames.LED_DT_3 | LedBitNames.LED_DT_4 | \
            LedBitNames.LED_DT_5 | LedBitNames.LED_DT_6 | LedBitNames.LED_DT_7)
            
        RulesFunc.GameData.bonusMult += 1
        print "Bonus mult = %d" % RulesFunc.GameData.bonusMult
        RulesFunc.GameData.score[RulesFunc.GameData.currPlayer] += 10
        RulesFunc.GameData.StdFuncs.Start(Timers.TIMEOUT_SPECIAL_TIMER)

    ## Function Proc_Targets_Comp_State
    #
    #  @param  self          [in]   Object reference
    #  @return None
    def Proc_Targets_Comp_State(self):
        self.Proc_Normal_Play()
        if (RulesFunc.GameData.StdFuncs.CheckSolBit(SolBitNames.SOL_KICKOUT_HOLE)):
            print "Collect Bonus"
            RulesFunc.GameData.score[RulesFunc.GameData.currPlayer] += (RulesFunc.GameData.bonusMult * RulesFunc.GameData.numSpinners)
        if (RulesFunc.GameData.StdFuncs.Expired(Timers.TIMEOUT_SPECIAL_TIMER)):
            RulesFunc.GameData.StdFuncs.Led_Off(LedBitNames.LED_SHOOT_AGAIN)
            RulesFunc.GameData.scoreLvl = 0
            RulesFunc.GameData.gameMode = State.MODE_NORMAL_PLAY
