# Python-boto3
Repo for the Udemy course: Python Programming for AWS

I'm using localstack for this course to emulate an AWS environment.
checkout the boto3/docker-compose.yaml(https://github.com/sentmedia/python-boto3/boto3/docker-compose.yml) for details on how I'm bringing up localstack.

To create and setup python venv:
 `cd python-boto3/boto3`
   ```
   python -m venv ./env  
   source ./env/bin/activate 
   pip install -r requirements.txt
   ```
   
To start localstack docker container:

1. Start Docker Desktop
2. Change directory to `python-boto3/boto3`
3. Run the following command:

   ```bash
   docker compose up -d
   ```
