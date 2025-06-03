#This is for Windows!

import shutil  # The shutil module in Python is used for high-level file operations, it's especially helpful for creating compressed archives.
import datetime # for show date-times. 
import os # connection /communication with Operation System

def backup_files(source, destination):
    # Ensure the destination directory exists
    os.makedirs(destination, exist_ok=True)

    # Get today's date
    today = datetime.date.today()

    # Define base name (without extension) for archive
    backup_file_name = os.path.join(destination, f"backup_{today}")

    # Create a .zip archive (For Windows)
    shutil.make_archive(backup_file_name, 'zip', source)

    print(f"Backup created at: {backup_file_name}.zip")

# Use raw strings (r"") or double backslashes to handle Windows paths properly
source = r"F:\VS CODESSSSS\My_Python"   # Write here your own Source path
destination = r"F:\VS CODESSSSS\My_Python\backups" # Write here your own Destination path

backup_files(source, destination)  #Call Function

