from Tkinter import *
import Tkinter

top = Tkinter.Tk()

B1 = Tkinter.Button(top, text ="circle", relief=RAISED,\
                         cursor="watch")
B2 = Tkinter.Button(top, text ="plus", relief=RAISED,\
                         cursor="hand2")
B1.pack()
B2.pack()
top.mainloop()