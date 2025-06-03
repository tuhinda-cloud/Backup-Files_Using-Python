
# Backup-files & Automate_Using-Python
● Using this python we can backup our files / folders in our local machine and also upload it in AWS S3 cloud storage using Python.

● Also Automate Terraform Script. And make a EC2 Instance in AWS Cloud.



## Demo

Project OutPut : 
Click > [Video](https://drive.google.com/file/d/1PImnlduhBEpqbwatGQZ6bVjvLBOMjfeJ/view?usp=drive_link)

## Installation 

● shutil --->The `shutil` module in Python is used for high-level file operations, it's especially helpful for creating compressed archives.

● datetime  ---> For show date-times.


● os ---> connection/communication with Operation System

● boto3 ---> used to do AWS tasks using python

● subprocess ---> This imports Python’s built-in module `subprocess`, which is used to run external shell commands (like Terraform CLI commands) from within Python.

```bash
  import shutil
  import datetime
  import os
  import subprocess
```

# Installation dependencies

```bash
# sudo apt update
# sudo apt install python3-pip
# pip3 install boto3
# python3 -m pip show boto3
```
 If ths commands not working do this..!

```bash
# sudo apt install python3-venv python3-pip
# python3 -m venv venv  (This command creating a virtual environment)
# source venv/bin/activate
# pip install boto3
# python -c "import boto3; print(boto3.__version__)"

```

# Connecting with AWS
```bash
# aws configure

After that Give a Access key and Secret access key, Which You can create through IAM.

For Confermation that AWS is connected, Run :

# aws sts get-caller-identity

```
# Terraform Installation

👉 Install Terraform : [Click Here](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)

👉 For More Terraform commands : [Click Here](https://developer.hashicorp.com/terraform/cli/commands)

```bash
● For Creating Infrastructure commands
# terraform Init
# terraform validate
# terraform plan
# terraform apply -auto-approve

● For delete / destroy Infrastructure command 
# terraform destroy -auto-approve
```

