"""
Specific config options, mainly for my OSX vs. Raspbian stuff
"""

import platform

if platform.system()=='linux':
    AL_DB = '/home/pi/python/astroList/astroListDB.sqlite'

    KEY_B01=106 #/
    KEY_B02=63 #*
    KEY_B03=82 #-
    KEY_B04=86 #+
    KEY_B05=104 #Enter

    KEY_B06=22 #Backspace

    #All numbers from 0-9 + .
    KEY_NUM_LIST=[90,87,88,89,83,84,85,79,80,81,91]


else:
    AL_DB = '/home/users/rich/Documents/pthon/astroList/astroListDB.sqlite'

    KEY_B01 = 2228329  # i
    KEY_B02 = 2031727  # o
    KEY_B03 = 2293872  # p
    KEY_B04 = 2687035  # ;
    KEY_B05 = 2883631  # /

    KEY_B06 = 8124162  # Left arrow

    # All numbers from 0-9 + .
    KEY_NUM_LIST = [1900592, 1179697, 1245234, 1310771, 1376308, 1507381, 1441846, 1703991, 1835064, 1638457, 3080238]

