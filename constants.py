# from win32api import GetSystemMetrics

# RWidth=GetSystemMetrics(0)
# RHeight=GetSystemMetrics(1)

import Tkinter as tk
import os

try:
	r=tk.Tk()
	RWidth=r.winfo_screenwidth()
	RHeight=r.winfo_screenheight()
	r.destroy()
except:
	pass

var_mimetype={

	"xls"     :   	'application/vnd.ms-excel',
    "xlsx"    :    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    "xml"     :    'text/xml',
    "ods"     :    'application/vnd.oasis.opendocument.spreadsheet',
    "csv"     :    'text/plain',
    "tmpl"    :    'text/plain',
    "pdf"     :    'application/pdf',
    "php"     :    'application/x-httpd-php',
    "jpg"     :    'image/jpeg',
    "png"     :    'image/png',
    "gif"     :    'image/gif',
    "bmp"     :    'image/bmp',
    "txt"     :    'text/plain',
    "doc"     :    'application/msword',
    "js"      :    'text/js',
    "swf"     :    'application/x-shockwave-flash',
    "mp3"     :    'audio/mpeg',
    "zip"     :    'application/zip',
    "rar"     :    'application/rar',
    "tar"     :    'application/tar',
    "arj"     :    'application/arj',
    "cab"     :    'application/cab',
    "html"    :    'text/html',
    "htm"     :    'text/html',
    "default" :    'application/octet-stream',
    "folder"  :    'application/vnd.google-apps.folder'
}

var_color={

	'MAIN_TAB_BACK'		:	'#000',
	'MAIN_TAB_ACT'		:	'#111',
	'MAIN_TAB_INACT'	:	'#333',
	'FG'				:	'#fff'
}			

var_tab0_clr={
	
	'FRAME_0'			:	'#ff0',
	'FRAME_1'			:	'#fff',
	'FG'				:	'#000',
	'RIBBON_BACK'		:	'#fff'
}

var_font={
	
	'RIBBON_BUT'		:	('Arial', '12', 'bold')
}

var_scr_size=[
				[RWidth-15,RHeight-80]				
]

fil_name={
	'T_ON_OLD' : os.path.join('Info', 'total_online_list_old.json'),
	'T_ON_NEW' : os.path.join('Info', 'total_online_list_new.json'),
	'T_OFF_OLD' : os.path.join('Info', 'total_offline_list_old.json'),
	'T_OFF_NEW' : os.path.join('Info', 'total_offline_list_new.json')
}