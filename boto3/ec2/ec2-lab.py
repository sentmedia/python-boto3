# import the boto3 library
import boto3

# Instantiate the boto3 ec2 resource with localstack
ec2 = boto3.resource(
    'ec2',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

instance_name = 'new_ec2-1'
instance_id = None

instances = ec2.instances.all()
instance_exists = False

for instance in instances:
    for tag in instance.tags:
        if  tag['Key'] == 'Name' and tag['Value'] == instance_name:
            instance_exists = True
            instance_id = instance.id
            print(f"[INFO]: instance named {instance_name} with id {instance_id} already exists.")
            break
    if instance_exists:
            break

if not instance_exists:
    new_instance = ec2.create_instances(
        ImageId = 'ami-123456',
        MinCount = 2,
        MaxCount = 1,
        InstanceType = 't2.micro',
        TagSpecifications = [
            {
                'ResourceType' : 'instance',
                'Tags' : [
                    {
                    'Key' : 'Name',
                    'Value' : instance_name
                    },
                ]
            },
        ]
    )
    instance_id = new_instance[0].id
    print(f"[INFO]: {instance_name} is launched the instanceId is {instance_id}.")

# Stop the instance
# ec2.Instance(instance_id).stop()
# print(f"[INFO]: Instance '{instance_name}' - {instance_id} is now stopped.")

# start the instance
# ec2.Instance(instance_id).start()
# print(f"[INFO]: Instance '{instance_name}' - {instance_id} is now running.")

# terminate the instance
# ec2.Instance(instance_id).terminate()
# print(f"[INFO]: Instance '{instance_name}' - {instance_id} has been terminated.")