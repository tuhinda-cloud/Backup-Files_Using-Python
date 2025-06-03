#This is a script to take a backup files / folder from local to AWS-S3

import boto3     # used to do AWS tasks using python
import datetime  # For Datetime function..

s3 = boto3.resource("s3" , region_name = "us-east-1")  #Region name mentioned 

#For Print my AWS S3 Bucket names....

def show_buckets(s3):
    for bucket in s3.buckets.all():   #This is called Interpollation system
        print(bucket.name)



#Bucket createing script...

def create_bucket(s3, bucket_name):
    s3.create_bucket(Bucket=bucket_name)  #Bucket name write here, must have it exception  
    print("Bucket Created Successfully")


#Backup files in local to AWS-S3 script...

def upload_backup(s3,file_name,bucket_name,key_name):
    data = open(file_name, 'rb')   #Read this file in binary format
    s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
print("Backup Uploded Successfully...")



bucket_name= "tuhins-backup-folder2"         # Give a S3 Bucket name, It must be have unique 
file_name = "/home/tuhin/Documents/VS Code_Code/TWS_Python/Python/backups/backup_2025-06-03.tar.gz"    # Give you local Mahine path of the folder

create_bucket(s3, bucket_name) #call function
show_buckets(s3)  #call fucntion
upload_backup(s3,file_name,bucket_name,"mybackup.tar.gz") #call fucntion




"""
This is extra part....
"""

#Backup files in local to AWS-S3 with date-time stamp script...

from datetime import datetime

bucket_name1 = "tuhins-backup-folder1"   # Give a S3 Bucket name, It must be have unique 
file_name = "/home/tuhin/Documents/VS Code_Code/TWS_Python/Python/backups/backup_2025-06-03.tar.gz"   # Give you local Mahine path of the folder

create_bucket(s3, bucket_name1)
show_buckets(s3)

# Generate timestamped key
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  #strftime means ---> String Format Time (Now/Current Date-time)
key_name = f"backup_{timestamp}.tar.gz"    # 'f' means 'Formated String' 

upload_backup(s3, file_name, bucket_name1, key_name)  #call function

