import os
import boto3

def upload_folder_to_s3(folder_path, bucket_name, access_key_id, secret_access_key,path):
    s3 = boto3.client(
        's3',
        aws_access_key_id=access_key_id,
        aws_secret_access_key=secret_access_key
    )

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            local_file_path = os.path.join(root, file)
            object_name = os.path.join(path, os.path.relpath(local_file_path, folder_path))
            try:
                s3.upload_file(local_file_path, bucket_name, object_name)
                print(f"Uploaded {local_file_path} to S3 as {object_name}")
            except Exception as e:
                print(f"Error uploading {local_file_path} to S3: {e}")

# Specify the path of the local folder containing the files
local_folder_path = (r'C:\Users\sureshswathi\Downloads\datamigrationaws')

# Specify the name of the bucket in AWS S3
bucket_name = 'datamigrationaws'

path = 'data/'

# Specify your AWS Access Key ID and Secret Access Key
access_key_id = 'AKIA4MTWLZQBMV4UCEUF'
secret_access_key = 'NPXsG/1px+eNcb6kpKQM+dw6c9b8572JHRPrwelD'

# Call the function to upload the files in the folder
upload_folder_to_s3(local_folder_path, bucket_name, access_key_id, secret_access_key,path)
