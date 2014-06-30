import os

def id_to_path(drive,fid,fpath):
	file1=drive.CreateFile({'id':fid})
	file1.GetContentFile(fpath)