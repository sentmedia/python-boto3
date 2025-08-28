# import the boto3 library
import boto3

# Instantiate the boto3 ec2 client with localstack

ec2 = boto3.client(
    'ec2',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)


# Create new VPC

vpc_name = 'vpc-hol'

response = ec2.describe_vpcs(
    Filters=[{'Name': 'tag:Name', 'Values': [vpc_name]}]
)
vpcs = response.get('Vpcs', [])

if vpcs:
    vpc_id = vpcs[0]['VpcId']
    print(f"VPC '{vpc_name}' with ID '{vpc_id}' already exists.")
else:
    vpc_response = ec2.create_vpc(CidrBlock='10.0.0.0/16')
    vpc_id = vpc_response.id
    ec2.create_tags(Resources=[vpc_id], Tags=[{'Key': 'Name', 'Value': vpc_name}])
    print(f"VPC '{vpc_name}' with ID '{vpc_id}' has been created." )


# Create internet gateway

igw_name = 'igw-hol'
response = ec2.describe_internet_gateways(
    Filters = [{'Name': 'tag:Name', 'Values': [igw_name]}]
)

internet_gateways = response.get('InternetGateways', [])

if internet_gateways:
    igw_id = internet_gateways[0]['InternetGatewayId']
    print(f"InternetGateway '{igw_name}' with ID '{igw_id}' already exists.")
else:
    igw_response = ec2.create_internet_gateway()
    igw_id = igw_response.id
    ec2.create_tags(Resources=[igw_id], Tags=[{'Key': 'Name', 'Value': igw_name}])
    ec2.attach_internet_gateway(VpcID=vpc_id, InternetGatewayId=igw_id)
    print(f"Internet Gateway '{igw_name}' with ID '{igw_id}' has been created.")


# Create Route Table and Public Route
rt_name = 'rt-hol'
response = ec2.describe_route_tables(
    Filters = [{'Name': 'tag:Name', 'Values': [rt_name]}]
)

route_tables = response.get('RouteTables', [])

if route_tables:
    rt_id = route_tables[0]['RouteTableId']
    print(f"Route Table '{rt_name}' with ID '{rt_id} already exists.")
else:
    rt_response = ec2.create_route_table(VpcId = vpc_id)
    rt_id = rt_response['RouteTable']['RouteTableId']
    route = ec2.create_route(
        RouteTableId = rt_id,
        DestinationCidrBlock = '0.0.0.0/0',
        GatewayId = igw_id
    )
    ec2.create_tags(Resources=[rt_id], Tags=[{'Key': 'Name', 'Value': rt_name}])
print(f"Route Table '{rt_name}' with ID '{rt_id}' has been created.")


# Create subnets in us-east-1 AZs

subnet_count = 3
cidr_base = "10.0.{0}.0/24"

# Get available AZs
azs = ec2.describe_availability_zones(
    Filters = [{'Name': 'region-name', 'Values': ['us-east-1']}]
)['AvailabilityZones']

# Get existing subnets in the VPC
existing_subnets = ec2.describe_subnets(
    Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}]
)['Subnets']
occupied_azs = {subnet['AvailabilityZone'] for subnet in existing_subnets}

created = 0
for i, az in enumerate(azs):
    az_name = az['ZoneName']
    if az_name in occupied_azs:
        print(f"Skipping {az_name}: subnet already exists.")
        continue
    if created >= subnet_count:
        break
    subnet_cidr = cidr_base.format(i)
    subnet_response = ec2.create_subnet(
        VpcId = vpc_id,
        CidrBlock = subnet_cidr,
        AvailabilityZone = az_name
    )
subnet_id = subnet_response['Subnet']['SubnetId']
ec2.create_tags(Resources=[subnet_id], Tags=[{'Key':'Name', 'Value': f'subnet-hol-{i}'}])
print(f"Subnet 'subnet-hol-{i}' created in '{az_name}' with CIDR: {subnet_cidr}")