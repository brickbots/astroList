"""
Specific config options, mainly for my OSX vs. Raspbian stuff
"""

import platform

#GENERAL LOOK AND FEEL

BUTTON_BG='#330000'
BUTTON_FG='#990000'
BUTTON_FONT=('Arial Unicode MS', -16, 'bold')
BUTTON_WIDTH=10
BUTTON_HEIGHT=2
BUTTON_BORDER=2
BUTTON_BORDER_COLOR='#000000'

DATA_FG_BRIGHT='#EE1111'
DATA_FG='#AA0000'

DATA_BG='#000000'

MENU_BG='#000000'
MENU_FG='#990000'
MENU_FONT=('Arial Unicode MS', -25, 'bold')
MENU_WIDTH=20
MENU_HEIGHT=2
MENU_BORDER=2
MENU_BORDER_COLOR='#000000'

OBJ_NAME_FONT=('Arial Black', -30, 'bold')
OBJ_LABEL_FONT=('Arial Unicode MS', -18, 'normal')
OBJ_DATA_FONT=('Arial Unicode MS', -18, 'bold')
OBJ_HEADING_FONT=('Arial Black', -20, 'normal')
OBJ_MONO_FONT=('Courier', -20, 'normal')

DATA_WIDTH=440
DATA_HEIGHT=554



if platform.system()=='Linux':
    AL_DB = '/home/pi/python/astroList/astroListDB.sqlite'
    PICTURE_PATH = '/home/pi/SAC_png'
    IMAGE_SIZE_FONT=['/usr/share/fonts/truetype/freefont/FreeSansBold.ttf',20]


    KEY_B01=106 #/
    KEY_B02=63 #*
    KEY_B03=82 #-
    KEY_B04=86 #+
    KEY_B05=104 #Enter

    KEY_B06=22 #Backspace

    #All numbers from 0-9 + .
    KEY_NUM_LIST=[90,87,88,89,83,84,85,79,80,81,91]


else:
    AL_DB = '/Users/rich/python/astroList/astroListDB.sqlite'
    PICTURE_PATH = '/Users/rich/Desktop/SAC_png'
    IMAGE_SIZE_FONT=['/System/Library/Fonts/SFNSDisplay-BoldItalic.otf',20]

    KEY_B01 = 2228329  # i
    KEY_B02 = 2031727  # o
    KEY_B03 = 2293872  # p
    KEY_B04 = 2687035  # ;
    KEY_B05 = 2883631  # /

    KEY_B06 = 8124162  # Left arrow

    # All numbers from 0-9 + .
    KEY_NUM_LIST = [1900592, 1179697, 1245234, 1310771, 1376308, 1507381, 1441846, 1703991, 1835064, 1638457, 3080238]

