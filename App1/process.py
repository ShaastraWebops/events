import json
import constants as cns
import time

f=open('total_file_list.json','r')
total_file_list=json.load(f)
f.close()

t=time.time()

r='0ACYEVIkyFuxiUk9PVA'
n='Shaastra'

print len(total_file_list)

for file1 in total_file_list:
	for iter1 in file1['parents']:
		if r in iter1['id']:
			print file1['title']		

for file1 in total_file_list:
	if n in file1['title']:		
		print file1['title']					

print time.time() - t		