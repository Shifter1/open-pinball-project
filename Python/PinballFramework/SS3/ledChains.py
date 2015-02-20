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
# @file    ledChains.py
# @author  AutoGenerated
# @date    02/08/2015
#
# @note    Open Pinball Project
# @note    Copyright 2015, Hugh Spahr
#
# @brief These are the LED chains.  It includes chains to automatically change
#    LEDs depending on the state.

#===============================================================================

from states import State
from ledBitNames import LedBitNames

## LED chains class.
#
#  Contains all the LED chains that are specific this this set of pinball rules.
class LedChains():    # LED chain commands
    WAIT = 0
    REPEAT = 1
    END_CHAIN = 2

    MASK_OFFSET = 0
    CHAIN_OFFSET = 1

    # Offsets into sublist
    CH_LED_BITS_OFFSET = 0
    CH_CMD_OFFSET = 1
    PARAM_OFFSET = 2

    ## LED Chain LedCh_Attract
    #    - First entry is LED mask
    #    - Next groups have a bitfield of LEDs to change and command
    LedCh_Attract = [ LedBitNames.LED_DT_1 | LedBitNames.LED_DT_2 | LedBitNames.LED_DT_3 | LedBitNames.LED_DT_4 | LedBitNames.LED_DT_5 | LedBitNames.LED_DT_6 | LedBitNames.LED_DT_7,
          [ [LedBitNames.LED_DT_1,  WAIT, 100],
            [LedBitNames.LED_DT_2,  WAIT, 100],
            [LedBitNames.LED_DT_3,  WAIT, 100],
            [LedBitNames.LED_DT_4,  WAIT, 100],
            [LedBitNames.LED_DT_5,  WAIT, 100],
            [LedBitNames.LED_DT_6,  WAIT, 100],
            [LedBitNames.LED_DT_7,  WAIT, 100],
            [0, REPEAT, 0] ] ]

    ## LED Chain LedCh_Tilt
    #    - First entry is LED mask
    #    - Next groups have a bitfield of LEDs to change and command
    LedCh_Tilt = [ LedBitNames.LED_SHOOT_AGAIN,
          [ [0, END_CHAIN, 0] ] ]

