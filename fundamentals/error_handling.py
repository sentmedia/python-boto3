def main():
    service = 'EKS'

    service_status = get_service_status(service)

    if service_status:
        print(f"\n{service} service status: '{service_status}'")
    
        if service_status == 'Operational':
            print(f"Running operation on '{service}'")
        else:
            print(f"'{service}' is not operational")
    else: 
        print(f"\nService status for {service} could not be retrieved.")

def get_service_status(service_name):
    aws_services_status = {
        "EC2" : "Maintenance",
        "S3" : "Operational",
        "Lambda" : "Issues Detected",
        "DynamoDB" : "Operational",
        "RDS" : "Operational"
    }
    try:
        return aws_services_status[service_name]
    except KeyError as ke:
        print(f"ERROR: {ke}. Status for service {service_name} is not in our records.")
        return None

if __name__ == '__main__':
    main()
    