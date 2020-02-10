import pandas as pd

def initial():
	#Database Login
	server = 'server'
	database = 'database'
	username = 'username'
	password = 'password'

	#FTP Login
	ftpserver = 'ftpserver'
	ftpusername = 'ftpusername'
	ftppassword = 'ftppassword'

	#FTP Directory
	ftpDirectory = 'ftp directory'

	#Query
	query = '''select * from yourtable'''

	#Local Directory
	localDirectory = 'localdirectory'

	#filename
	filename = 'filename'

	#file format ('excel'/'csv')
	format = 'excel'
	
	return server,database,username,password,ftpserver,ftpusername,ftppassword,tempDirectory,query,localDirectory,filename,format