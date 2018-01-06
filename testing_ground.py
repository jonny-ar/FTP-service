from ftplib import FTP  # import class FTP from ftplib

# connects directly to the host ip address
# namespace -> ip address
# default ftp port = 21

ftp = FTP('speedtest.tele2.net')  # test server

"""
unclear if FTP class initialization calls .connect
if so, no need for ftp.connect(host,port)
"""

ftp.login()  # defaults to 'anonymous' for user,pw

ftp.retrlines('LIST')  # list directory content

# we could also list the files/directories to a file by calling
files = ftp.dir()
print("Directory Contents: {}".format(files))

# ftp.storlines() or ftp.storbinary() to upload to ftp server

ftp.cwd('upload')  # arg is path/directory to change into
ftp.retrlines('LIST') #what is in upload dir?

ftp.quit()  # finished

# FTP HOST SERVER
"""
Listening to port for incoming connects
Have welcome msg ready
"""
