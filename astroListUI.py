from Tkinter import *
import constDict
import alUtils
from alConfig import *

BUTTON_BG='#330000'
BUTTON_FG='#990000'
BUTTON_FONT=('Arial Unicode MS', -16, 'bold')
BUTTON_WIDTH=10
BUTTON_HEIGHT=2
BUTTON_BORDER=2
BUTTON_BORDER_COLOR='#000000'

DATA_FG='#EE1111'
DATA_BG='#000000'

MENU_BG='#000000'
MENU_FG='#990000'
MENU_FONT=('Arial Unicode MS', -25, 'bold')
MENU_WIDTH=20
MENU_HEIGHT=2
MENU_BORDER=2
MENU_BORDER_COLOR='#000000'

OBJ_NAME_FONT=('Arial Black', -30, 'bold')
OBJ_LABEL_FONT=('Arial Unicode MS', -18, 'bold')
OBJ_DATA_FONT=('Arial Unicode MS', -18, 'bold')
OBJ_HEADING_FONT=('Arial Black', -20, 'normal')

DATA_WIDTH=440
DATA_HEIGHT=554

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
        tmpW.configure(text=self._oInfo('PREFIX') + ' ' + self._oInfo('OBJECT'), font=OBJ_NAME_FONT,
                       foreground=DATA_FG, background=DATA_BG, anchor=W)
        tmpW.grid(row=0,column=0, columnspan=4, sticky=W+E)

        #Alternate NAme
        tmpW = Label(self._layout)
        tmpW.configure(text=self._oInfo('OTHER'), font=OBJ_HEADING_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=W)
        tmpW.grid(row=1, column=0, columnspan=4, sticky=W+E)

        #Spacer
        tmpW = Label(self._layout)
        tmpW.configure(text=' ', font=BUTTON_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=W)
        tmpW.grid(row=2, column=0, columnspan=4, sticky=W + E)

        #Type
        tmpW = Label(self._layout)
        tmpW.configure(text='Type:', font=OBJ_LABEL_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=W)
        tmpW.grid(row=3, column=0, sticky=W + E)
        tmpW = Label(self._layout)
        tmpW.configure(text=self._oInfo('TYPE'), font=OBJ_DATA_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=W)
        tmpW.grid(row=3, column=1, sticky=W + E)


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

class ALMenu(object):
    def __init__(self,parent, menuItemList=None):
        self._parent = parent
        self._menuItemList=menuItemList
        if not self._menuItemList:
            self._menuItemList=['One','Two','Three']

        self._drawMenu()

    def draw(self, newParent=None):
        if newParent:
            self._parent = newParent
        self._drawMenu()

    def _drawMenu(self):
        self._menuItems=[]
        i=1
        for menuItem in self._menuItemList:
            self._menuItems.append(Label(self._parent))
            self._menuItems[-1].configure(text="        %i - %s" %(i,menuItem) , font = MENU_FONT, background = MENU_BG,
                                          foreground=MENU_FG, height=MENU_HEIGHT, width = MENU_WIDTH,
                                          highlightthickness = MENU_BORDER, highlightbackground = MENU_BORDER_COLOR,
                                          highlightcolor = MENU_BORDER_COLOR, anchor=W)
            self._menuItems[-1].grid(column=0, row=i, sticky=N + S + E + W)
            i+=1

    def dataType(self):
        """

        :return: String indicating what's in the data pane
        """
        return "TEST"

    def keyHandle(self,keyEvent):
        print "DATA KEY: %s - %s" % (keyEvent.keycode, keyEvent.char)


class MainMenu(ALMenu):
    def __init__(self, parent):
        super(MainMenu, self).__init__(parent, menuItemList=['ALL', 'NGC', 'Messier', 'Herschel', 'Caldwell', 'SAC'])

    def dataType(self):
        return "MAIN"


class Filter(object):
    def __init__(self):
        self._catalog=None
        self._type=None
        self._magnitude=None
        self._constellation=None


class FilterPane(object):
    def __init__(self, parent, filterObject):
        self._parent=parent
        self._filterObject=filterObject

        self.draw()

    def draw(self, newParent=None):
        if newParent:
            self._parent=newParent
        testLabel=Label(self._parent, text="Filter this yo!")
        testLabel.grid()

    def keyHandle(self,keyEvent):
        print "DATA KEY: %s - %s" % (keyEvent.keycode, keyEvent.char)

    def dataType(self):
        return "FILTER"

