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
# @file    procChains.py
# @author  AutoGenerated
# @date    02/08/2015
#
# @note    Open Pinball Project
# @note    Copyright 2015, Hugh Spahr
#
# @brief These are the processing chains.  It includes initial chains and normal
# processing chains that are run each time the rules thread runs.

#===============================================================================

from rulesFunc import RulesFunc
from states import State
from ledChains import LedChains
from soundChains import SoundChains
from imageChains import ImageChains
from sounds import Sounds

## Process chain lists.
#
#  Contains all the chains that are specific this this set of pinball rules.
class ProcChain():
    INIT_CHAIN_OFFSET = 1
    NORM_CHAIN_OFFSET = 2
    IMAGE_CHAIN_OFFSET = 3
    SOUND_CHAIN_OFFSET = 4
    LED_CHAIN_OFFSET = 5
    VIDEO_CHAIN_OFFSET = 6

    ## Create process chain lists.
    #    - First entry is State number, only used to ease debugging
    #    - Second entry is initial processing functions, called only when first entering a state
    #    - Third entry are processing functions, called each time the rules thread runs
    #    - Fourth entry is the image chain
    #    - Fifth entry is the sound chain
    #    - Sixth entry is the LED chain
    #    - Seventh entry is the video chain
    PROC_CHAIN = [
        [State.MODE_INIT, [RulesFunc.Proc_Init], [], [], [], [], [] ],
        [State.MODE_ATTRACT, [], [RulesFunc.Proc_Start_and_Coin], ImageChains.ImageCh_Attract, SoundChains.SndCh_Attract, LedChains.LedCh_Attract, [] ],
        [State.MODE_PRESS_START, [], [], [], [], [], [] ],
        [State.MODE_START_GAME, [RulesFunc.Proc_Init_Game], [RulesFunc.Proc_Start_Game], [], [], [], [] ],
        [State.MODE_START_BALL, [], [], [], [], [], [] ],
        [State.MODE_BALL_IN_PLAY, [RulesFunc.Proc_Ball_In_Play_Init], [RulesFunc.Proc_Ball_In_Play_Start, RulesFunc.Proc_Start_and_Coin], [], [], [], [] ],
        [State.MODE_NORMAL_PLAY, [RulesFunc.Proc_Normal_Play_Init], [RulesFunc.Proc_Normal_Play], [], [], [], [] ],
        [State.MODE_ERROR, [], [], [], [], [], [] ],
        [State.MODE_TILT, [RulesFunc.Proc_Tilt_Init], [RulesFunc.Proc_Tilt_State], [], Sounds.SOUND_WAH_WUH, LedChains.LedCh_Tilt, [] ],
        [State.MODE_END_OF_BALL, [RulesFunc.Proc_End_Of_Ball], [], [], [], [], [] ],
        [State.MODE_INLANE_COMPLETE, [RulesFunc.Proc_Inlane_Comp], [], [], [], [], [] ],
        [State.MODE_TARGETS_COMPLETE, [RulesFunc.Proc_Targets_Comp_Init], [RulesFunc.Proc_Targets_Comp_State], [], [], [], [] ],
    ]