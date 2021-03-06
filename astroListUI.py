from Tkinter import *
from alConfig import *
from alConstants import *
import astroObjList

class ALMenu(object):
    def __init__(self, uiObj=None, filterObj=None, menuTitle='', menuItemList=None):
        self._parent = None
        self._filterObj=filterObj
        self._menuTitle=menuTitle
        self._menuItemList=menuItemList
        self._uiObj=uiObj
        if not self._menuItemList:
            self._menuItemList=['One','Two','Three']

    def draw(self, newParent=None):
        if newParent:
            self._parent = newParent
        self._drawMenu()

    def _drawMenu(self):
        # TITLE
        tmpW=Label(self._parent)
        tmpW.configure(text=self._menuTitle, font=MENU_FONT, background=MENU_BG,
                                      foreground=MENU_FG, height=MENU_HEIGHT,
                                      highlightthickness=MENU_BORDER, highlightbackground=MENU_BORDER_COLOR,
                                      highlightcolor=MENU_BORDER_COLOR, anchor=W)
        tmpW.grid(column=0, row=0, columnspan=3, sticky=N + S + E + W)

        self._menuItems=[]
        i=1
        for menuItem in self._menuItemList:
            #Spacer
            self._menuItems.append(Label(self._parent))
            self._menuItems[-1].configure(text="", font=MENU_FONT, background=MENU_BG,
                                          foreground=MENU_FG, height=MENU_HEIGHT, width=2,
                                          highlightthickness=MENU_BORDER, highlightbackground=MENU_BORDER_COLOR,
                                          highlightcolor=MENU_BORDER_COLOR, anchor=W)
            self._menuItems[-1].grid(column=0, row=i, sticky=N + S + E + W)

            #Number
            iStr='%i' % i
            if i==10:
                iStr='0'
            self._menuItems.append(Label(self._parent))
            self._menuItems[-1].configure(text=iStr, font=MENU_FONT, background=MENU_KEY_BG,
                                          foreground=MENU_KEY_FG, height=MENU_HEIGHT, width=1,
                                          highlightthickness=MENU_BORDER, highlightbackground=MENU_BORDER_COLOR,
                                          highlightcolor=MENU_BORDER_COLOR, anchor=W)
            self._menuItems[-1].grid(column=1, row=i, sticky=N + S + E + W)

            #Item
            self._menuItems.append(Label(self._parent))
            self._menuItems[-1].configure(text=menuItem , font = MENU_FONT, background = MENU_BG,
                                          foreground=MENU_FG, height=MENU_HEIGHT, width = MENU_WIDTH,
                                          highlightthickness = MENU_BORDER, highlightbackground = MENU_BORDER_COLOR,
                                          highlightcolor = MENU_BORDER_COLOR, anchor=W)
            self._menuItems[-1].grid(column=2, row=i, sticky=N + S + E + W)
            i+=1

    def dataType(self):
        """

        :return: String indicating what's in the data pane
        """
        return "MENU-%s" % self._menuTitle

    def keyHandle(self,keyEvent):
        print "DATA KEY: %s - %s" % (keyEvent.keycode, keyEvent.char)


class TypeMenu(ALMenu):
    def __init__(self, uiObj, filterObj):
        self._typeList=[]
        for t in FILTER_TYPES:
            self._typeList.append(t)
        self._typeList.append('All')
        self._typeList.sort()
        super(TypeMenu, self).__init__(uiObj=uiObj, filterObj=filterObj, menuTitle='Catalog',
                                          menuItemList=self._typeList)
    def keyHandle(self,keyEvent):
        print "DATA KEY: %s - %s" % (keyEvent.keycode, keyEvent.char)
        num = int(keyEvent.char)

        if num > 0:
            self._filterObj._type=self._typeList[num-1]
        else:
            self._filterObj._type = self._typeList[9]
        self._uiObj.popStack()


