# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""This example uses the capacitive touch pads on the Circuit Playground. They are located around
the outer edge of the board and are labeled A1-A6 and TX. (A0 is not a touch pad.) This example
lights up the nearest NeoPixel to that pad a different color of the rainbow!"""
import time
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.3
tone_volume = 0.1 

FREQUENCY_DO_C4 = 523.25
FREQUENCY_DOd_Cd4 = 554
FREQUENCY_RE_D4 = 587.0
FREQUENCY_REd_Dd4 = 622
FREQUENCY_MI_E4 = 659.25
FREQUENCY_FA_F4 = 698.46
FREQUENCY_FAd_Fd4 = 740
FREQUENCY_SOL_G4 = 783.99
FREQUENCY_SOLd_Gd4 = 831
FREQUENCY_LA_A4 = 880.00
FREQUENCY_LAd_Ad4 = 932
FREQUENCY_SI_B4 = 988.00
FREQUENCY_DO_C5 = 1046.5
FREQUENCY_DOd_Cd5 = 1109
FREQUENCY_RE_D5 = 1175
FREQUENCY_REd_Dd5 = 1244.5
FREQUENCY_MI_E5 = 1318.5
FREQUENCY_FA_F5 = 1397
FREQUENCY_FAd_Fd5 = 1480
FREQUENCY_SOL_G5 = 1568
FREQUENCY_SOLd_Gd5 = 1661
FREQUENCY_LA_A5 = 1760

while True:

    while cp.touch_A1 and not( cp.touch_A2):
        print("Touched A1!")
        cp.pixels[5] = (255, 152, 1)
        cp.start_tone(FREQUENCY_DO_C4)


    while cp.touch_A1 and cp.touch_A2:
        print("Touched A1 and A2!")
        
        cp.pixels[6] = (185, 187, 0)
        cp.start_tone(FREQUENCY_RE_D4)
    while cp.touch_A2 and not(cp.touch_A1 or cp.touch_A3):
        print("Touched A2!")
        cp.pixels[7] = (115, 221, 0)
        cp.start_tone(FREQUENCY_MI_E4)

    while cp.touch_A2 and cp.touch_A3:
        print("Touched A2 and A3!")
        cp.pixels[8] = (45, 255, 0)
        cp.start_tone(FREQUENCY_FA_F4)

    while cp.touch_A3 and not(cp.touch_A2 or cp.touch_A4):
        print("Touched A3!")
        cp.pixels[9] = (30, 255, 85)
        cp.start_tone(FREQUENCY_SOL_G4)
    while cp.touch_A3 and cp.touch_A4:
        print("Touched A3 and A4!")
        cp.pixels[9] = (15, 255, 170)
        cp.start_tone(FREQUENCY_LA_A4)


    while cp.touch_A4 and not(cp.touch_A3 or cp.touch_A5):
        print("Touched A4!")
        cp.pixels[0] = (1, 255, 255)
        cp.start_tone(FREQUENCY_SI_B4)


    while cp.touch_A4 and cp.touch_A5:
        print("Touched A4 and A5!")
        cp.pixels[1] = (14, 255, 255)
        cp.start_tone(FREQUENCY_DO_C5)
    while cp.touch_A5 and not(cp.touch_A4 or cp.touch_A6):
        print("Touched A5!")
        cp.pixels[1] = (28, 135, 255)
        cp.start_tone(FREQUENCY_RE_D5)


    while cp.touch_A5 and cp.touch_A6:
        print("Touched A5 and A6!")
        cp.pixels[2] = (43, 0, 255)
        cp.start_tone(FREQUENCY_MI_E5)

    while cp.touch_A6 and not(cp.touch_A5 or cp.touch_TX):
        print("Touched A6!")
        cp.pixels[3] = (184, 0, 221)
        cp.start_tone(FREQUENCY_FA_F5)
    while cp.touch_A6 and cp.touch_TX:
        print("Touched A6 and TX!")
        cp.pixels[3] = (113, 0, 107)
        cp.start_tone(FREQUENCY_SOL_G5)   

    while cp.touch_TX and not(cp.touch_A6):
        print("Touched TX!")
        cp.pixels[4] = (255, 0, 154)
        cp.start_tone(FREQUENCY_LA_A5)


    time.sleep(0.1)
    cp.stop_tone()
    cp.pixels.fill((0, 0, 0))

