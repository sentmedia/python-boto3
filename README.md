# Python-boto3
Repo for the Udemy course: Python Programming for AWS

I'm using localstack for this course to emulate an AWS environment.
checkout the [boto3/docker-compose.yaml](https://github.com/sentmedia/python-boto3/blob/main/boto3/docker-compose.yml) for details on which services are being emulated.

To create and setup python venv:
 1. `cd boto3`
 2. Run the below command:
   ```
   python -m venv ./env  
   source ./env/bin/activate 
   pip install -r requirements.txt
   ```
   
To start localstack docker container:

1. Start Docker Desktop
2. `cd boto3`
3. Run the following command:

   ```bash
   docker compose up -d
   ```
