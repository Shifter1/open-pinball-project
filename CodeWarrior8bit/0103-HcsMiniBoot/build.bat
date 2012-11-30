"C:\Program Files\Freescale\CodeWarrior for Microcontrollers V6.1\prog\ahc08.exe" -Cs08 -FA2 -DAPP_START_ADDR=32768 -DRAM_END=1135 -env"GENPATH=Sources" -env"OBJPATH=bin" -env"TEXTPATH=bin" -env"ABSPATH=bin" "Sources\HCS08MiniBoot.asm" -objn"bin\HCS08MiniBoot.asm.o"
move "bin\HCS08MiniBoot.asm.sx" bin\HCS08MiniBoot.asm.32k.sx

"C:\Program Files\Freescale\CodeWarrior for Microcontrollers V6.1\prog\ahc08.exe" -Cs08 -FA2 -DAPP_START_ADDR=49152 -DRAM_END=1135 -env"GENPATH=Sources" -env"OBJPATH=bin" -env"TEXTPATH=bin" -env"ABSPATH=bin" "Sources\HCS08MiniBoot.asm" -objn"bin\HCS08MiniBoot.asm.o"
move "bin\HCS08MiniBoot.asm.sx" bin\HCS08MiniBoot.asm.16k.sx

"C:\Program Files\Freescale\CodeWarrior for Microcontrollers V6.1\prog\ahc08.exe" -Cs08 -FA2 -DAPP_START_ADDR=57344 -DRAM_END=639 -env"GENPATH=Sources" -env"OBJPATH=bin" -env"TEXTPATH=bin" -env"ABSPATH=bin" "Sources\HCS08MiniBoot.asm" -objn"bin\HCS08MiniBoot.asm.o"
move "bin\HCS08MiniBoot.asm.sx" bin\HCS08MiniBoot.asm.8k.sx

del EDOUT

HexMerge.exe -boot bin\HCS08MiniBoot.asm.32k.sx -crc32
HexMerge.exe -boot bin\HCS08MiniBoot.asm.16k.sx -crc32
HexMerge.exe -boot bin\HCS08MiniBoot.asm.8k.sx -crc32