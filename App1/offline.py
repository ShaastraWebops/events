import os
import glob
import json
import time
import constants as cns

app_dir=os.getcwd()

def complete_offline_file_list(parent,total_file_list):

	file_list=glob.glob(parent+'\\*')
	for ea_file in file_list:
		ea_file1={'path':ea_file, 'mtime':os.path.getmtime(ea_file)}
		total_file_list.append(ea_file1)

	for file1 in file_list:
		if os.path.isdir(file1):
			complete_offline_file_list(file1, total_file_list)


def print_list(vlist):
	for ele in vlist:
		for key,val in ele.items():
			print key,val
		print


def sort():

	if os.path.exists(cns.fil_name['T_OFF_OLD']):

		print 'Entered'

		f=open(cns.fil_name['T_OFF_OLD'] ,'r')
		to_old=json.load(f)
		f.close()

		f=open(cns.fil_name['T_OFF_NEW'] ,'r')
		to_new=json.load(f)
		f.close()

		print 'loaded'

		off_del=[]
		for old in to_old:
			if not old in to_new:
				off_del.append(old)

		print 'deleted done'

		off_new=[]
		for new in to_new:
			if not new in to_old:
				off_new.append(new)

		print 'new done'

		off_cf=[]
		for new in off_new:
			for old in off_del:
				if new['path']==old['path']:
					off_new.remove(new)
					off_del.remove(old)
					off_cf.append(new)


		print '\nDELETED\n'
		print_list(off_del)
		print 'NEW\n'
		print_list(off_new)
		print 'CHANGED\n'
		print_list(off_cf)



def main():
	
	total_file_list=[]

	complete_offline_file_list(app_dir+'\\Data',total_file_list)

	print app_dir
	print len(total_file_list)	

	# for file1 in total_file_list:
	# 	print file1, time.ctime(os.path.getmtime(file1)), time.ctime(os.path.getctime(file1))
	
	try:
		os.remove(cns.fil_name['T_OFF_OLD'])
	except:
		pass

	try:
		os.rename(cns.fil_name['T_OFF_NEW'], cns.fil_name['T_OFF_OLD'])
	except:
		pass

	try:
		f=open(cns.fil_name['T_OFF_NEW'] ,'w+')
		json.dump(total_file_list,f)
		f.close()
	except:
		pass

