from win32api import GetSystemMetrics

RWidth=GetSystemMetrics(0)
RHeight=GetSystemMetrics(1)

var_mimetype={

	'MIME_TYPE_FOLDER'	:	'application/vnd.google-apps.folder',
	'MIME_TYPE_XLS'		:	'application/x-msexcel'
}

var_color={

	'MAIN_TAB_BACK'		:	'#000',
	'MAIN_TAB_ACT'		:	'#111',
	'MAIN_TAB_INACT'	:	'#333',
	'FG'				:	'#fff'
}			

var_tab0_clr={
	
	'FRAME_0'			:	'#ff0',
	'FRAME_1'			:	'#080',
	'FG'				:	'#fff',
	'RIBBON_BACK'		:	'#222'
}

var_font={
	
	'RIBBON_BUT'		:	('Arial', '12', 'bold')
}

var_scr_size=[
				[RWidth-15,RHeight-80]				
]