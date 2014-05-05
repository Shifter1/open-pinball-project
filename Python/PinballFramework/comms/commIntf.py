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
# @file    commIntf.py
# @author  Hugh Spahr
# @date    1/16/2014
#
# @note    Open Pinball Project
# @note    Copyright 2014, Hugh Spahr
#
# @brief This is the communication interface file that is used to send commands and
# receive responses from the hardware.

#===============================================================================

import rs232Intf
import errIntf

## Update the stored solenoid configuration so it can be sent to the board. 
#
#  Verify the board is valid and solenoid number is valid.  Copy configuration
#  into [solBrdCfg](@ref comms.commThread.CommThread.solBrdCfg).
#
#  @param  commThread    [in]   Comm thread object
#  @param  brd           [in]   Solenoid board number base 0
#  @param  sol           [in]   Solenoid number base 0
#  @param  params        [in]   List of parameters for solenoid cfg
#  @return Can return CMD_OK if good, or BAD_SOL_BRD_NUM, BAD_SOL_NUM,
#     BAD_PARAM_BYTES if an error.
def updateSol(commThread, brd, sol, params):
    if brd > commThread.numSolBrd:
        return errIntf.BAD_SOL_BRD_NUM
    if sol > rs232Intf.NUM_SOL_PER_BRD:
        return errIntf.BAD_SOL_NUM
    if len(params) != rs232Intf.CFG_BYTES_PER_SOL:
        return errIntf.BAD_PARAM_BYTES
    for loop in range(rs232Intf.CFG_BYTES_PER_SOL):
        commThread.solBrdCfg[brd][(rs232Intf.CFG_BYTES_PER_SOL * sol) + loop] = params[loop]
    return errIntf.CMD_OK

## Mark a solenoid configuration to be sent to the board.
#
#  Verify the board is valid.  Mark a bit to indicate the solenoid cfg must be sent to the
#  board.
#
#  @param  commThread    [in]   Comm thread object
#  @param  brd           [in]   Solenoid board number base 0
#  @return Can return CMD_OK if good, or BAD_SOL_BRD_NUM if an error.
def sendSolCfg(commThread, brd):
    if brd > commThread.numSolBrd:
        return errIntf.BAD_SOL_BRD_NUM
    commThread.updateSolBrdCfg |= (1 << brd)
    return errIntf.CMD_OK

## Update the stored input configuration so it can be sent to the board. 
#
#  Verify the board is valid and input number is valid.  Copy configuration
#  into [inpBrdCfg](@ref comms.commThread.CommThread.inpBrdCfg).
#
#  @param  commThread    [in]   Comm thread object
#  @param  brd           [in]   Solenoid board number base 0
#  @param  inp           [in]   Solenoid number base 0
#  @param  cfg           [in]   Parameter for input cfg
#  @return Can return CMD_OK if good, or BAD_INP_BRD_NUM, BAD_INP_NUM
#     if an error.
def updateInp(commThread, brd, inp, cfg):
    if brd > commThread.numInpBrd:
        return errIntf.BAD_INP_BRD_NUM
    if inp > rs232Intf.NUM_INP_PER_BRD:
        return errIntf.BAD_INP_NUM
    commThread.inpBrdCfg[brd][rs232Intf.CFG_BYTES_PER_INP * inp] = cfg
    return errIntf.CMD_OK

## Mark an input configuration to be sent to the board.
#
#  Verify the board is valid.  Mark a bit to indicate the input cfg must be sent to the
#  board.
#
#  @param  commThread    [in]   Comm thread object
#  @param  brd           [in]   Solenoid board number base 0
#  @return Can return CMD_OK if good, or BAD_INP_BRD_NUM if an error.
def sendInpCfg(commThread, brd):
    if brd > commThread.numInpBrd:
        return errIntf.BAD_INP_BRD_NUM
    commThread.updateInpBrdCfg |= (1 << brd)
    return errIntf.CMD_OK