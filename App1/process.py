import json
import constants as cns
import time

f=open('total_file_list.json','r')
total_file_list=json.load(f)
f.close()

t=time.time()

r='0ACYEVIkyFuxiUk9PVA'

for file1 in total_file_list:
	if r in file1['parents'][0]['id']:
		print file1['title']		

print time.time() - t		