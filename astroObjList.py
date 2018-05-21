from alConfig import *
from Tkinter import *
from alConstants import *
import alUtils

class ALObjectInfo(object):
    def __init__(self, parent, filterObject):
        self._parent=parent
        self._filter=filterObject
        self._objectList=[]
        self._listIndex=0
        self._mode=0 #0= DEtails, 1= Image!
        self._createLayout()
        self._getList()
        self.draw()

    def _createLayout(self):
        self._layout=Frame(self._parent)
        self._layout.configure(background=DATA_BG, width=DATA_WIDTH, height=DATA_HEIGHT)

        self._layout.grid_propagate(0)
        self._layout.grid(sticky=N+S+E+W)

    def _oInfo(self, name):
        """
        Returns the field specified by name
        :param name:
        :return: value of the field
        """
        curObj = self._objectList[self._listIndex]
        return curObj[alUtils.OBJ_FIELD_NAME.index(name)]

    def draw(self, newParent=None):
        if newParent:
            self._parent = newParent
        else:
            self._layout.destroy()


        self._createLayout()





        #OBject Name
        tmpW=Label(self._layout)
        tmpS=self._oInfo('PREFIX') + ' ' + self._oInfo('OBJECT')
        tmpW.configure(text=tmpS.strip(), font=OBJ_NAME_FONT,
                       foreground=DATA_FG_BRIGHT, background=DATA_BG, anchor=W)
        tmpW.grid(row=0,column=0, columnspan=4, sticky=W + E)


        #Alternate NAme
        tmpW = Label(self._layout)
        tmpW.configure(text=self._oInfo('OTHER'), font=OBJ_HEADING_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=W, width=40)
        tmpW.grid(row=1, column=0, columnspan=4)

        # Spacer / Grid Settings
        """
        tmpW = Label(self._layout)
        tmpW.configure(text='', font=BUTTON_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=W, width=2)
        tmpW.grid(row=2, column=0)
        tmpW = Label(self._layout)
        tmpW.configure(text='', font=BUTTON_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=W, width=15)
        tmpW.grid(row=2, column=1)
        tmpW = Label(self._layout)
        tmpW.configure(text='', font=BUTTON_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=W, width=2)
        tmpW.grid(row=2, column=2)
        tmpW = Label(self._layout)
        tmpW.configure(text='', font=BUTTON_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=W, width=15)
        tmpW.grid(row=2, column=3)
        """
        #Type
        tmpW = Label(self._layout)
        tmpW.configure(text='Type:', font=OBJ_LABEL_FONT, foreground=DATA_FG,
                       background=DATA_BG,  anchor=E)
        tmpW.grid(row=3, column=0, sticky=W + E)
        tmpW = Label(self._layout)
        tmpW.configure(text=OBJ_TYPES[self._oInfo('TYPE')], font=OBJ_DATA_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=W)
        tmpW.grid(row=3, column=1, columnspan=3,  sticky=W + E)

        # CONST
        tmpW = Label(self._layout)
        tmpW.configure(text='Const:', font=OBJ_LABEL_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=E)
        tmpW.grid(row=4, column=0, sticky=W + E)
        tmpW = Label(self._layout)
        tmpW.configure(text=CONSTELLATIONS[self._oInfo('CON')], font=OBJ_DATA_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=W, width=45)
        tmpW.grid(row=4, column=1, columnspan=3,  sticky=W + E)

        #notes

    def _getList(self):
        #need to do filtering here, but for now, get the WHOLE list
        self._objectList=alUtils.executeQuery("SELECT * FROM OBJECTS ORDER BY MAG")
        self._listIndex=0

    def keyHandle(self,keyEvent):
        print "DATA KEY: %s - %s" % (keyEvent.keycode, keyEvent.char)
        if keyEvent.keycode==KEY_B04:
            self._listIndex-=1
            if self._listIndex < 0:
                self._listIndex=0
        if keyEvent.keycode==KEY_B05:
            self._listIndex+=1
            if self._listIndex > len(self._objectList) - 1:
                self._listIndex=len(self._objectList) -1

        self.draw()

    def dataType(self):
        return "OBJECT"