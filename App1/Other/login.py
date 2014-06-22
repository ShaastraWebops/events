from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# from google API console - convert private key to base64 or load from file
uid = 'shagun.exp@gmail.com'
key = '1qW@1qW@'

credentials = SignedJwtAssertionCredentials(uid, key, scope='https://www.googleapis.com/auth/drive')
credentials.authorize(httplib2.Http())

gauth = GoogleAuth()
gauth.credentials = credentials

drive = GoogleDrive(gauth)