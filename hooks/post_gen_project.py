import os
import json
import shutil
import logging
import boto3
from botocore.exceptions import ClientError

engine = "{{ cookiecutter.engine }}"
project = "{{ cookiecutter.project_slug }}".replace("_", "-")


def create_bucket(bucket_name, region=None):

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client("s3")
            region = s3_client.meta.region_name
        else:
            s3_client = boto3.client("s3", region_name=region)

        location = {"LocationConstraint": region}
        s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
        bucket_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "DjangoBucketPolicy",
                    "Effect": "Allow",
                    "Principal": "*",
                    "Action": ["s3:GetObject", "s3:PutObject"],
                    "Resource": f"arn:aws:s3:::{bucket_name}/*",
                }
            ],
        }

        # Convert the policy from JSON dict to string
        bucket_policy = json.dumps(bucket_policy)

        # Set the new policy
        s3 = boto3.client("s3")
        s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)

        # Define the configuration rules
        cors_configuration = {
            "CORSRules": [
                {
                    "AllowedHeaders": ["Authorization"],
                    "AllowedMethods": ["GET", "PUT"],
                    "ExposeHeaders": ["GET", "PUT"],
                    "AllowedOrigins": ["*"],
                    "MaxAgeSeconds": 3000,
                }
            ]
        }

        # Set the CORS configuration
        s3 = boto3.client("s3")
        s3.put_bucket_cors(Bucket=bucket_name, CORSConfiguration=cors_configuration)
    except ClientError as e:
        logging.error(e)
        return False
    return True


if engine == "Flask":
    os.remove("manage.py")
    os.remove("db.sqlite3")
    shutil.rmtree(project, ignore_errors=True)

elif engine == "Django":
    os.remove("app.py")
    static_bucket = project.replace("_", "-") + "-" + engine.lower()
    create_bucket(static_bucket)
    print("A bucket for your Static files has been created: " + static_bucket)
