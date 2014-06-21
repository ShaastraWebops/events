import Tkinter as tk
import time
import os

def main():
	p2=tk.Tk()
	p2.title('Main')
	p2.iconbitmap(default='icon/penguin_1.ico')

	RWidth=p2.winfo_screenwidth()
	RHeight=p2.winfo_screenheight()
	SCR_SIZE=[RWidth-15,RHeight-80]

	p2.geometry(("%dx%d+%d+%d")%(SCR_SIZE[0],SCR_SIZE[1],5,5))	
	p2.resizable(0,0)

	p2.mainloop()