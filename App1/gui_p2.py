import Tkinter as tk
import time
import constants as cns

def main_layout():
	global frame2, p2
	p2=tk.Tk()
	p2.title('Main')
	p2.config(bg='white')	

	RWidth=p2.winfo_screenwidth()
	RHeight=p2.winfo_screenheight()
	SCR_SIZE=[RWidth-15,RHeight-80]

	p2.geometry(("%dx%d+%d+%d")%(SCR_SIZE[0],SCR_SIZE[1],5,5))	
	p2.resizable(0,0)

	frame1=tk.Frame(p2, bg='#000', width=SCR_SIZE[0], height=SCR_SIZE[1]*0.05)
	frame1.pack()
	frame1.place(y=0, relwidth=1, relheight=0.05)

	frame2=tk.Frame(p2, bg=cns.var_color['MAIN_TAB_ACT'], width=SCR_SIZE[0], height=SCR_SIZE[1]*0.8)	
	frame2.pack()
	frame2.place(y=SCR_SIZE[1]*0.05, relwidth=1, relheight=0.8)	

	but1=tk.Button(frame1, text='Files', bg=cns.var_color['MAIN_TAB_ACT'], bd=0, fg='white')
	but1.pack()
	but1.place(x=0, y=0.2*frame1.cget('height'), relwidth=0.2, relheight=0.8)

	but2=tk.Button(frame1, text='Other', bg=cns.var_color['MAIN_TAB_INACT'], bd=0, fg='white')
	but2.pack()
	but2.place(x=0.2*frame1.cget('width'), y=0.2*frame1.cget('height'), relwidth=0.2, relheight=0.8)


	aq=but1
	w=list(aq.keys())

	for t in w:		
		print t,aq.cget(t)



def main():

	main_layout()		

	p2.mainloop()
