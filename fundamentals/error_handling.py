def main():
    service = 'Lambda'

    service_status = get_service_status(service)

    print(f"\n{service} service status: '{service_status}'")

    if service_status == 'Operational':
        print(f"Running operation on '{service}'")
    else:
        print(f"'{service}' is not operational")

def get_service_status(service_name):
    aws_services_status = {
        "EC2" : "Maintenance",
        "S3" : "Operational",
        "Lambda" : "Issues Detected",
        "DynamoDB" : "Operational",
        "RDS" : "Operational"
    }
    return aws_services_status[service_name]

if __name__ == '__main__':
    main()
    