class CatalogMenu(ALMenu):
    def __init__(self, uiObj, filterObj):
        super(CatalogMenu, self).__init__(uiObj=uiObj, filterObj=filterObj, menuTitle='Catalog',
                                          menuItemList=['ALL', 'NGC', 'Messier', 'Herschel', 'Caldwell', 'SAC',
                                                             'Obs List'])
    def keyHandle(self,keyEvent):
        print "DATA KEY: %s - %s" % (keyEvent.keycode, keyEvent.char)
        num = int(keyEvent.char)

        if num == 1:
            self._filterObj._catalog=None

        if num == 2:
            # NGC
            self._filterObj._catalog = 'NGC'

        if num == 3:
            # Messier
            self._filterObj._catalog = 'M'
            self._sortClause = 'OTHER'

        if num == 4:
            # Herschel
            self._filterObj._catalog = 'H'

        if num == 5:
            ##Caldwel
            self._filterObj._catalog = 'C'

        if num == 6:
            # SAC
            self._filterObj._catalog = 'B'

        if num == 7:
            # ObsList
            self._filterObj._catalog = 'ObsList'
        self._uiObj.popStack()

class FilterObj(object):
    def __init__(self):
        self._catalog=None
        self._type=None
        self._magnitude=None
        self._constellation=None
        self._sortClause = 'PREFIX, CAST(OBJECT AS INTEGER) ASC'

    def reset(self):
        self._catalog=None
        self._type=None
        self._magnitude=None
        self._constellation=None

    def __str__(self):
        return "%s/%s/%s/%s/%s" % (self._catalog, self._type, str(self._magnitude), self._constellation,
                                   self._sortClause)


class FilterMenu(ALMenu):
    def __init__(self, uiObj, filterObj):
        super(FilterMenu, self).__init__(uiObj=uiObj, filterObj=filterObj,menuTitle='Filter',
                                          menuItemList=['Reset', 'Catalog', 'Type', 'Const', 'Mag'])

    def _drawMenu(self):
        # TITLE
        tmpW=Label(self._parent)
        tmpW.configure(text=self._menuTitle, font=MENU_FONT, background=MENU_BG,
                                      foreground=MENU_FG, height=MENU_HEIGHT,
                                      highlightthickness=MENU_BORDER, highlightbackground=MENU_BORDER_COLOR,
                                      highlightcolor=MENU_BORDER_COLOR, anchor=W)
        tmpW.grid(column=0, row=0, columnspan=3, sticky=N + S + E + W)

        i=1
        for menuItem in self._menuItemList:
            #Spacer
            tmpW=Label(self._parent)
            tmpW.configure(text="", font=MENU_FONT, background=MENU_BG,
                                          foreground=MENU_FG, height=MENU_HEIGHT, width=2,
                                          highlightthickness=MENU_BORDER, highlightbackground=MENU_BORDER_COLOR,
                                          highlightcolor=MENU_BORDER_COLOR, anchor=W)
            tmpW.grid(column=0, row=i, sticky=N + S + E + W)

            #Number
            tmpW=Label(self._parent)
            tmpW.configure(text="%i" % i, font=MENU_FONT, background=MENU_KEY_BG,
                                          foreground=MENU_KEY_FG, height=MENU_HEIGHT, width=1,
                                          highlightthickness=MENU_BORDER, highlightbackground=MENU_BORDER_COLOR,
                                          highlightcolor=MENU_BORDER_COLOR, anchor=W)
            tmpW.grid(column=1, row=i, sticky=N + S + E + W)

            #Item
            tmpW=Label(self._parent)
            tmpW.configure(text=menuItem , font = MENU_FONT, background = MENU_BG,
                                          foreground=MENU_FG, height=MENU_HEIGHT, width=8,
                                          highlightthickness = MENU_BORDER, highlightbackground = MENU_BORDER_COLOR,
                                          highlightcolor = MENU_BORDER_COLOR, anchor=W)
            tmpW.grid(column=2, row=i, sticky=N + S + E + W)

            #Data
            dataStr=''
            if menuItem=='Catalog':
                if self._filterObj._catalog:
                    dataStr=self._filterObj._catalog
                else:
                    dataStr='All'

            if menuItem=='Type':
                dataStr=self._filterObj._type

            tmpW=Label(self._parent)
            tmpW.configure(text=dataStr, font=MENU_FONT, background=MENU_BG,
                                          foreground=MENU_FG, height=MENU_HEIGHT, width=MENU_WIDTH,
                                          highlightthickness=MENU_BORDER, highlightbackground=MENU_BORDER_COLOR,
                                          highlightcolor=MENU_BORDER_COLOR, anchor=W)
            tmpW.grid(column=3, row=i, sticky=N + S + E + W)


            i+=1


    def keyHandle(self, keyEvent):
        print "DATA KEY: %s - %s" % (keyEvent.keycode, keyEvent.char)
        num = int(keyEvent.char)

        if num==1:
            self._filterObj.reset()
            self.draw()

        if num==2:
            self._uiObj.pushStack(CatalogMenu(uiObj=self._uiObj, filterObj=self._filterObj))

        if num==3:
            self._uiObj.pushStack(TypeMenu(uiObj=self._uiObj, filterObj=self._filterObj))

