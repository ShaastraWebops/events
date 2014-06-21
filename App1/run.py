import os
import time
import gui_p1
import gui_p2
# import requests

os.putenv('http_proxy','http://na12b028:-tx5Y$4P@hproxy.iitm.ac.in:3128/')
os.putenv('https_proxy','https://na12b028:-tx5Y$4P@hproxy.iitm.ac.in:3128/')

# os.putenv('http_proxy','http://10.200.1.3:3128/')
# os.putenv('https_proxy','https://10.200.1.3:3128/')

# requests.get('https://github.com',verify=True)

# os.system('python login_1.py')

gui_p1.main()
gui_p2.main()

# os.system('python login.py')



##st='''
##D:
##cd Documents\GitHub\events\App1
##set http_proxy=http://na12b028:-tx5Y$4P@hproxy.iitm.ac.in:3128/
##set https_proxy=https://na12b028:-tx5Y$4P@hproxy.iitm.ac.in:3128/
##python start.py
##'''
##
##os.system(st)
