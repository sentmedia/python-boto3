def main():

    # Dictionary of AWS services
    aws_services = {
        "S3" : "Simple Storage Service",
        "Lambda" : "Serverless Compute Service",
        "EC2" : "Elastic Compute Cloud"
    }
    # Print the dictionary of AWS services
    print(f'Dictionary of AWS Services: {aws_services}')

    # Create a var for the lambda desc and print
    lambda_desc = aws_services["Lambda"]
    print(f'Description of Lambda: {lambda_desc}')

    # update the desc of the S3 service and print the new S3 desc.
    aws_services["S3"] = "AWS Object Storage Service"
    print(f'Updated desc of S3: {aws_services["S3"]}')

    # Add a new service to the dictionary and print it out.
    aws_services['SQS'] = "Simple Queue Service"
    print(f'Added SQS: {aws_services['SQS']}')

    # Remove a service from the dictionary and print out the revised dictionary
    del aws_services["Lambda"]
    print(f'Revised AWS Service Dictionary: {aws_services}')

    # Display diff attributes of the dict using keys(), values() and items()
    print(aws_services.keys())
    print(aws_services.values())
    print(aws_services.items())

    # Modify the aws_services dict to include a nested dict for EC2
    aws_services["EC2"] = {
        'description' : 'Elastic Compute Cloud',
        'Launch year' : 2006
    }
    print(aws_services)




if __name__ == "__main__":
    main()