class SortMenu(ALMenu):
    def __init__(self, uiObj, filterObj):
        super(SortMenu, self).__init__(uiObj=uiObj, filterObj=filterObj, menuTitle='Sort',
                                          menuItemList=['ObjID', 'Other', 'Type', 'Const', 'Mag', 'RA'])
    def keyHandle(self,keyEvent):
        print "DATA KEY: %s - %s" % (keyEvent.keycode, keyEvent.char)
        num = int(keyEvent.char)

        if num==1:
            self._filterObj._sortClause='PREFIX, CAST(OBJECT AS INTEGER) ASC'

        if num==2:
            self._filterObj._sortClause='OTHER, PREFIX, CAST(OBJECT AS INTEGER) ASC'

        if num==3:
            self._filterObj._sortClause = 'TYPE, PREFIX, CAST(OBJECT AS INTEGER) ASC'

        if num==4:
            self._filterObj._sortClause='CON, PREFIX, CAST(OBJECT AS INTEGER) ASC'

        if num==5:
            self._filterObj._sortClause='MAG ASC'

        if num==6:
            self._filterObj._sortClause = 'RA ASC'

        self._uiObj.popStack()


class AstroList(object):
    def __init__(self, parent):
        self._filterObj=FilterObj()
        self._parent = parent
        self._mainLayout = Frame(self._parent, height=600, width=510, background="#000000", takefocus=1)
        self._mainLayout.bind("<Key>", self._keyHandle)
        self._mainLayout.grid_propagate(0)
        self._mainLayout.grid()
        self._dataFrame=None
        self._dataStack=[]

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

        self._clearData()
        self._filterObj.reset()
        self._filterObj._catalog = 'NGC'
        self.pushStack(astroObjList.ALObjectInfo(self._filterObj, self.setButton, self.setStatus))
        self._mainLayout.focus_set()

    def setStatus(self, statusText):
        print "STATUS:" + statusText

    def setButton(self, buttonNo, buttonText):
        if buttonNo > 3 and buttonNo < 8:
            buttonText='\\n'.join(buttonText)
        eval('self.button%i.configure(text="%s")' % (buttonNo, buttonText))

    def _clearData(self):

        if self._dataFrame:
            self._dataFrame.destroy()
        self._dataFrame = Frame(self._mainLayout, height=DATA_HEIGHT, width=DATA_WIDTH)
        self._dataFrame.configure(background=DATA_BG)
        self._dataFrame.grid_propagate(0)
        self._dataFrame.grid(column=0, row=1, columnspan=4, rowspan=4)

    def popStack(self):
        if len(self._dataStack) > 1:
            self._clearData()
            self._dataStack.pop()
            self._dataStack[-1].draw(self._dataFrame)
            if len(self._dataStack)==1:
                self.setButton(8,'')

    def pushStack(self, dataObj):
        self._clearData()
        self._dataStack.append(dataObj)
        self._dataStack[-1].draw(self._dataFrame)
        if len(self._dataStack) > 1:
            self.setButton(8,'BACK')

    def _keyHandle(self, keyEvent):
        print "KEY: %s - %s" % (keyEvent.keycode,keyEvent.char)

        doType=self._dataStack[-1].dataType().split('-')[0]

        if keyEvent.keycode==KEY_B01:
            #Filter
            if doType=='FILTER':
                #Restore previous data objet
                self.popStack()

            else:

                self.pushStack(FilterMenu(self, self._filterObj))

        elif keyEvent.keycode==KEY_B02:
            #SORT
            if doType=='SORT':
                #Restore previous data objet
                self.popStack()
            else:
                self.pushStack(SortMenu(self, self._filterObj))

        elif keyEvent.keycode==KEY_B08:
            #Back
            self.popStack()


        elif keyEvent.keycode in KEY_NUM_LIST:
            #Numeric keys, decode for convinience
            num = KEY_NUM_LIST.index(keyEvent.keycode)
            keyEvent.char = str(num)

            self._dataStack[-1].keyHandle(keyEvent)

        else:
            #Pass through to data objects
            self._dataStack[-1].keyHandle(keyEvent)
