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

