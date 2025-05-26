import boto3

s3 = boto3.resource(
    's3',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

for bucket in s3.buckets.all():
    print(bucket.name)