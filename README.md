# MUM
Matt's Universal Macropad (MUM) is a 7-key macropad. It uses the kmk frimware.
# Features
- 7 programable keys
# CAD Model
It has 2 seperate 3d-printed pieces. The bottom case where the PCB goes, and the top cover.

<img src=assets/CAD_Screenshot.png>

<img src=assets/CAD_Render.png>

Made in Fusion 360.
# PCB
The PCB was made in KiCad.

Schematic
<img src=assets/Schematic.png>

PCB
<img src=assets/PCB.png>

# Frimware
This macropad uses KMK

The code is written in python and it is where you can configure the macros.

The Frimware/main.py code has the following macros:
- First row of keys (the two far away from eachother) are volume controls: the left one is vol. up, and the other vol. down.
- The second row is playback control. Left is Backwords, middle is Play/Pause, right is Forwards.
- The third, and last row is copy paste. Left is Copy, and Right is Paste.

# BOM
Here's everything you need to bring this hackpad to life!

BOM: 
- 4x Cherry MX Switches
- 2x SK6812 MINI Leds
- 1x XIAO RP2040
- 4x Blank DSA Keycaps
- 4x M3x16 Bolt
- 4x M3 Heatset