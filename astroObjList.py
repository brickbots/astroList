from alConfig import *
from Tkinter import *
from alConstants import *
import alUtils
from astropy.io import fits
from PIL import Image, ImageTk, ImageFont, ImageDraw
import os
import alSkyChart
import textwrap
import math

def getObsListItems():
    objList=[]
    baseList=alUtils.loadObsList(OBSLIST_PATH)
    for item in baseList:
        print item
        cat=item.split(' ')[0]
        objID=item.split(' ')[1]
        queryString = "SELECT * FROM OBJECTS WHERE (PREFIX='%s' AND OBJECT='%s') OR OTHER='%s'" % (cat, objID, item)

        tmpRet=alUtils.executeQuery(queryString)
        if len(tmpRet) > 0:
            objList.append(tmpRet[0])

    return objList


class ALObjectInfo(object):
    def __init__(self, filterObject, buttonMethod, statusMethod):
        self._parent=None
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
        self._skyChart=None
        self._currentFilterHash=None
        self._gammaIndex=2


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
        self._buttonMethod(6, 'ESC')
        self._buttonMethod(7, 'GO!')

        tmpW = Label(parent)
        tmpW.configure(text=self._prefixes[self._searchPrefixIndex], font=OBJ_NAME_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=E, height=5, width=10)
        tmpW.grid(row=0, column=0, sticky=W + E + N + S)

        tmpW = Label(parent)
        tmpW.configure(text=self._searchObject, font=OBJ_NAME_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=W)
        tmpW.grid(row=0, column=1, sticky=W + E + N + S)


    def _showImage(self, parent):
        self._buttonMethod(6,'INFO')
        self._buttonMethod(7,'LOG')
        self._buttonMethod(9,'GAMMA')

        # Add image
        imageName=self._oInfo('PREFIX') + self._oInfo('OBJECT')
        imageFile = '%s/%s.fit' % (PICTURE_PATH, imageName)

        if not os.path.exists(imageFile):

            imageName = self._oInfo('OTHER').replace(' ','')
            imageFile = '%s/%s.fit' % (PICTURE_PATH, imageName)

        if os.path.exists(imageFile):

            #imgObj=Image.open(imageFile).convert('RGB')

            image_file = fits.open(imageFile)
            image_array = image_file[0].data

            imgSize=440
            img = Image.fromarray(image_array, 'L')
            img = img.resize((imgSize, imgSize), resample=Image.BICUBIC)

            img = Image.eval(img, lambda x: math.pow((float(x) / 255), GAMMA_LIST[self._gammaIndex]) * 255)
            bandList = [img, Image.new('L', (imgSize,imgSize)),
                        Image.new('L', (imgSize,imgSize))]

            imgObj = Image.merge('RGB', bandList)



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

    def _formatCats(self, cats):
        catList=['B','M', 'H', 'C']

        catString=''.join(catList)

        for c in catList:
            if c not in cats:
                catString=catString.replace(c, ' ')

        return catString

    def _decodeNGC(self, ngcString):
        """
        Decodes NGC Description code to more legible equiv
        :param ncgString:
        :return: String with readable descriptions, already line broken
        """

        descriptions=[]
        pPrefix=False
        for code in ngcString.split(';'):
            prefix=''
            if code=='p':
                pPrefix=True
            else:
                if pPrefix:
                    pPrefix=False
                    if code in ['F','B','L','S']:
                        prefix='pretty '
                    else:
                        prefix='preceding '

                descriptions.append(prefix + NGC_CODES.get(code,code))

        return textwrap.fill(', '.join(descriptions), 40)


    def _showDetails(self, parent):
        self._buttonMethod(6,'IMAGE')
        self._buttonMethod(7,'LOG')
        self._buttonMethod(9, '')

        tmpRow=0

        # Type / RA
        tmpW = Label(parent)
        tmpW.configure(text='Type:', font=OBJ_LABEL_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=E)
        tmpW.grid(row=tmpRow, column=0, sticky=W + E)
        tmpW = Label(parent)
        tmpW.configure(text=OBJ_TYPES.get(self._oInfo('TYPE'), 'OTHER'), font=OBJ_DATA_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=W, width=19)
        tmpW.grid(row=tmpRow, column=1, sticky=W + E)

        tmpW = Label(parent)
        tmpW.configure(text='RA:', font=OBJ_LABEL_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=E)
        tmpW.grid(row=tmpRow, column=2, sticky=W + E)
        tmpW = Label(parent)
        tmpW.configure(text=self._oInfo('RA'), font=OBJ_DATA_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=W)
        tmpW.grid(row=tmpRow, column=3, sticky=W + E)
        tmpRow+=1

        # CONST / DEC
        tmpW = Label(parent)
        tmpW.configure(text='Const:', font=OBJ_LABEL_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=E)
        tmpW.grid(row=tmpRow, column=0, sticky=W + E)
        tmpW = Label(parent)
        tmpW.configure(text=CONSTELLATIONS[self._oInfo('CON')], font=OBJ_DATA_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=W)
        tmpW.grid(row=tmpRow, column=1,  sticky=W + E)

        tmpW = Label(parent)
        tmpW.configure(text='DEC:', font=OBJ_LABEL_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=E)
        tmpW.grid(row=tmpRow, column=2, sticky=W + E)
        tmpW = Label(parent)
        tmpW.configure(text=self._oInfo('DEC'), font=OBJ_DATA_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=W)
        tmpW.grid(row=tmpRow, column=3,  sticky=W + E)
        tmpRow += 1

        # Line Break
        tmpW = Label(parent)
        tmpW.configure(text='', font=OBJ_DATA_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=W)
        tmpW.grid(row=tmpRow, column=0, columnspan=4, sticky=W + E)
        tmpRow += 1


        # Size / Mag
        if self._oInfo('SIZE_MIN') <> '':
            sizeString = "%s x %s" % (self._oInfo('SIZE_MAX'), self._oInfo('SIZE_MIN'))
        else:
            sizeString = self._oInfo('SIZE_MAX')

        tmpW = Label(parent)
        tmpW.configure(text='Size:', font=OBJ_LABEL_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=E)
        tmpW.grid(row=tmpRow, column=0, sticky=W + E)
        tmpW = Label(parent)
        tmpW.configure(text=sizeString, font=OBJ_DATA_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=W)
        tmpW.grid(row=tmpRow, column=1,  sticky=W + E)

        tmpW = Label(parent)
        tmpW.configure(text='Mag:', font=OBJ_LABEL_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=E)
        tmpW.grid(row=tmpRow, column=2, sticky=W + E)
        tmpW = Label(parent)
        tmpW.configure(text=self._oInfo('MAG'), font=OBJ_DATA_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=W)
        tmpW.grid(row=tmpRow, column=3,  sticky=W + E)
        tmpRow += 1

        # PA / SBright
        tmpW = Label(parent)
        tmpW.configure(text='Angle:', font=OBJ_LABEL_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=E)
        tmpW.grid(row=tmpRow, column=0, sticky=W + E)
        tmpW = Label(parent)
        tmpW.configure(text=self._oInfo('PA'), font=OBJ_DATA_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=W)
        tmpW.grid(row=tmpRow, column=1, sticky=W + E)

        tmpW = Label(parent)
        tmpW.configure(text='Surf:', font=OBJ_LABEL_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=E)
        tmpW.grid(row=tmpRow, column=2, sticky=W + E)
        tmpW = Label(parent)
        tmpW.configure(text=self._oInfo('SUBR'), font=OBJ_DATA_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=W)
        tmpW.grid(row=tmpRow, column=3, sticky=W + E)
        tmpRow += 1


        # CLassification / catalogs
        tmpW = Label(parent)
        tmpW.configure(text='Class:', font=OBJ_LABEL_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=E)
        tmpW.grid(row=tmpRow, column=0, sticky=W + E)
        tmpW = Label(parent)
        tmpW.configure(text=self._oInfo('CLASS'), font=OBJ_DATA_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=W)
        tmpW.grid(row=tmpRow, column=1, sticky=W + E)

        tmpW = Label(parent)
        tmpW.configure(text='Cats:', font=OBJ_LABEL_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=E)
        tmpW.grid(row=tmpRow, column=2, sticky=W + E)
        tmpW = Label(parent)
        tmpW.configure(text=self._formatCats(self._oInfo('BCHM')), font=OBJ_MONO_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=S)
        tmpW.grid(row=tmpRow, column=3, sticky=W + E)
        tmpRow += 1

        #Line Break
        tmpW = Label(parent)
        tmpW.configure(text='', font=OBJ_DATA_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=W)
        tmpW.grid(row=tmpRow, column=0, columnspan=4, sticky=W + E)
        tmpRow += 1

        #NGC Codes
        tmpW = Label(parent)
        tmpW.configure(text='NGC:', font=OBJ_LABEL_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=W)
        tmpW.grid(row=tmpRow, column=0, sticky=W + E)
        tmpRow += 1
        tmpW = Label(parent)
        tmpW.configure(text=self._decodeNGC(self._oInfo('NGC_DESCR')), font=OBJ_DATA_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=W)
        tmpW.grid(row=tmpRow, column=0, columnspan=4, sticky=W + E)
        tmpRow += 1

        #Line Break
        tmpW = Label(parent)
        tmpW.configure(text='', font=OBJ_DATA_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=W)
        tmpW.grid(row=tmpRow, column=0, columnspan=4, sticky=W + E)
        tmpRow += 1

        # notes
        tmpW = Label(parent)
        tmpW.configure(text='Notes:', font=OBJ_LABEL_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=W)
        tmpW.grid(row=tmpRow, column=0, sticky=W + E)
        tmpRow += 1

        tmpW = Label(parent)
        tmpW.configure(text=textwrap.fill(self._oInfo('NOTES'), 40), font=OBJ_DATA_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=W)
        tmpW.grid(row=tmpRow, column=0, columnspan=4, sticky=W + E)



    def draw(self, newParent=None):
        #Set buttons
        self._buttonMethod(3,'CHART')
        self._buttonMethod(4, 'UP')
        self._buttonMethod(5, 'DOWN')
        self._buttonMethod(8, '')
        self._buttonMethod(7, 'LOG')

        if newParent:
            self._parent = newParent
        else:
            self._layout.destroy()

        #check if filter or sort have changed....
        if str(self._filter) <> self._currentFilterHash:
            self._getList()

        self._createLayout()

        #OBject Name
        tmpW=Label(self._layout)
        tmpS=self._oInfo('PREFIX') + ' ' + self._oInfo('OBJECT')
        tmpW.configure(text=tmpS.strip(), font=OBJ_NAME_FONT,
                       foreground=DATA_FG_BRIGHT, background=DATA_BG, anchor=W)
        tmpW.grid(row=0,column=0, sticky=W + E)


        #Alternate NAme
        tmpW = Label(self._layout)
        tmpW.configure(text=self._oInfo('OTHER'), font=OBJ_NAME_FONT, foreground=DATA_FG,
                       background=DATA_BG, anchor=E)
        tmpW.grid(row=0, column=1, sticky=W + E)

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
        self._detailsLayout.configure(background=DATA_BG, width=DATA_WIDTH, height=DATA_HEIGHT - 45)

        self._detailsLayout.grid_propagate(0)
        self._detailsLayout.grid(row=1, column=0, columnspan=2, sticky=N+S+E+W)

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
        whereClause=''
        clauseList=[]
        if self._filter._catalog:
            #SPECIAL CASES
            if self._filter._catalog=='ObsList':
                self._objectList=getObsListItems()
                self._listIndex = 0
                self._currentFilterHash = str(self._filter)
                return

            if self._filter._catalog in ['M','C','B','H']:
                clauseList.append("BCHM LIKE '%%%s%%'" % self._filter._catalog)
            else:
                clauseList.append("PREFIX='%s'" % self._filter._catalog)

        if self._filter._magnitude:
            clauseList.append("MAG > %f" % self._filter._magnitude)

        if self._filter._constellation:
            clauseList.append("CONST='%s'" % self._filter._constellation)

        if self._filter._type:
            clauseList.append("TYPE='%s'" % self._filter._type)

        if len(clauseList) > 0:
            whereClause='WHERE ' + ' AND '.join(clauseList)

        self._queryString="SELECT * FROM OBJECTS %s ORDER BY %s" % (whereClause, self._filter._sortClause)
        print "QS: %s" % self._queryString
        self._objectList=alUtils.executeQuery(self._queryString)
        self._listIndex=0
        self._currentFilterHash=str(self._filter)

    def keyHandle(self,keyEvent):
        print "DATA KEY: %s - %s" % (keyEvent.keycode, keyEvent.char)

        if keyEvent.keycode==KEY_B04:
            if self._disiplayMode=='search':
                self._searchPrefixIndex-=1
                if self._searchPrefixIndex < 0:
                    self._searchPrefixIndex=0
            else:
                self._listIndex-=1
                if self._listIndex < 0:
                    self._listIndex=0
        elif keyEvent.keycode==KEY_B05:
            if self._disiplayMode=='search':
                self._searchPrefixIndex+=1
                if self._searchPrefixIndex > len(self._prefixes)-1:
                    self._searchPrefixIndex=len(self._prefixes)-1
            else:
                self._listIndex+=1
                if self._listIndex > len(self._objectList) - 1:
                    self._listIndex=len(self._objectList) - 1

        elif keyEvent.keycode==KEY_B06:
            self._searchObject = ''
            if self._disiplayMode=='info':
                self._disiplayMode='image'
            else:
                self._disiplayMode='info'
        elif keyEvent.keycode == KEY_B07 and self._disiplayMode=='search':
            if self.findItem(self._prefixes[self._searchPrefixIndex], self._searchObject):
                self._disiplayMode='info'
                self._searchObject='' #reset for next search
            else:
                self._statusMethod('Could not find object')
                self._searchObject=''
        elif keyEvent.keycode == KEY_B03 and self._disiplayMode <> 'search':
            #Go to on chart
            objID=self._oInfo('PREFIX') + self._oInfo('OBJECT')
            if not self._skyChart:
                self._skyChart=alSkyChart.SkyChartControl()

            self._skyChart.findObject(objID.upper())
            self._skyChart.setFOV(40)
        elif keyEvent.keycode == KEY_B09 and self._disiplayMode=='image':
            self._gammaIndex -= 1
            if self._gammaIndex < 0:
                self._gammaIndex= len(GAMMA_LIST) -1

            self.draw()

        else:
            #Numeric?
            if keyEvent.char.isdigit:
                self._disiplayMode='search'
                self._searchObject+=keyEvent.char

        self.draw()

    def dataType(self):
        return "OBJECT"