from Tkinter import *

BUTTON_BG='#330000'
BUTTON_FG='#990000'
BUTTON_FONT=('Arial Unicode MS', -16, 'bold')
BUTTON_WIDTH=10
BUTTON_HEIGHT=2
BUTTON_BORDER=2
BUTTON_BORDER_COLOR='#000000'

DATA_FG='#EE1111'
DATA_BG='#000000'

class AstroList(object):
    def __init__(self, parent):
        self._parent = parent
        self._mainLayout = Frame(self._parent, height=600, width=510, background="#000000")
        self._mainLayout.grid_propagate(0)
        self._mainLayout.grid()

        self.button1 = Label(self._mainLayout )
        self.button1.configure(text="BACK", font=BUTTON_FONT, background=BUTTON_BG, foreground=BUTTON_FG,
                               height=BUTTON_HEIGHT, width=BUTTON_WIDTH, highlightthickness=BUTTON_BORDER,
                               highlightbackground=BUTTON_BORDER_COLOR, highlightcolor=BUTTON_BORDER_COLOR)
        self.button1.grid(column=0, row=0, sticky=N+S+E+W)

        self.button2 = Label(self._mainLayout )
        self.button2.configure(text="FILTER", font=BUTTON_FONT, background=BUTTON_BG, foreground=BUTTON_FG,
                               height=BUTTON_HEIGHT, width=BUTTON_WIDTH, highlightthickness=BUTTON_BORDER,
                               highlightbackground=BUTTON_BORDER_COLOR, highlightcolor=BUTTON_BORDER_COLOR)
        self.button2.grid(column=1, row=0, sticky=N+S+E+W)

        self.button3 = Label(self._mainLayout)
        self.button3.configure(text="", font=BUTTON_FONT, background=BUTTON_BG, foreground=BUTTON_FG,
                               height=BUTTON_HEIGHT, width=BUTTON_WIDTH, highlightthickness=BUTTON_BORDER,
                               highlightbackground=BUTTON_BORDER_COLOR, highlightcolor=BUTTON_BORDER_COLOR)
        self.button3.grid(column=2, row=0, sticky=N+S+E+W)

        self.button4 = Label(self._mainLayout)
        self.button4.configure(text="CLOSE", font=BUTTON_FONT, background=BUTTON_BG, foreground=BUTTON_FG,
                               height=BUTTON_HEIGHT, width=BUTTON_WIDTH, highlightthickness=BUTTON_BORDER,
                               highlightbackground=BUTTON_BORDER_COLOR, highlightcolor=BUTTON_BORDER_COLOR)
        self.button4.grid(column=3, row=0, columnspan=2, sticky=N+S+E+W)

        self.button5 = Label(self._mainLayout)
        self.button5.configure(text="", font=BUTTON_FONT, background=BUTTON_BG, foreground=BUTTON_FG,
                               height=BUTTON_HEIGHT * 4, width=6, highlightthickness=BUTTON_BORDER,
                               highlightbackground=BUTTON_BORDER_COLOR, highlightcolor=BUTTON_BORDER_COLOR)
        self.button5.grid(column=4, row=1, rowspan=2, sticky=N+S+E+W)

        self.button6 = Label(self._mainLayout)
        self.button6.configure(text="E\nN\nT\nE\nR", font=BUTTON_FONT, background=BUTTON_BG, foreground=BUTTON_FG,
                               height=BUTTON_HEIGHT * 4, width=6, highlightthickness=BUTTON_BORDER,
                               highlightbackground=BUTTON_BORDER_COLOR, highlightcolor=BUTTON_BORDER_COLOR)
        self.button6.grid(column=4, row=3, rowspan=2, sticky=N+S+E+W)

        self.cornerSpace=Label(self._mainLayout)
        self.cornerSpace.configure(text="", font=BUTTON_FONT, background=DATA_BG, foreground=DATA_FG,
                                   height=BUTTON_HEIGHT, width=6, highlightthickness=BUTTON_BORDER,
                                   highlightbackground=BUTTON_BORDER_COLOR, highlightcolor=BUTTON_BORDER_COLOR)
        self.cornerSpace.grid(column=5, row=5)

        self._dataFrame = Frame(self._mainLayout, height=554, width=440)
        self._dataFrame.configure(background='#111111')
        self._dataFrame.grid_propagate(0)
        self._dataFrame.grid(column=0, row=1, columnspan=4, rowspan=5)


