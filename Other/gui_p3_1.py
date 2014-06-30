import Tkinter as tk
import time
import constants as cns
import browse



# def main_layout(window):	

# 	frame=[]

# 	frame.append(tk.Frame(window, bg='#000', width=cns.var_scr_size[0][0], height=cns.var_scr_size[0][1]*0.05))
# 	frame[0].pack()
# 	frame[0].place(y=0, relwidth=1, relheight=0.05)

# 	frame.append(tk.Frame(window, bg=cns.var_color['MAIN_TAB_ACT'], width=cns.var_scr_size[0][0], height=cns.var_scr_size[0][1]*0.8))
# 	frame[1].pack()
# 	frame[1].place(y=cns.var_scr_size[0][1]*0.05, relwidth=1, relheight=0.8)	

# 	but=[[]]

# 	but[0].append(tk.Button(frame[0], text='Fil!!!', command= lambda: browse.browse(0,frame)))
# 	but[0].append(tk.Button(frame[0], text='Otherss', command= lambda: browse.browse(1,frame)))
    
# 	i=0
# 	for e_but in but[0]:
# 		e_but.config(bg=cns.var_color['MAIN_TAB_INACT'],bd=0, fg='white')
# 		e_but.pack()
# 		e_but.place(x=i*0.2*frame[0].cget('width'), y=0.2*frame[0].cget('height'), relwidth=0.2, relheight=0.8)
# 		i+=1
	



def main(window):

	main_layout(window)		

	window.mainloop()
