from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import constants as cns 
import json



def list_all_files(parent_id, trashed=False):
	
	file_list=drive.ListFile({'q' : "'%s' in parents and trashed=%s"%(parent_id,trashed) }).GetList()
	return file_list


def complete_file_list(parent_id):		

	global total_file_list
	file_list=list_all_files(parent_id)

	if len(file_list)>0:				
		total_file_list+=file_list	
		for file1 in file_list:			
			complete_online_file_list(file1['id'])
			

def main():
	
	global drive, total_file_list	

	total_file_list=[]

	gauth = GoogleAuth()
	gauth.LocalWebserverAuth()
	drive = GoogleDrive(gauth)

	#complete_file_list('root')	
	total_file_list=drive.ListFile().GetList();

	#print len(total_file_list)	

	# for file1 in total_file_list:
	#   print 'title: ', (file1['title'])	
	
	# f=open('total_file_list.json','w+')
	# json.dump(total_file_list,f)
	# f.close()

