"""
Example of using FTP from https://www.askpython.com/python-modules/file-transfer-protocol-in-python
"""


#import module
import ftplib
#define server ftp address
site_addr= "ftp.ubuntu.com"
#make a connection to server
ftp_obj = ftplib.FTP(site_addr)
#login to the server
ftp_obj.login()
print("Content of the directory "+ " is:")
#print the content of present working directory
ftp_obj.dir()
 
#close the connection
ftp_obj.close()