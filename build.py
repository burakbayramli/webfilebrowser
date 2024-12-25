import sys, os

if sys.argv[1] == 'zip':
    os.system("zip /opt/Downloads/dotbkps/webfilebrowser.zip -r /home/burak/Documents/repos/webfilebrowser/.git/")
