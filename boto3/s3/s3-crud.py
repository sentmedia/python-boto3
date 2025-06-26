# import the boto3 library
import boto3

# Instantiate the boto3 s3 resource with localstack
s3 = boto3.resource(
    's3',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

# Set bucket name
bucket_name = 'dct-crud-1'

# Check if the bucket exists and create if does NOT exist.
all_my_buckets = [bucket.name for bucket in s3.buckets.all()]

if bucket_name not in all_my_buckets:
    print(f"'{bucket_name}' does not exist. Creating now...")
    s3.create_bucket(Bucket=bucket_name)
    print(f"'{bucket_name}' has been created.")
else:
    print(f"'{bucket_name}' already exists.")

# Create 'file_1' and 'file_2'
file_1 = 'file_1.txt'
file_2 = 'file_2.txt'

# Upload 'file_1' and 'file_2' to the new bucket
s3.Bucket(bucket_name).upload_file(Filename=file_1,Key=file_1)

# Get bucket objects
for obj in s3.Bucket(bucket_name).objects.all():
    print(obj.key)

# Read and print the file from the bucket
obj = s3.Object(bucket_name, file_1)
body = obj.get()['Body'].read()
print(body)

# Update file_1 contents with file_contents and print the body
s3.Object(bucket_name, file_1).put(Body=open(file_2, 'rb'))
obj = s3.Object(bucket_name, file_1)
body = obj.get()['Body'].read()
print(body)

#Delete the file from the bucket
s3.Object(bucket_name, file_1).delete()

# Delete the bucket
bucket = s3.Bucket(bucket_name)
bucket.delete()