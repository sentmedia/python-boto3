# Python-boto3
Repo for the Udemy course: Python Programming for AWS

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