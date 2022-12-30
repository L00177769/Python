ftp=FTP(“domain name”)
ftp.login()
print(ftp.getWelcome())
ftp.retrlines('LIST')