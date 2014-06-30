import os
import time
import browse
import offline

t = time.time()

if 'HTTP_PROXY' in locals() and HTTP_PROXY:
	os.putenv('http_proxy', HTTP_PROXY)
if 'HTTPS_PROXY' in locals() and HTTPS_PROXY:
	os.putenv('https_proxy', HTTPS_PROXY)


os.system('python gui_p1.py')

import process
browse.main()
offline.main()	
offline.sort()
print time.time() - t



