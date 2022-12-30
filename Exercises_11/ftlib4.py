""""
Example of ftp https://www.askpython.com/python-modules/file-transfer-protocol-in-python
Getting the size of a file

"""

#import module
import ftplib
 
#define server ftp address
site_addr= "ftp.ubuntu.com"
 
#make a connection to server
ftp_obj = ftplib.FTP(site_addr)
 
#login to the server
ftp_obj.login()
ftp_obj.cwd("ubuntu")
 
print("Present Working Directory is:")
 
#get the name of present working directory
present=ftp_obj.pwd()
print(present)
print("Content of the directory "+ " is:")
ftp_obj.dir()
 
#print size of "ls-lR.gz"
fsize= ftp_obj.size("ls-lR.gz")
print("Size of file ls-lR.gz is:"+ str(fsize))
 
#close the connection
ftp_obj.close()