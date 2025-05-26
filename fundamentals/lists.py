def main():
    # list of aws services
    aws_services = [
        "Amazon EC2",
        "Amazon S3",
        "Amazon RDS",
        "Amazon DynamoDB",
        "Amazon Lambda"]
    
    #Print the list of aws services
    print(f"List of AWS Services: {aws_services}")

    # print the first service in the list
    print(f'First AWS Service: {aws_services[0]}')
   
    # print the last service in the list
    print(f'Last AWS Service: {aws_services[-1]}')
   
    # print the number of services in the list
    print(f'Number of AWS Services: {len(aws_services)}')

    # modify the last service in the list
    aws_services[-1] = "Amazon SNS"

    # print the modified list

    print(f"Modified List of AWS Services: {aws_services}")

    # append a new service to the list
    aws_services.append("Amazon SQS")

    # print the list after appending
    print(f'AWS Service list after appending: {aws_services}')

    # remove a service from the list
    aws_services.pop(3)
    # print the list after removing
    print(f'AWS Service list after removing: {aws_services}')

    # slice the list elements
    sliced_services = aws_services[1:5]
    # print the sliced list
    print(f"Sliced list of AWS Services: {sliced_services}")


if __name__ == "__main__":
    main()