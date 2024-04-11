import boto3
from base64 import b64decode
from io import BytesIO

from src.settings import settings
from src.core.exception import FileUploadException

BUCKET_NAME = settings.S3_BUCKET_NAME
SERVICE_NAME = settings.SERVICE_NAME
S3_CLIENT = boto3.client('s3')


class S3BucketUtil:
    @staticmethod
    def upload_to_s3_bucket(file: str, filename: str, path: str = SERVICE_NAME) -> None:
        file_to_upload = BytesIO(b64decode(file)).getvalue()
        try:
            S3_CLIENT.put_object(Bucket=BUCKET_NAME, Key=f'{SERVICE_NAME}/{filename}', Body=file_to_upload)
        except Exception:
            raise FileUploadException()

    @staticmethod
    def delete_from_s3_bucket(filename: str, path: str = SERVICE_NAME) -> None:
        S3_CLIENT.delete_object(Bucket=BUCKET_NAME, key = f'{path}/{filename}')

    @staticmethod
    def download_from_s3_bucket(filename: str, path: str = SERVICE_NAME) -> bytes:
        response = S3_CLIENT.get_object(Bucket=BUCKET_NAME, key = f'{path}/{filename}')
        return response['Body'].read()
