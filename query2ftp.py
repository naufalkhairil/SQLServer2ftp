import ftplib
from ftplib import FTP
import pandas as pd
import io, os, time, pyodbc, sys
from datetime import datetime  
from datetime import timedelta 

from init import initial
start_time = time.time()

server,database,username,password,ftpserver,ftpusername,ftppassword,ftpDirectory,query,localDirectory,filename,format = initial()

print('\nStarting connection to database %s'%database)
			
#Connection String

conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()
print('\nSuccess connected to database')

print ('Starting connection to FTP %s' %ftpserver)
# Try connecting to the server
try:
    ftp = ftplib.FTP(ftpserver) 
    ftp.login(user=ftpusername, passwd = ftppassword)
    print ('Success connected to FTP %s'%ftpserver)
except ftplib.all_errors as e:
    errorcode_string = str(e).split(None, 1)[0]

print ('Changing directory to' + ' ' + ftpDirectory)
ftp.cwd(ftpDirectory)
print ('Current working directory is %s' % ftp.pwd())

df = pd.read_sql(query,conn)

print(df.head())

if format == 'excel':
	df.to_excel(localDirectory + filename + '_' + week + '.xlsx', index=False)

	file_dir = localDirectory + filename + '_' + week + '.xlsx'

	with open(file_dir, "rb") as f:
		ftp.storbinary('STOR ' + os.path.basename(file_dir), f)
		
	print('Success write %s to FTP %s' %(filename + '_' + week + '.excel', ftpserver))
	
elif format == 'csv':
	df.to_csv(localDirectory + filename + '_' + week + '.csv', index=False)

	file_dir = localDirectory + filename + '_' + week + '.csv'

	with open(file_dir, "rb") as f:
		ftp.storbinary('STOR ' + os.path.basename(file_dir), f)
		
	print('Success write %s to FTP %s' %(filename + '_' + week + '.csv', ftpserver))
else:
	print('wrong format')