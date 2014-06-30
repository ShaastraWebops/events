from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from constants import var_mimetype
import os
import json


gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)


##file1 = drive.CreateFile({'title': 'Hello.xls'})  # Create GoogleDriveFile instance with title 'Hello.txt'
##file1.SetContentString('Hello World!') # Set content of the file from given string
##file1.Upload()


#file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList();
file_list = drive.ListFile({'q':'trashed=False'}).GetList();

# print len(file_list)

#print file_list[0]['title']

# for file1 in file_list:
#   print 'title: %s, id: %s' % (file1['title'], file1['id'])
#   for key,val in file1.iteritems():
#    print 'key: %s, val: %s' %(key,val)

# folder1=drive.CreateFile({'title':'Shaastra_2015','mimetype':'application/vnd.google-apps.folder'})
# folder1=drive.CreateFile({'title':'ShagunRashmi.xls','mimeType': var_mimetype['MIME_TYPE_XLS']})
# folder1.Upload()

# f=open(cns.fil_name['T_ON_NEW'] ,'r')
# total_file_list=json.load(f)
# f.close()

# for file1 in total_file_list:
# 	if 'rr.xlsx' in file1['title']:
# 		break

# for file2 in file_list:
# 	if 'rr.xlsx' in file2['title']:
# 		break

# for key in file1.keys():
# 	print key


# unmatched=file1.items() and file2.items()
# print len(unmatched)
# print len(file1.keys())

# f=open('file1.json','w+')
# for key in file1.keys():
# 	f.write(key)
# 	f.write(str(file1[key]))
# 	f.write("\n")
# f.close()

# f=open('file2.json','w+')
# for key in file2.keys():
# 	f.write(key)
# 	f.write(str(file2[key]))
# 	f.write("\n")
# f.close()

# file2=drive.CreateFile({'title':'rr.xlsx','mimeType':var_mimetype['xlsx']})
# file2.SetContentFile('price.xlsx')
# file2.Upload()
# print file2['mimeType']
# print file2['id']
##file3=drive.CreateFile({'id':'0B0nWZ2E2mBvzN0o1VVdralZvc00'})
##file3.GetContentFile('ee.xlsx')


i='0B0nWZ2E2mBvzVkhTX0xEZWdWVUU'
r='0ACYEVIkyFuxiUk9PVA'
q='0ByYEVIkyFuxiSE1zT1JBRzhicnM'
t='Shagun'
sh_2015='0ByYEVIkyFuxiNjRsbWxxUGViNHc'
for file1 in file_list:
	if i in file1['id']:		
		print file1['title']
		print file1['id']
		break

for key,val in file1.items():
	print key,'\t\t',val



file1['parents']=[{'id':sh_2015}]
file1.Upload()
print 'done'