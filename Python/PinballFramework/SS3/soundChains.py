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
# @file    soundChains.py
# @author  AutoGenerated
# @date    02/08/2015
#
# @note    Open Pinball Project
# @note    Copyright 2015, Hugh Spahr
#
# @brief These are the sound chains.  It includes chains to automatically play
#    a string of sounds with delays in between.

#===============================================================================

from sounds import Sounds

## Sound chains class.
#
#  Contains all the sound chains that are specific to this set of pinball rules.
#
#  Each sound chain group contains the sound to play, the command, and the
#  parameter to the command.

class SoundChains():    # Sound chain commands
    WAIT = 0
    REPEAT = 1
    END_CHAIN = 2

    SOUND_OFFSET = 0
    CH_CMD_OFFSET = 1
    PARAM_OFFSET = 2

    ## Sound Chain SndCh_Attract
    #    - Groups have sound name then WAIT command
    #    - Chain ends with REPEAT if desired
    SndCh_Attract = [
        [Sounds.SOUND_YALL_COME_BACK,  WAIT, 30000],
        [Sounds.SOUND_HOWDYFOLKS,  WAIT, 30000],
        [0, REPEAT, 0] ]
