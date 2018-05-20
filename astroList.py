from Tkinter import *
import astroListUI

reload(astroListUI)

def goAstro():
    """
    Main function for runing app
    :return:
    """

    root=Tk()

    alUI=astroListUI.AstroList(root)

    root.mainloop()




if __name__=='__main__':
    goAstro()
