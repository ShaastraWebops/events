import Tkinter as tk
import constants as cns
from encoder_beta3 import encoder

class ribbon:
	
	def __init__(self, parent, index, fileob):
		self.parent=parent
		self.index=index
		self.fileob=fileob

		thickness=int(self.parent.cget('height')*0.1)

		self.frame=tk.Frame(self.parent, width=self.parent.cget('width'), height=thickness,
						bd=1, relief=tk.RAISED, bg=cns.var_tab0_clr['RIBBON_BACK'])
		self.frame.pack()
		self.frame.place(x=0, y=self.index*thickness, 
						width=self.frame.cget('width'), height=self.frame.cget('height'))

		self.chk1_var=tk.IntVar()
		self.chk1=tk.Checkbutton(self.frame, variable=self.chk1_var, bg=self.frame.cget('bg'))
		self.chk1.pack(side=tk.LEFT)

		self.but1=tk.Button(self.frame, text=fileob['title'], bg=self.frame.cget('bg'), bd=1,
						fg=cns.var_tab0_clr['FG'], cursor='hand2', relief=tk.FLAT,
						anchor=tk.W, justify=tk.LEFT, font=cns.var_font['RIBBON_BUT'],
						width=int(self.frame.cget('width')*0.3), height=int(0.8*thickness),
						command=self.but1_callback)		
		self.but1.pack()
		self.but1.place(x=30, y=int(0.1*thickness), width=self.but1.cget('width'), height=self.but1.cget('height'))

		self.but2=tk.Button(self.frame, text='trial')
		self.but2.pack(side=tk.RIGHT)
	
	def but1_callback(self):
		print 'but1_callback'
		print self.chk1_var.get()
		print cns.var_scr_size[0]




def main(parent):

	clrance=0.01*parent.cget('width')

	frame=[];	
	frame.append(tk.Frame(parent, bg=cns.var_tab0_clr['FRAME_0'], 
				width=parent.cget('width')-2*clrance, height=0.1*parent.cget('height')))
	frame[0].pack()
	frame[0].place(x=clrance, y=clrance, 
				width=frame[0].cget('width'), height=frame[0].cget('height'))

	frame.append(tk.Frame(parent, bg=cns.var_tab0_clr['FRAME_1'], 
				width=parent.cget('width')-2*clrance, height=parent.cget('height')-frame[0].cget('height')-3*clrance))
	frame[1].pack()
	frame[1].place(x=clrance, y=2*clrance+frame[0].cget('height'), 
				width=frame[1].cget('width'), height=frame[1].cget('height'))

	rib1=ribbon(frame[1], 0, {'title':'Shagun'})
	rib1=ribbon(frame[1], 1, {'title':'Agarwal'})

