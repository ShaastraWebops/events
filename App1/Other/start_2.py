from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import urllib2
from httplib2 import socks as pr;


##proxy_support = urllib2.ProxyHandler({"http":"http://10.200.1.3:3128"})
##proxy_support = urllib2.ProxyHandler({"https":"https://10.200.1.3:3128"})
##opener = urllib2.build_opener(proxy_support)
##urllib2.install_opener(opener)
##
###html = urllib2.urlopen("http://www.iitm.ac.in/").read()
##html = urllib2.urlopen("https://mail.google.com").read()
##
##pr.setdefaultproxy(3,'10.200.1.3',3128)
##
##print html

print 0
gauth = GoogleAuth()
print 1
##gauth.http=httplib2.Http(proxy_info= httplib2.ProxyInfo(3,'10.200.1.3',3128))
##gauth.http=httplib2.Http(proxy_info= httplib2.ProxyInfo(3,'10.200.1.3',3128))
##gauth.http=httplib2.Http(proxy_info= httplib2.ProxyInfo(2,'10.200.1.3',3128))
print 2
gauth.LocalWebserverAuth()
print 3

drive = GoogleDrive(gauth)
