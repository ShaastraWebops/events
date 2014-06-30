from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import constants as cns 
import os
import json



def online_list_files(parent_id, trashed=False):
	
	file_list=drive.ListFile({'q' : "'%s' in parents and trashed=%s"%(parent_id,trashed) }).GetList()
	return file_list


def complete_online_file_list(parent_id, total_file_list):		
	
	file_list=online_list_files(parent_id)

	if len(file_list)>0:				
		total_file_list+=file_list	
		for file1 in file_list:			
			complete_online_file_list(file1['id'],total_file_list)

				

def main():
	
	global drive	

	total_file_list=[]
	total_ob_list=[]

	gauth = GoogleAuth()
	gauth.LocalWebserverAuth()
	drive = GoogleDrive(gauth)

	#complete_online_file_list('root',total_file_list)	
	total_file_list=drive.ListFile({'q':'trashed=False'}).GetList();

	print len(total_file_list)	
	
	# for file1 in total_file_list:
	#  	on_path=[]
	#  	online_path(file1, on_path, total_file_list)
	#  	on_path.reverse()
	#  	total_ob_list.append({'on_path':''.join(on_path), 'file':file1})
	
	try:
		os.remove(cns.fil_name['T_ON_OLD'])
	except:
		pass

	try:
		os.rename(cns.fil_name['T_ON_NEW'], cns.fil_name['T_ON_OLD'])	
	except:
		pass
	f=open(cns.fil_name['T_ON_NEW'] ,'w+')
	json.dump(total_file_list,f)
	f.close()

