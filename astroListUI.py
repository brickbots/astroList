from Tkinter import *
from alConfig import *
import astroObjList

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
        super(MainMenu, self).__init__(parent, menuItemList=['ALL', 'NGC', 'Messier', 'Herschel', 'Caldwell', 'SAC',
                                                             'Obs List'])

    def dataType(self):
        return "MAIN"


class Filter(object):
    def __init__(self):
        self._catalog=None
        self._type=None
        self._magnitude=None
        self._constellation=None

    def reset(self):
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

class SortPane(object):
    def __init__(self, parent, filterObject):
        self._parent=parent
        self._filterObject=filterObject

        self.draw()

    def draw(self, newParent=None):
        if newParent:
            self._parent=newParent
        testLabel=Label(self._parent, text="Sort this yo!")
        testLabel.grid()

    def keyHandle(self,keyEvent):
        print "DATA KEY: %s - %s" % (keyEvent.keycode, keyEvent.char)

    def dataType(self):
        return "SORT"

class AstroList(object):
    def __init__(self, parent):
        self._filter=Filter()
        self._sortClause='PREFIX, OBJECT ASC'
        self._parent = parent
        self._mainLayout = Frame(self._parent, height=600, width=510, background="#000000", takefocus=1)
        self._mainLayout.bind("<Key>", self._keyHandle)
        self._mainLayout.grid_propagate(0)
        self._mainLayout.grid()

        self.button0 = Label(self._mainLayout )
        self.button0.configure(text="CLOSE", font=BUTTON_FONT, background=BUTTON_BG, foreground=BUTTON_FG,
                               height=BUTTON_HEIGHT, width=BUTTON_WIDTH, highlightthickness=BUTTON_BORDER,
                               highlightbackground=BUTTON_BORDER_COLOR, highlightcolor=BUTTON_BORDER_COLOR)
        self.button0.grid(column=0, row=0, sticky=N+S+E+W)

        self.button1 = Label(self._mainLayout )
        self.button1.configure(text="FILTER", font=BUTTON_FONT, background=BUTTON_BG, foreground=BUTTON_FG,
                               height=BUTTON_HEIGHT, width=BUTTON_WIDTH, highlightthickness=BUTTON_BORDER,
                               highlightbackground=BUTTON_BORDER_COLOR, highlightcolor=BUTTON_BORDER_COLOR)
        self.button1.grid(column=1, row=0, sticky=N+S+E+W)

        self.button2 = Label(self._mainLayout)
        self.button2.configure(text="SORT", font=BUTTON_FONT, background=BUTTON_BG, foreground=BUTTON_FG,
                               height=BUTTON_HEIGHT, width=BUTTON_WIDTH, highlightthickness=BUTTON_BORDER,
                               highlightbackground=BUTTON_BORDER_COLOR, highlightcolor=BUTTON_BORDER_COLOR)
        self.button2.grid(column=2, row=0, sticky=N+S+E+W)

        self.button3 = Label(self._mainLayout)
        self.button3.configure(text="", font=BUTTON_FONT, background=BUTTON_BG, foreground=BUTTON_FG,
                               height=BUTTON_HEIGHT, width=BUTTON_WIDTH, highlightthickness=BUTTON_BORDER,
                               highlightbackground=BUTTON_BORDER_COLOR, highlightcolor=BUTTON_BORDER_COLOR)
        self.button3.grid(column=3, row=0, columnspan=2, sticky=N+S+E+W)

        #SIDE BUTTONS
        self.button4 = Label(self._mainLayout)
        self.button4.configure(text="", font=BUTTON_FONT, background=BUTTON_BG, foreground=BUTTON_FG,
                               height=SIDE_BUTTON_HEIGHT, width=SIDE_BUTTON_WIDTH, highlightthickness=BUTTON_BORDER,
                               highlightbackground=BUTTON_BORDER_COLOR, highlightcolor=BUTTON_BORDER_COLOR)
        self.button4.grid(column=4, row=1, sticky=N+S+E+W)

        self.button5 = Label(self._mainLayout)
        self.button5.configure(text="", font=BUTTON_FONT, background=BUTTON_BG, foreground=BUTTON_FG,
                               height=SIDE_BUTTON_HEIGHT, width=SIDE_BUTTON_WIDTH, highlightthickness=BUTTON_BORDER,
                               highlightbackground=BUTTON_BORDER_COLOR, highlightcolor=BUTTON_BORDER_COLOR)
        self.button5.grid(column=4, row=2, sticky=N+S+E+W)

        self.button6 = Label(self._mainLayout)
        self.button6.configure(text="", font=BUTTON_FONT, background=BUTTON_BG, foreground=BUTTON_FG,
                               height=SIDE_BUTTON_HEIGHT, width=SIDE_BUTTON_WIDTH, highlightthickness=BUTTON_BORDER,
                               highlightbackground=BUTTON_BORDER_COLOR, highlightcolor=BUTTON_BORDER_COLOR)
        self.button6.grid(column=4, row=3, sticky=N + S + E + W)

        self.button7 = Label(self._mainLayout)
        self.button7.configure(text="", font=BUTTON_FONT, background=BUTTON_BG, foreground=BUTTON_FG,
                               height=SIDE_BUTTON_HEIGHT, width=SIDE_BUTTON_WIDTH, highlightthickness=BUTTON_BORDER,
                               highlightbackground=BUTTON_BORDER_COLOR, highlightcolor=BUTTON_BORDER_COLOR)
        self.button7.grid(column=4, row=4, rowspan=2, sticky=N + S + E + W)


        #BOTTOM BUTTONS
        self.button8 = Label(self._mainLayout)
        self.button8.configure(text="", font=BUTTON_FONT, background=BUTTON_BG, foreground=BUTTON_FG,
                               height=BUTTON_HEIGHT, width=BUTTON_WIDTH, highlightthickness=BUTTON_BORDER,
                               highlightbackground=BUTTON_BORDER_COLOR, highlightcolor=BUTTON_BORDER_COLOR)
        self.button8.grid(column=0, row=5, sticky=N + S + E + W)

        self.button9 = Label(self._mainLayout)
        self.button9.configure(text="", font=BUTTON_FONT, background=BUTTON_BG, foreground=BUTTON_FG,
                               height=BUTTON_HEIGHT, width=BUTTON_WIDTH, highlightthickness=BUTTON_BORDER,
                               highlightbackground=BUTTON_BORDER_COLOR, highlightcolor=BUTTON_BORDER_COLOR)
        self.button9.grid(column=3, row=5, sticky=N + S + E + W)

        self.bottomSpace = Label(self._mainLayout)
        self.bottomSpace.configure(text="", font=BUTTON_FONT, background=DATA_BG, foreground=DATA_FG,
                                   height=BUTTON_HEIGHT, width=BUTTON_WIDTH *2, highlightthickness=BUTTON_BORDER,
                                   highlightbackground=DATA_BG, highlightcolor=BUTTON_BORDER_COLOR)
        self.bottomSpace.grid(column=1, row=5, columnspan=2)

        self._dataFrame=None
        self._clearData() #also ends up creating frame
        self._dataObject=MainMenu(self._dataFrame)
        self._mainLayout.focus_set()

    def setStatus(self, statusText):
        print "STATUS:" + statusText

    def setButton(self, buttonNo, buttonText):
        if buttonNo > 3 and buttonNo < 8:
            buttonText='\\n'.join(buttonText)
        eval('self.button%i.configure(text="%s")' % (buttonNo, buttonText))

    def _clearData(self):
        self._dataObject=None

        if self._dataFrame:
            self._dataFrame.destroy()
        self._dataFrame = Frame(self._mainLayout, height=DATA_HEIGHT, width=DATA_WIDTH)
        self._dataFrame.configure(background=DATA_BG)
        self._dataFrame.grid_propagate(0)
        self._dataFrame.grid(column=0, row=1, columnspan=4, rowspan=4)


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

        if keyEvent.keycode==KEY_B02:
            #SORT
            if self._dataObject.dataType()=='SORT':
                #Restore previous data objet
                self._clearData()
                self._dataObject=self._dataObjectBackup
                self._dataObject.draw(self._dataFrame)
            else:
                self._dataObjectBackup=self._dataObject
                self._clearData()
                self._dataObject=SortPane(self._dataFrame,self._filter)

        elif keyEvent.keycode in KEY_NUM_LIST:
            #Numeric keys, decode for convinience
            num=KEY_NUM_LIST.index(keyEvent.keycode)
            if self._dataObject.dataType()=='MAIN':
                if num==1:
                    self._clearData()
                    self._dataObject = astroObjList.ALObjectInfo(self._dataFrame, self._filter, self._sortClause,
                                                                 self.setButton, self.setStatus)
                if num==2:
                    #NGC
                    self._clearData()
                    self._filter.reset()
                    self._filter._catalog='NGC'
                    self._dataObject = astroObjList.ALObjectInfo(self._dataFrame, self._filter, self._sortClause,
                                                                 self.setButton, self.setStatus)

                if num==3:
                    #Messier
                    self._clearData()
                    self._filter.reset()
                    self._filter._catalog='M'
                    self._sortClause='OTHER'
                    self._dataObject = astroObjList.ALObjectInfo(self._dataFrame, self._filter, self._sortClause,
                                                                 self.setButton, self.setStatus)
                if num==4:
                    #Herschel
                    self._clearData()
                    self._filter.reset()
                    self._filter._catalog='H'
                    self._sortClause='PREFIX, OBJECT ASC'
                    self._dataObject = astroObjList.ALObjectInfo(self._dataFrame, self._filter, self._sortClause,
                                                                 self.setButton, self.setStatus)
                if num==5:
                    ##Caldwel
                    self._clearData()
                    self._filter.reset()
                    self._filter._catalog='C'
                    self._sortClause='PREFIX, OBJECT ASC'
                    self._dataObject = astroObjList.ALObjectInfo(self._dataFrame, self._filter, self._sortClause,
                                                                 self.setButton, self.setStatus)

                if num==6:
                    #SAC
                    self._clearData()
                    self._filter.reset()
                    self._filter._catalog='B'
                    self._sortClause='PREFIX, OBJECT ASC'
                    self._dataObject = astroObjList.ALObjectInfo(self._dataFrame, self._filter, self._sortClause,
                                                                 self.setButton, self.setStatus)
            elif self._dataObject.dataType() == 'OBJECT':
                self._dataObject.keyHandle(keyEvent)

        else:
            #Pass through to data objects
            self._dataObject.keyHandle(keyEvent)
