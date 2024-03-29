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
# @file:   incandDrvTest.py
# @author: Hugh Spahr
# @date:   9/21/2014
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
# Incandescent driver board tests.
#
#===============================================================================

testVers = '00.00.02'

import sys
import parallel
import array
import time
import msvcrt

testNum = 0
numCards = 1

CLK = 0x04
DATA = 0x01
LATCH = 0x02

def updateLights(byteList):
    for data in byteList:
        sendByte(data)
    endWrite()
    time.sleep(.1)

#Send byte
def sendByte(data):
    global pport
    for i in xrange(8):
        if (data & (1 << i) != 0):
            #Data bit is set, so clear it
            dataOut = DATA
        else:
            #Data bit is clear, so set it
            dataOut = 0
        #Set the data up, clock is low, and latch is low
        pport.setData(dataOut)
        #Clock the data bit in
        pport.setData(dataOut | CLK)

def endWrite():
    global pport
    #Bring the clock low, data doesn't matter, latch remains low
    pport.setData(0)
    #Bring the latch high
    pport.setData(LATCH)
    #Bring the latch low to end the cycle
    pport.setData(0)

def endTest(error):
    global pport
    global errMsg
    print "\nError code =", error
    pport.close()
    print "\nPress any key to close window"
    ch = msvcrt.getch()
    sys.exit(error)

#Main code
end = False
for arg in sys.argv:
  if arg.startswith('-test='):
    testNum = int(arg.replace('-test=','',1))
  elif arg.startswith('-cards='):
    numCards = int(arg.replace('-cards=','',1))
  elif arg.startswith('-?'):
    print "python inpDrvTest.py [OPTIONS]"
    print "    -?                 Options Help"
    print "    -cards=numCards    Number of cards in the SPI chain"
    print "    -test=testNum      test number, defaults to 0"
    print "-test=0: Walking 1 on lights."
    print "-test=1: Walking 1 on each card, 'n' moves to next bit."
    end = True
if end:
    print "\nPress any key to close window"
    ch = msvcrt.getch()
    sys.exit(0)
pport = parallel.Parallel()
if (testNum == 0):
    exitReq = False
    currVal = 0
    count = 0
    outData = [0] * numCards
    while (not exitReq):
        time.sleep(.1)
        byteIndex = currVal / 8
        bitIndex = currVal % 8
        outData[byteIndex] = 1 << bitIndex
        updateLights(outData)
        outData[byteIndex] = 0
        currVal += 1
        if (currVal >= numCards * 8):
            currVal = 0
            count += 1
        
        #Check if exit is requested
        while msvcrt.kbhit():
            char = msvcrt.getch()
            if ((char == 'x') or (char == 'X')):
                print "\nCount = %d" % count
                exitReq = True
elif (testNum == 1):
    exitReq = False
    count = 0
    outData = [0xfe] * numCards
    updateLights(outData)
    while (not exitReq):
        #Check if exit is requested
        while msvcrt.kbhit():
            char = msvcrt.getch()
            if ((char == 'x') or (char == 'X')):
                print "\nCount = %d" % count
                exitReq = True
            if ((char == 'n') or (char == 'N')):
                count += 1
                if (count >= 8):
                    count = 0
                for index in range(numCards):
                    outData[index] = ~(1 << count)
                updateLights(outData)
                print "\nCount = 0x%02x" % (1 << count)
print "\nSuccessful completion."
print "\nPress any key to close window"
ch = msvcrt.getch()
sys.exit(0)