class AstroList(object):
    def __init__(self, parent):
        self._filter=Filter()
        self._parent = parent
        self._mainLayout = Frame(self._parent, height=600, width=510, background="#000000", takefocus=1)
        self._mainLayout.bind("<Key>", self._keyHandle)
        self._mainLayout.grid_propagate(0)
        self._mainLayout.grid()

        self.button1 = Label(self._mainLayout )
        self.button1.configure(text="CLOSE", font=BUTTON_FONT, background=BUTTON_BG, foreground=BUTTON_FG,
                               height=BUTTON_HEIGHT, width=BUTTON_WIDTH, highlightthickness=BUTTON_BORDER,
                               highlightbackground=BUTTON_BORDER_COLOR, highlightcolor=BUTTON_BORDER_COLOR)
        self.button1.grid(column=0, row=0, sticky=N+S+E+W)

        self.button2 = Label(self._mainLayout )
        self.button2.configure(text="FILTER", font=BUTTON_FONT, background=BUTTON_BG, foreground=BUTTON_FG,
                               height=BUTTON_HEIGHT, width=BUTTON_WIDTH, highlightthickness=BUTTON_BORDER,
                               highlightbackground=BUTTON_BORDER_COLOR, highlightcolor=BUTTON_BORDER_COLOR)
        self.button2.grid(column=1, row=0, sticky=N+S+E+W)

        self.button3 = Label(self._mainLayout)
        self.button3.configure(text="SORT", font=BUTTON_FONT, background=BUTTON_BG, foreground=BUTTON_FG,
                               height=BUTTON_HEIGHT, width=BUTTON_WIDTH, highlightthickness=BUTTON_BORDER,
                               highlightbackground=BUTTON_BORDER_COLOR, highlightcolor=BUTTON_BORDER_COLOR)
        self.button3.grid(column=2, row=0, sticky=N+S+E+W)

        self.button4 = Label(self._mainLayout)
        self.button4.configure(text="CHART", font=BUTTON_FONT, background=BUTTON_BG, foreground=BUTTON_FG,
                               height=BUTTON_HEIGHT, width=BUTTON_WIDTH, highlightthickness=BUTTON_BORDER,
                               highlightbackground=BUTTON_BORDER_COLOR, highlightcolor=BUTTON_BORDER_COLOR)
        self.button4.grid(column=3, row=0, columnspan=2, sticky=N+S+E+W)

        self.button5 = Label(self._mainLayout)
        self.button5.configure(text="", font=BUTTON_FONT, background=BUTTON_BG, foreground=BUTTON_FG,
                               height=BUTTON_HEIGHT * 4, width=6, highlightthickness=BUTTON_BORDER,
                               highlightbackground=BUTTON_BORDER_COLOR, highlightcolor=BUTTON_BORDER_COLOR)
        self.button5.grid(column=4, row=1, rowspan=2, sticky=N+S+E+W)

        self.button6 = Label(self._mainLayout)
        self.button6.configure(text="", font=BUTTON_FONT, background=BUTTON_BG, foreground=BUTTON_FG,
                               height=BUTTON_HEIGHT * 4, width=6, highlightthickness=BUTTON_BORDER,
                               highlightbackground=BUTTON_BORDER_COLOR, highlightcolor=BUTTON_BORDER_COLOR)
        self.button6.grid(column=4, row=3, rowspan=2, sticky=N+S+E+W)

        self.cornerSpace=Label(self._mainLayout)
        self.cornerSpace.configure(text="", font=BUTTON_FONT, background=DATA_BG, foreground=DATA_FG,
                                   height=BUTTON_HEIGHT, width=6, highlightthickness=BUTTON_BORDER,
                                   highlightbackground=BUTTON_BORDER_COLOR, highlightcolor=BUTTON_BORDER_COLOR)
        self.cornerSpace.grid(column=5, row=5)

        self._dataFrame=None
        self._clearData() #also ends up creating frame
        self._dataObject=MainMenu(self._dataFrame)
        self._mainLayout.focus_set()

    def _clearData(self):
        self._dataObject=None

        if self._dataFrame:
            self._dataFrame.destroy()
        self._dataFrame = Frame(self._mainLayout, height=DATA_HEIGHT, width=DATA_WIDTH)
        self._dataFrame.configure(background=DATA_BG)
        self._dataFrame.grid_propagate(0)
        self._dataFrame.grid(column=0, row=1, columnspan=4, rowspan=5)


    def _keyHandle(self, keyEvent):
        print "KEY: %s - %s" % (keyEvent.keycode,keyEvent.char)

        if keyEvent.keycode==KEY_B01:
            #Filter
            if self._dataObject.dataType()=='FILTER':
                #Restore previous data objet
                self._clearData()
                self._dataObject=self._dataObjectBackup
                self._dataObject.draw(self._dataFrame)
            else:
                self._dataObjectBackup=self._dataObject
                self._clearData()
                self._dataObject=FilterPane(self._dataFrame,self._filter)

        elif keyEvent.keycode in KEY_NUM_LIST:
            #Numeric keys, decode for convinience
            num=KEY_NUM_LIST.index(keyEvent.keycode)
            if self._dataObject.dataType()=='MAIN':
                if num==1:
                    self._clearData()
                    self._dataObject=ALObjectInfo(self._dataFrame, self._filter)

        else:
            #Pass through to data objects
            self._dataObject.keyHandle(keyEvent)
