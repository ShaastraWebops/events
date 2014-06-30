import json
import constants as cns
import time
import os

def online_path(file1, on_path, total_file_list):
	on_path = os.path.join(on_path, file1['title'])
	print on_path
	if not file1['parents'][0]['isRoot']:
		parent_id=file1['parents'][0]['id']
		for parent in total_file_list:			
			if parent_id==parent['id']:
				break
		online_path(parent, on_path, total_file_list)


f = open(cns.fil_name['T_ON_NEW'] ,'r')
total_file_list=json.load(f)
f.close()

t=time.time()

r='0ACYEVIkyFuxiUk9PVA'
n='Learning Module'
n1='Shaastra 2017'
i='0B0nWZ2E2mBvzVkhTX0xEZWdWVUU'
q='0ByYEVIkyFuxiSE1zT1JBRzhicnM'

print len(total_file_list)

# file1=total_file_list[100]
# for key in file1.keys():
# 	print key,'\t\t\t',file1[key]

# for file1 in total_file_list:
# 	for iter1 in file1['parents']:
# 		if r in iter1['id']:
# 			print file1['title']		

# for file1 in total_file_list:
# 	if n1 in file1['id']:		
# 		print file1['title']
# 		break

for file1 in total_file_list:
	if n1 in file1['title']:		
		print file1['title'], file1['id']
		break

# print "\nStarting\n"
# on_path=[]
# online_path(file1, on_path, total_file_list)
# on_path.reverse()
# print on_path
# print ''.join(on_path)
# print "\nEnding\n"

# for key in file1.keys():
# 	print key,'\t\t\t',file1[key]

print time.time() - t		