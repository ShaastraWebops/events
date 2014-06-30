import Tkinter as tk
import constants as cns
import tab_0
import tab_1
import os

tab=[tab_0.main,tab_1.main]

def main_layout(window,tab_no):	

	frame=[]

	frame.append(tk.Frame(window, bg=cns.var_color['MAIN_TAB_BACK'], width=cns.var_scr_size[0][0], height=cns.var_scr_size[0][1]*0.05))
	frame[0].pack()
	frame[0].place(y=0, relwidth=1, relheight=0.05)

	frame.append(tk.Frame(window, bg=cns.var_color['MAIN_TAB_ACT'], width=cns.var_scr_size[0][0], height=cns.var_scr_size[0][1]*0.95))
	frame[1].pack()
	frame[1].place(y=cns.var_scr_size[0][1]*0.05, relwidth=1, relheight=0.95)	

	but=[[]]

	but[0].append(tk.Button(frame[0], text='Files', command= lambda: browse(0,frame)))
	but[0].append(tk.Button(frame[0], text='Others', command= lambda: browse(1,frame)))
    	
	for e_but in but[0]:
		i=but[0].index(e_but)
		if i==tab_no:
			e_but.config(bg=cns.var_color['MAIN_TAB_ACT'],bd=0, fg=cns.var_color['FG'])
		else:
			e_but.config(bg=cns.var_color['MAIN_TAB_INACT'],bd=0, fg=cns.var_color['FG'])

		e_but.pack()
		e_but.place(x=i*0.2*frame[0].cget('width'), y=0.2*frame[0].cget('height'), relwidth=0.2, relheight=0.8)	

	return frame	



def browse(tab_no,parent):		
	for each in parent:
		each.destroy()		

	frame=main_layout(p2,tab_no)
	tab[tab_no](frame[1])

def main():

	global p2
	p2 = tk.Tk()
	p2.title('Main')
	p2.config(bg='white')	
	if 'nt' == os.name:
		p2.iconbitmap(default='icon/penguin_1.ico')
	p2.tk.call('wm')

	p2.geometry(("%dx%d+%d+%d")%(cns.var_scr_size[0][0],cns.var_scr_size[0][1],5,5))	
	p2.resizable(0,0)

	browse(0,[])	

	p2.mainloop()