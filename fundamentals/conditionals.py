def main():
    user_requirement = 'compute'  # This can be changed to 'serverless', 'storage', or 'compute'

    if user_requirement == 'serverless':
        aws_service = 'Lambda'
    elif user_requirement == 'storage':
        aws_service = 'S3'
    elif user_requirement == 'compute':
        aws_service = 'EC2'
    else:
        aws_service = 'Unknown'

    # check if the aws_service is not 'Unknown'
    # print the aws_service based on user_requirement
    if aws_service != 'Unknown':
        print(f'The AWS service required is {aws_service}.')
    else:
        print(f'ERROR: The required AWS service is {aws_service}.')

main()