"""
Digital Ocean Spaces Storage Module

Provides unified storage operations for uploading, checking, and listing files.
"""

import os 
from typing import Optional, Set
from dotenv import load_dotenv
import boto3 
from botocore.client import Config
from botocore.exceptions import ClientError

load_dotenv()

BUCKET_NAME = os.getenv("SPACES_SPACE_NAME")

session = boto3.session.Session()
client = session.client(
    's3',
    region_name=os.getenv('SPACES_REGION_NAME'),
    endpoint_url=f"https://{os.getenv('SPACES_REGION_NAME')}.digitaloceanspaces.com",
    aws_access_key_id=os.getenv("SPACES_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("SPACES_SECRET_KEY"))


def upload_file(file_path: str, object_name: str, skip_existing: bool = False) -> bool:
    """
    Upload a file to Digital Ocean Spaces.
    
    Args:
        file_path: Local path to the file to upload
        object_name: Destination key/path in the bucket
        skip_existing: If True, skip upload if file already exists (saves time).
                       If False, always upload (replaces existing file).
    
    Returns:
        True if uploaded successfully, False if skipped or error
    """
    try:
        # Check if file exists (only if skip_existing is True)
        if skip_existing and file_exists(object_name):
            print(f"Skipped (exists): {object_name}")
            return False
        
        client.upload_file(file_path, BUCKET_NAME, object_name)
        print(f"Uploaded: {object_name}")
        return True
    except Exception as e:
        print(f"Error uploading file: {e}")
        return False


def file_exists(object_name: str) -> bool:
    """
    Check if a file exists in Digital Ocean Spaces.
    
    Args:
        object_name: The key/path in the bucket to check
    
    Returns:
        True if file exists, False otherwise
    """
    try:
        client.head_object(Bucket=BUCKET_NAME, Key=object_name)
        return True
    except ClientError:
        return False


def list_files(prefix: str) -> Set[str]:
    """
    List all files under a given prefix in Digital Ocean Spaces.
    
    Args:
        prefix: The prefix/folder path to list (e.g., "tiktok_video_metadata/nike/")
    
    Returns:
        Set of object keys matching the prefix
    """
    keys = set()
    try:
        paginator = client.get_paginator('list_objects_v2')
        for page in paginator.paginate(Bucket=BUCKET_NAME, Prefix=prefix):
            for obj in page.get('Contents', []):
                keys.add(obj['Key'])
    except Exception as e:
        print(f"Error listing files: {e}")
    return keys


def list_file_ids(prefix: str, extension: str = ".json") -> Set[str]:
    """
    List all file IDs (filenames without extension) under a given prefix.
    
    Useful for getting video IDs from paths like:
    tiktok_video_metadata/username/video_id.json
    
    Args:
        prefix: The prefix/folder path to list (e.g., "tiktok_video_metadata/nike/")
        extension: File extension to strip (default: ".json")
    
    Returns:
        Set of file IDs (filenames without extension)
    """
    file_ids = set()
    try:
        paginator = client.get_paginator('list_objects_v2')
        for page in paginator.paginate(Bucket=BUCKET_NAME, Prefix=prefix):
            for obj in page.get('Contents', []):
                key = obj['Key']
                filename = key.split('/')[-1]
                if filename.endswith(extension):
                    file_ids.add(filename[:-len(extension)])
    except Exception as e:
        print(f"Error listing file IDs: {e}")
    return file_ids


def delete_file(object_name: str) -> bool:
    """
    Delete a file from Digital Ocean Spaces.
    
    Args:
        object_name: The key/path in the bucket to delete
    
    Returns:
        True if deleted successfully, False otherwise
    """
    try:
        client.delete_object(Bucket=BUCKET_NAME, Key=object_name)
        print(f"Deleted: {object_name}")
        return True
    except Exception as e:
        print(f"Error deleting file: {e}")
        return False
