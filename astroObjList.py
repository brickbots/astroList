from alConfig import *
from Tkinter import *
from alConstants import *
import alUtils
from PIL import Image, ImageTk, ImageFont, ImageDraw
import os

class ALObjectInfo(object):
    def __init__(self, parent, filterObject, buttonMethod, statusMethod):
        self._parent=parent
        self._filter=filterObject
        self._objectList=[]
        self._buttonMethod=buttonMethod
        self._statusMethod=statusMethod
        self._listIndex=0
        self._mode=0 #0= DEtails, 1= Image!
        self._createLayout()
        self._getList()
        self._prefixes=MAIN_PREFIXES
        self._searchPrefixIndex=3
        self._searchObject=''
        self._disiplayMode='info'
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

    def _showSearch(self, parent):
        self._buttonMethod(5, 'ESC')
        self._buttonMethod(6, 'SEARCH')

        tmpW = Label(parent)
        tmpW.configure(text=self._prefixes[self._searchPrefixIndex], font=OBJ_NAME_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=E, height=5, width=10)
        tmpW.grid(row=0, column=0, sticky=W + E + N + S)

        tmpW = Label(parent)
        tmpW.configure(text=self._searchObject, font=OBJ_NAME_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=W)
        tmpW.grid(row=0, column=1, sticky=W + E + N + S)


    def _showImage(self, parent):
        self._buttonMethod(5,'INFO')

        # Add image
        imageName=self._oInfo('PREFIX') + self._oInfo('OBJECT')
        imageFile = '%s/%s.png' % (PICTURE_PATH, imageName)

        if not os.path.exists(imageFile):

            imageName = self._oInfo('OTHER').replace(' ','')
            imageFile = '%s/%s.png' % (PICTURE_PATH, imageName)

        if os.path.exists(imageFile):

            imgObj=Image.open(imageFile).convert('RGB')

            #Add object dimensions
            font = ImageFont.truetype(IMAGE_SIZE_FONT[0], IMAGE_SIZE_FONT[1])

            # Drawing the text on the picture
            if self._oInfo('SIZE_MIN') <> '':
                sizeString="%s x %s" % (self._oInfo('SIZE_MAX'), self._oInfo('SIZE_MIN'))
            else:
                sizeString=self._oInfo('SIZE_MAX')

            draw = ImageDraw.Draw(imgObj)
            draw.text((280,400), sizeString, fill=(220,0,0), font=font)

            self._imageObj = ImageTk.PhotoImage(imgObj)

            # get the image size
            w = self._imageObj.width()
            h = self._imageObj.height()
            self._imagePanel = Label(parent, image=self._imageObj, width=w, height=h, background=DATA_BG, anchor=W)
            self._imagePanel.grid(row=0, column=0, sticky=W + E + N + S)

    def _showDetails(self, parent):
        self._buttonMethod(5,'IMAGE')

        # Type
        tmpW = Label(parent)
        tmpW.configure(text='Type:', font=OBJ_LABEL_FONT, foreground=DATA_FG,
                       background=DATA_BG)
        tmpW.grid(row=0, column=0, sticky=W + E)

        tmpW = Label(parent)
        tmpW.configure(text=OBJ_TYPES[self._oInfo('TYPE')], font=OBJ_DATA_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=W)
        tmpW.grid(row=0, column=1, columnspan=3, sticky=W + E)

        # CONST
        tmpW = Label(parent)
        tmpW.configure(text='Const:', font=OBJ_LABEL_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=E)
        tmpW.grid(row=1, column=0, sticky=W + E)
        tmpW = Label(parent)
        tmpW.configure(text=CONSTELLATIONS[self._oInfo('CON')], font=OBJ_DATA_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=W, width=45)
        tmpW.grid(row=1, column=1, columnspan=3, sticky=W + E)

        # notes

    def draw(self, newParent=None):
        #Set buttons
        self._buttonMethod(6,'CHART')

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

        #Detail container
        self._detailsLayout=Frame(self._layout)
        self._detailsLayout.configure(background=DATA_BG, width=DATA_WIDTH, height=DATA_HEIGHT - 90)

        self._detailsLayout.grid_propagate(0)
        self._detailsLayout.grid(sticky=N+S+E+W)

        if self._disiplayMode=='info':
            self._showDetails(self._detailsLayout)
        if self._disiplayMode=='image':
            self._showImage(self._detailsLayout)
        if self._disiplayMode=='search':
            self._showSearch(self._detailsLayout)

        return

    def findItem(self, prefix, object):
        for i in range(0,len(self._objectList)):
            if self._objectList[i][0]==prefix and self._objectList[i][1]==object:
                self._listIndex=i
                return True
            if self._objectList[i][2]=='%s %s' % (prefix, object):
                self._listIndex = i
                return True

        return False

    def _getPrefixes(self):
        self._prefixes=alUtils.executeQuery('SELECT DISTINCT PREFIX FROM OBJECTS ORDER BY PREFIX')

    def _getList(self):
        #need to do filtering here, but for now, get the WHOLE list
        self._objectList=alUtils.executeQuery("SELECT * FROM OBJECTS ORDER BY MAG")
        self._listIndex=0

    def keyHandle(self,keyEvent):
        print "DATA KEY: %s - %s" % (keyEvent.keycode, keyEvent.char)

        if keyEvent.keycode==KEY_B03:
            if self._disiplayMode=='search':
                self._searchPrefixIndex-=1
                if self._searchPrefixIndex < 0:
                    self._searchPrefixIndex=0
            else:
                self._listIndex-=1
                if self._listIndex < 0:
                    self._listIndex=0
        elif keyEvent.keycode==KEY_B04:
            if self._disiplayMode=='search':
                self._searchPrefixIndex+=1
                if self._searchPrefixIndex > len(self._prefixes)-1:
                    self._searchPrefixIndex=len(self._prefixes)-1
            else:
                self._listIndex+=1
                if self._listIndex > len(self._objectList) - 1:
                    self._listIndex=len(self._objectList) - 1

        elif keyEvent.keycode==KEY_B05:
            self._searchObject = ''
            if self._disiplayMode=='info':
                self._disiplayMode='image'
            else:
                self._disiplayMode='info'
        elif keyEvent.keycode == KEY_B06 and self._disiplayMode=='search':
            if self.findItem(self._prefixes[self._searchPrefixIndex], self._searchObject):
                self._disiplayMode='info'
                self._searchObject='' #reset for next search
            else:
                self._statusMethod('Could not find object')
                self._searchObject=''
        else:
            #Numeric?
            if keyEvent.char.isdigit:
                self._disiplayMode='search'
                self._searchObject+=keyEvent.char

        self.draw()

    def dataType(self):
        return "OBJECT"