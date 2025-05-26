def main():
    # list of aws services
    aws_services = ['S3', 'Lambda', 'EC2', 'RDS', 'DynamoDB']

    # use a for loop to iterate thru the list
    # print("\nUsing a for loop to iterate through the list:")
    for service in aws_services:
        print(service)

    # use a while loop to iterate through the list in reverse order
    # print("\nUsing a for loop to iterate through the list in reverse order:")
    index = len(aws_services) -1
    while index >= 0:
        print(aws_services[index])
        index -=1

    # use enumerate() with a for loop to get both the index and value.
    print("\nUsing enumerate with a loop to get both index and value:")
    for index, service in enumerate(aws_services):
        print(f"Service {index +1}: {service}")


if __name__ == '__main__':
    main()