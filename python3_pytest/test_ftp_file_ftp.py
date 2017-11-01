import ftplib

connect = ftplib.FTP('192.168.2.170', 'xzrs', 'xzrs')
myfile = open('xzrs', 'rb')
connect.storbinary('STOR xzrs/', myfile)
myfile.close()
connect.quit()