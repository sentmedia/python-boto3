def main():
    # Determine the app type based on the services provided
    services_1 = ['S3', 'Lambda', 'DynamoDB', 'ApiGateway']
    services_2 = ['EKS', 'ECR']

    # Use the create_app fuction and check the result
    app_1 = create_app(services_1)
    app_2 = create_app(services_2)
    
    print (f"app_1 type is: {app_1['type']} \ncontaining the following services: {app_1['services']}")
    print (f"app_2 type is: {app_2['type']} \ncontaining the following services: {app_2['services']}")
    

def create_app(services):
    app_type = ''

    if 'Lambda' in services and 'ApiGateway' in services:
        app_type = 'serverless app'
    elif 'EKS' in services and 'ECR' in services:
        app_type = 'container app'
    else:
        app_type = "unknown"

    return {'type' : app_type, 'services' : services}



if __name__ == '__main__':
    main()