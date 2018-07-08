"""
Specific config options, mainly for my OSX vs. Raspbian stuff
"""

import platform

#GENERAL LOOK AND FEEL

BUTTON_BG='#330000'
BUTTON_FG='#990000'
BUTTON_FONT=('Arial Unicode MS', -16, 'bold')
BUTTON_WIDTH=9
BUTTON_HEIGHT=2
SIDE_BUTTON_HEIGHT=3
SIDE_BUTTON_WIDTH=5
BUTTON_BORDER=2
BUTTON_BORDER_COLOR='#000000'

DATA_FG_BRIGHT='#EE1111'
DATA_FG='#AA0000'

DATA_BG='#000000'

MENU_BG='#000000'
MENU_FG='#990000'
MENU_FONT=('Arial Unicode MS', -25, 'bold')
MENU_KEY_BG=BUTTON_BG
MENU_KEY_FG=BUTTON_FG
MENU_WIDTH=20
MENU_HEIGHT=1
MENU_BORDER=2
MENU_BORDER_COLOR='#000000'

OBJ_NAME_FONT=('Arial Black', -30, 'bold')
OBJ_LABEL_FONT=('Arial Unicode MS', -18, 'normal')
OBJ_DATA_FONT=('Arial Unicode MS', -18, 'bold')
OBJ_HEADING_FONT=('Arial Black', -20, 'normal')
OBJ_MONO_FONT=('Courier', -20, 'normal')

DATA_WIDTH=450
DATA_HEIGHT=500



if platform.system()=='Linux':
    OBSLIST_PATH='/home/pi/python/astroList/obsList/obsList.skylist'
    AL_DB = '/home/pi/python/astroList/astroListDB.sqlite'
    PICTURE_PATH = '/usr/share/skychart/data/pictures/sac'
    IMAGE_SIZE_FONT=['/usr/share/fonts/truetype/freefont/FreeSansBold.ttf',20]

    KEY_B01 = 57  # N
    KEY_B02 = 39  # S
    KEY_B03 = 52  # Z
    KEY_B04 = 82  # -
    KEY_B05 = 86  # +
    KEY_B06 = 40  # D
    KEY_B07 = 41  # F
    KEY_B08 = 25  # W
    KEY_B09 = 26  # E

    #All numbers from 0-9 + .
    KEY_NUM_LIST=[90,87,88,89,83,84,85,79,80,81,60]


else:
    OBSLIST_PATH='/Users/rich/python/astroList/obsList/obsList.skylist'
    AL_DB = '/Users/rich/python/astroList/astroListDB.sqlite'
    PICTURE_PATH = '/Applications/Cartes du Ciel/data/pictures/sac'
    IMAGE_SIZE_FONT=['/System/Library/Fonts/SFNSDisplay-BoldItalic.otf',20]

    KEY_B01 = 852087  # W
    KEY_B02 = 917605  # E
    KEY_B03 = 983154  # R
    KEY_B04 = 97  # A
    KEY_B05 = 65651  # S
    KEY_B06 = 131172  # D
    KEY_B07 = 196710  # F
    KEY_B08 = 393338  # Z
    KEY_B09 = 458872  # X

    # All numbers from 0-9 + .
    KEY_NUM_LIST = [1900592, 1179697, 1245234, 1310771, 1376308, 1507381, 1441846, 1703991, 1835064, 1638457, 3080238]

