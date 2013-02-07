/*
 *===============================================================================
 *
 *                         OOOO
 *                       OOOOOOOO
 *      PPPPPPPPPPPPP   OOO    OOO   PPPPPPPPPPPPP
 *    PPPPPPPPPPPPPP   OOO      OOO   PPPPPPPPPPPPPP
 *   PPP         PPP   OOO      OOO   PPP         PPP
 *  PPP          PPP   OOO      OOO   PPP          PPP
 *  PPP          PPP   OOO      OOO   PPP          PPP
 *  PPP          PPP   OOO      OOO   PPP          PPP
 *   PPP         PPP   OOO      OOO   PPP         PPP
 *    PPPPPPPPPPPPPP   OOO      OOO   PPPPPPPPPPPPPP
 *     PPPPPPPPPPPPP   OOO      OOO   PPP
 *               PPP   OOO      OOO   PPP
 *               PPP   OOO      OOO   PPP
 *               PPP   OOO      OOO   PPP
 *               PPP    OOO    OOO    PPP
 *               PPP     OOOOOOOO     PPP
 *              PPPPP      OOOO      PPPPP
 *
 * @file:   ParseRules.java
 * @author: Hugh Spahr
 * @date:   2/06/2013
 *
 * @note:   Open Pinball Project
 *          Copyrightę 2013, Hugh Spahr
 *
 *  This program is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 *===============================================================================
 */
/**
 * Parse a rules file.
 *
 *===============================================================================
 */

package com.wordpress.openpinballproject.hostctl;

import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class ParseRules
{
   public static final int       STATE_IDLE              = 0;
   public static final int       STATE_NAME_SOL          = 1;
   public static final int       STATE_NAME_INP          = 2;
   public static final int       STATE_NAME_LED          = 3;
   public static final int       STATE_NAME_VAR          = 4;
   public static final int       STATE_NAME_IND_VAR      = 5;
   public static final int       STATE_NAME_MODE         = 6;
   public static final int       STATE_NAME_PROC_CHAIN   = 7;
   public static final int       STATE_NAME_LED_CHAIN    = 8;

   private static final Map<String, Integer> RSVD_STATE_MAP = (Map<String, Integer>) createMap();

   private static Map<String, Integer> createMap()
   {
       Map<String, Integer> result = new HashMap<String, Integer>();
       result.put("SOLENOID_CARDS", STATE_NAME_SOL);
       result.put("INPUT_CARDS", STATE_NAME_INP);
       result.put("LED_CARDS", STATE_NAME_LED);
       result.put("VARIABLES", STATE_NAME_VAR);
       result.put("INDEXED_VARIABLES", STATE_NAME_IND_VAR);
       result.put("MODES", STATE_NAME_MODE);
       result.put("PROCESS_CHAINS", STATE_NAME_PROC_CHAIN);
       result.put("LED_CHAINS", STATE_NAME_LED_CHAIN);
       return Collections.unmodifiableMap(result);
   }
   
   public ParseRules(
      String                           rulesFile)
   {
      int                              offset;
      boolean                          done;
      int                              lineNum = 0;
      String[]                         tokens;
      int                              state = STATE_IDLE;
      Integer                          temp;
      
      try
      {
         FileInputStream fstream = new FileInputStream(rulesFile);
         DataInputStream in = new DataInputStream(fstream);
         BufferedReader br = new BufferedReader(new InputStreamReader(in));
         String strLine;
         
         try
         {
            while ((strLine = br.readLine()) != null)
            {
               done = false;
               
               /* Remove everything after a '#' since it is a comment */
               offset = strLine.indexOf("#");
               if (offset != -1)
               {
                  strLine = strLine.substring(0, offset);
               }
               
               /* Guarantee spaces before and after () {} and [] for split */
               strLine = strLine.replaceAll("\\{", " \\{ ").replaceAll("\\}", " \\} ");
               strLine = strLine.replaceAll("\\[", " \\[ ").replaceAll("\\]", " \\] ");
               strLine = strLine.replaceAll("\\(", " \\( ").replaceAll("\\)", " \\) ");
            
               /* Make sure that some tokens exist */
               tokens = strLine.split(" ");
               if (tokens.length == 0)
               {
                  done = true;
               }
               
               if (!done)
               {
                  if (state == STATE_IDLE)
                  {
                     /* Look for keyword to for section */
                     temp = RSVD_STATE_MAP.get(tokens[0]);
                     if (temp == null)
                     {
                        /* Could not find dictionary entry */
                        done = true;
                     }
                     else
                     {
                        state = temp.intValue();
                        System.out.println("Found " + tokens[0] + "on line: " + lineNum);
                        state = STATE_IDLE;
                     }
                  }
               }
               // Print the content on the console
               lineNum++;
            }
            in.close();
         }
         catch (IOException e)
         {
            // TODO Auto-generated catch block
            e.printStackTrace();
         }
      }
      catch (FileNotFoundException e)
      {
         // TODO Auto-generated catch block
         e.printStackTrace();
      }
   }
}
