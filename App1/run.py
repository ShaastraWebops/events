import os
import time
#import gui_p1
#import gui_p2
import browse
import offline
# import requests

t=time.time()

# os.putenv('http_proxy','http://na12b028:-tx5Y$4P@hproxy.iitm.ac.in:3128/')
# os.putenv('https_proxy','https://na12b028:-tx5Y$4P@hproxy.iitm.ac.in:3128/')

# os.putenv('http_proxy','http://10.200.1.3:3128/')
# os.putenv('https_proxy','https://10.200.1.3:3128/')

# requests.get('https://github.com',verify=True)

# os.system('python start.py')
#os.system('start.exe')

os.system('python gui_p1.py')
# import gui_p1
import process
browse.main()
offline.main()	
offline.sort()
print time.time()-t



