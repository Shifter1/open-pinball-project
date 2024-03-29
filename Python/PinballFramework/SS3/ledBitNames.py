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
# @file    ledBitNames.py
# @author  AutoGenerated
# @date    02/08/2015
#
# @note    Open Pinball Project
# @note    Copyright 2014, Hugh Spahr
#
# @brief These are the LED bit names.  It has a bitmask for each LED.

#===============================================================================

## LED bit name enumeration.
#  Contains a bit mask for each LED.  Can also contain bitfield masks.
#  Top most nibble contains the index of the LED card base 0.
class LedBitNames:
    ## Number of LED boards in the system
    NUM_LED_BRDS = 6

    LED1_ALL_BITS_MSK                = 0x000ff
    LED_KO_CTR_BTM                   = 0x00001
    LED_KO_CTR_CTR                   = 0x00002
    LED_KO_CTR_RGHT                  = 0x00004
    LED_KO_CTR_LFT                   = 0x00008
    LED_KO_TOP_RGHT                  = 0x00010
    LED_KO_TOP_LFT                   = 0x00020
    LED_HORSESHOE                    = 0x00040
    LED_SPINNER                      = 0x00080
    LED2_ALL_BITS_MSK                = 0x100ff
    LED_ROLL_LFT                     = 0x10001
    LED_ROLL_CTR                     = 0x10002
    LED_ROLL_RGHT                    = 0x10004
    LED_POP_UPCTR                    = 0x10008
    LED_POP_UPLFT                    = 0x10010
    LED_INLN_LFT                     = 0x10020
    LED_INLN_CTR                     = 0x10040
    LED_INLN_RGHT                    = 0x10080
    LED3_ALL_BITS_MSK                = 0x200ff
    LED_MODE_7                       = 0x20001
    LED_MODE_8                       = 0x20002
    LED_MODE_9                       = 0x20004
    LED_MODE_10                      = 0x20008
    LED_MODE_11                      = 0x20010
    LED_POP_BTMUP                    = 0x20040
    LED_POP_BTMLOW                   = 0x20080
    LED4_ALL_BITS_MSK                = 0x300ff
    LED_MULT_2                       = 0x30001
    LED_MULT_3                       = 0x30002
    LED_MULT_4                       = 0x30004
    LED_MULT_5                       = 0x30008
    LED_SHOOT_AGAIN                  = 0x30080
    LED5_ALL_BITS_MSK                = 0x400ff
    LED_MODE_6                       = 0x40001
    LED_MODE_5                       = 0x40002
    LED_MODE_4                       = 0x40004
    LED_MODE_3                       = 0x40008
    LED_MODE_2                       = 0x40010
    LED_MODE_1                       = 0x40020
    LED_LFT_INLN                     = 0x40040
    LED_LFT_OUTLN                    = 0x40080
    LED6_ALL_BITS_MSK                = 0x500ff
    LED_DT_1                         = 0x50001
    LED_DT_2                         = 0x50002
    LED_DT_3                         = 0x50004
    LED_DT_4                         = 0x50008
    LED_DT_5                         = 0x50010
    LED_DT_6                         = 0x50020
    LED_DT_7                         = 0x50040

    ## LED board bit names
    # Indexed into using the [LedBitNames](@ref ledBitNames.LedBitNames) class
    LED_BRD_BIT_NAMES = [ ["KOCtrBtm", "KOCtrCtr", "KOCtrRght", "KOCtrLft",
        "KOTopRght", "KOTopLft", "Horseshoe", "Spinner"],
        ["RollLft", "RollCtr", "RollRght", "PopUpCtr",
        "PopUpLft", "InlnLft", "InlnCtr", "InlnRght"],
        ["Mode7", "Mode8", "Mode9", "Mode10",
        "Mode11", "Unused", "PopBtmUp", "PopBtmLow"],
        ["Mult2", "Mult3", "Mult4", "Mult5",
        "Unused", "Unused", "Unused", "ShootAgain"],
        ["Mode6", "Mode5", "Mode4", "Mode3",
        "Mode2", "Mode1", "LftInln", "LftOutln"],
        ["DT1", "DT2", "DT3", "DT4",
        "DT5", "DT6", "DT7", "Unused"] ]

