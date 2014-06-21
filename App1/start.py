from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from constants import var_mimetype
import os


gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)


##file1 = drive.CreateFile({'title': 'Hello.xls'})  # Create GoogleDriveFile instance with title 'Hello.txt'
##file1.SetContentString('Hello World!') # Set content of the file from given string
##file1.Upload()


file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList();


print len(file_list)

print file_list[0]['title']

# for file1 in file_list:
#   print 'title: %s, id: %s , mimeType: %s' % (file1['title'], file1['id'], file1['parents'])
#   for key,val in file1.iteritems():
#    print 'key: %s, val: %s' %(key,val)

# folder1=drive.CreateFile({'title':'Shaastra_2015','mimetype':'application/vnd.google-apps.folder'})
folder1=drive.CreateFile({'title':'Shaastra_2015','mimeType': var_mimetype['MIME_TYPE_FOLDER']})
folder1.Upload()

##file2=drive.CreateFile({'title':'rr.xls','mimeType':'application/x-msexcel','parent':'0B0nWZ2E2mBvzdnJ0Z3Q2Z0k3Q0E'})
##file2.SetContentFile('Mass Balance.xlsx')
##file2.Upload()

##file3=drive.CreateFile({'id':'0B0nWZ2E2mBvzN0o1VVdralZvc00'})
##file3.GetContentFile('ee.xlsx')


