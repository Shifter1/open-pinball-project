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
# @file    solBitNames.py
# @author  AutoGenerated
# @date    02/08/2015
#
# @note    Open Pinball Project
# @note    Copyright 2014, Hugh Spahr
#
# @brief These are the solenoid bit names.  It has a bitmask for each solenoid.

#===============================================================================

import rs232Intf

## Solenoid bit name enumeration.
#  Contains a bit mask for each solenoid.  Can also contain bitfield masks.
#  Top most nibble contains the index of the solenoid card base 0.
class SolBitNames:
    SOL_UPPER_LFT_POP                = 0x00001
    SOL_UPPER_CTR_POP                = 0x00002
    SOL_TOP_DROP_RUBBER              = 0x00008
    SOL_DROP_BANK                    = 0x00010
    SOL_KICKOUT_HOLE                 = 0x00080
    SOL_BTM_LFT_SLING                = 0x10001
    SOL_LFT_FLIPPER                  = 0x10002
    SOL_BALL_IN_PLAY                 = 0x10008
    SOL_RGHT_FLIPPER                 = 0x10010
    SOL_BTM_LOW_POP                  = 0x10040
    SOL_BTM_UP_POP                   = 0x10080

    ## Solenoid board bit names
    # Indexed into using the [SolBitNames](@ref solBitNames.SolBitNames) class
    SOL_BRD_BIT_NAMES = [ ["UpLftPop", "UpCtrPop", "Unused", "TopDropRbr",
        "DropBank", "Unused", "Unused", "KickOut"],
        ["BtmLftSling", "LftFlip", "Unused", "BallInPlay",
        "RghtFlip", "Unused", "BtmLowPop", "BtmUpPop"] ]

    ## Solenoid board configuration
    # Three bytes for each solenoid being configured
    SOL_BRD_CFG = [ [rs232Intf.CFG_SOL_USE_SWITCH, '\x30', '\x00', rs232Intf.CFG_SOL_USE_SWITCH, '\x30', '\x00',
        rs232Intf.CFG_SOL_DISABLE, '\x00', '\x00', rs232Intf.CFG_SOL_USE_SWITCH, '\x00', '\x00',
        rs232Intf.CFG_SOL_USE_SWITCH, '\x30', '\x00', rs232Intf.CFG_SOL_DISABLE, '\x00', '\x00',
        rs232Intf.CFG_SOL_DISABLE, '\x00', '\x00', rs232Intf.CFG_SOL_AUTO_CLR, '\x30', '\x00'],
        [rs232Intf.CFG_SOL_USE_SWITCH, '\x30', '\x00', rs232Intf.CFG_SOL_USE_SWITCH, '\x30', '\x04',
        rs232Intf.CFG_SOL_DISABLE, '\x00', '\x00', rs232Intf.CFG_SOL_AUTO_CLR, '\x30', '\x00',
        rs232Intf.CFG_SOL_USE_SWITCH, '\x30', '\x04', rs232Intf.CFG_SOL_DISABLE, '\x00', '\x00',
        rs232Intf.CFG_SOL_USE_SWITCH, '\x30', '\x00', rs232Intf.CFG_SOL_USE_SWITCH, '\x30', '\x00'] ]

