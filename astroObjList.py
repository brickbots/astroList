from alConfig import *
from Tkinter import *
from alConstants import *
import alUtils
from PIL import Image, ImageTk, ImageFont, ImageDraw
import os

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

    def _showImage(self, parent):
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
            #ImageDraw.Draw(self._imageObj)


            self._imageObj = ImageTk.PhotoImage(imgObj)

            # get the image size
            w = self._imageObj.width()
            h = self._imageObj.height()
            self._imagePanel = Label(parent, image=self._imageObj, width=w, height=h, background=DATA_BG, anchor=W)
            self._imagePanel.grid(row=0, column=0, sticky=W + E + N + S)

    def _showDetails(self, parent):
        # Type
        tmpW = Label(parent)
        tmpW.configure(text='Type:', font=OBJ_LABEL_FONT, foreground=DATA_FG,
                       background=DATA_BG)
        tmpW.grid(row=0, column=0, sticky=W + E)
        tmpW = Label(self._layout)
        tmpW.configure(text=OBJ_TYPES[self._oInfo('TYPE')], font=OBJ_DATA_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=W)
        tmpW.grid(row=0, column=1, columnspan=3, sticky=W + E)

        # CONST
        tmpW = Label(self._layout)
        tmpW.configure(text='Const:', font=OBJ_LABEL_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=E)
        tmpW.grid(row=1, column=0, sticky=W + E)
        tmpW = Label(self._layout)
        tmpW.configure(text=CONSTELLATIONS[self._oInfo('CON')], font=OBJ_DATA_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=W, width=45)
        tmpW.grid(row=1, column=1, columnspan=3, sticky=W + E)

        # notes

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

        #Detail container
        self._detailsLayout=Frame(self._layout)
        self._detailsLayout.configure(background=DATA_BG, width=DATA_WIDTH, height=DATA_HEIGHT - 90)

        self._detailsLayout.grid_propagate(0)
        self._detailsLayout.grid(sticky=N+S+E+W)

        self._showImage(self._detailsLayout)

        return

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