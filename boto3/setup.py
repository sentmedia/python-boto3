import boto3

# Instantiate the boto3 s3 resource with localstack
s3 = boto3.resource(
    's3',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

# List all buckets
for bucket in s3.buckets.all():
    print(bucket.name)