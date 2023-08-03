

#####for updating the configuration file 
import boto3
S3API = boto3.client("s3", region_name="us-east-1") 
bucket_name = "your bucket name"####bucket hosting static file

filename = "/home/ec2-user/environment/resources/website/config.js"
S3API.upload_file(filename, bucket_name, "config.js", ExtraArgs={'ContentType': "application/js", "CacheControl": "max-age=0"})


print ("DONE")