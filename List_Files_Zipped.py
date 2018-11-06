from zipfile import ZipFile

file_name = 'random files.zip'

def get_file_name(file_path):
	z = ZipFile(file_path)
	return z.namelist()

def get_file_name_detailed(file_path):
	z = ZipFile(file_path)
	return list(z.infolist())
