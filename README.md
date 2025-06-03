
# backup-files_Using-Python
using this python we can backup our files / folders in our local machine and also upload it in AWS S3 cloud storage using Python.




## Installation 

shutil --->The shutil module in Python is used for high-level file operations, it's especially helpful for creating compressed archives.

datetime  ---> For show date-times.

os ---> connection/communication with Operation System

boto3 ---> used to do AWS tasks using python

```bash
  import shutil
  import datetime
  import os

```

# Installation dependencies

```bash
# sudo apt update
# sudo apt install python3-pip
# pip3 install boto3
# python3 -m pip show boto3
```
 If this commands not working do this..!

```bash
# sudo apt install python3-venv python3-pip
python3 -m venv venv  (This command creating a virtual environment for running this commands.)
# source venv/bin/activate
# pip install boto3
# python -c "import boto3; print(boto3.__version__)"

```

# Connecting with AWS
```bash
# aws configure

After that Give a Access key and Secrate key, Which You can create throung IAM.
```

