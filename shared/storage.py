import os 
from dotenv import load_dotenv
import boto3 
from botocore.client import Config

load_dotenv()
session = boto3.session.Session()
client = session.client(
    's3',
    region_name=os.getenv('SPACES_REGION_NAME'),
    endpoint_url=f"https://{os.getenv('SPACES_REGION_NAME')}.digitaloceanspaces.com",
    aws_access_key_id=os.getenv("SPACES_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("SPACES_SECRET_KEY"))

def upload_file(file_path, object_name=None):
    try: 
        print(file_path)
        print(object_name)
        client.upload_file(file_path, os.getenv("SPACES_SPACE_NAME"), object_name)
        print(f"Uploaded file: {object_name}")
        return True
    except Exception as e:
        print(f"Error uploading file: {e}")
    