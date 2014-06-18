from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)


##file1 = drive.CreateFile({'title': 'Hello.xls'})  # Create GoogleDriveFile instance with title 'Hello.txt'
##file1.SetContentString('Hello World!') # Set content of the file from given string
##file1.Upload()



file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:
  print 'title: %s, id: %s' % (file1['title'], file1['id'])

##file2=drive.CreateFile({'title':'rr.xls','mimetype':'application/x-msexcel','parent':'0B0nWZ2E2mBvzdnJ0Z3Q2Z0k3Q0E'})
##file2.SetContentFile('Mass Balance.xlsx')
##file2.Upload()

##file3=drive.CreateFile({'id':'0B0nWZ2E2mBvzN0o1VVdralZvc00'})
##file3.GetContentFile('ee.xlsx')


