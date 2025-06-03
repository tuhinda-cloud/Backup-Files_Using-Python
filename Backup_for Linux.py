#This is for Linux!

import shutil  # The shutil module in Python is used for high-level file operations, it's especially helpful for creating compressed archives.
import datetime # for show date-times. 
import os # connection /communication with Operation System

def backup_files(source, destination):
    today = datetime.date.today() # Get today's date
    backup_file_name = os.path.join(destination, f"backup_{today}.tar.gz") # Define base name for archive and join it OS sysetm files.
    shutil.make_archive(backup_file_name.replace('.tar.gz' , ''), 'gztar' ,source)

    print(backup_file_name)

source = # write source path
destination = # write destination path
backup_files(source, destination)  #Call Function

