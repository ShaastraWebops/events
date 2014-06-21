import Tkinter as tk
import time
import os
import comm_1
# import requests

# requests.get('https://github.com',verify=True)

p1=tk.Tk()
p1.title('Login')
p1.iconbitmap(default='icon/penguin_1.ico')

SCR_SIZE=[500,250]

RWidth=p1.winfo_screenwidth()
RHeight=p1.winfo_screenheight()
p1.geometry(("%dx%d+%d+%d")%(SCR_SIZE[0],SCR_SIZE[1],(RWidth-SCR_SIZE[0])/2,(RHeight-SCR_SIZE[1])/2))	
p1.resizable(0,0)

def but1_callback():		
	t=time.time()
	comm_1.main()
	print time.time()-t
	#os.system('python start.py')
	p1.destroy()

but1=tk.Button(p1, text='Login', command=but1_callback)
but1.pack()
but1.place(bordermode=tk.OUTSIDE, width=100, height=50, x=(SCR_SIZE[0]-100)/2, y=(SCR_SIZE[1]-50)/2)


p1.mainloop()

