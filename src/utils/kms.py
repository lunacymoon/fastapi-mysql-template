from base64 import b64decode, b64encode

import boto3
KMS_CLIENT = boto3.client('kms')

class KMSUtil:
    @staticmethod
    def encrypt(key_arn: str, text: str) -> str:
        plaintext = text.encode('utf-8')
        response = KMS_CLIENT.encrypt(KeyId=key_arn, Plaintext=plaintext)
        return b64encode(response['CiphertextBlob']).decode('utf-8')

    @staticmethod
    def decrypt(key_arn: str, text: str) -> str:
        ciphertext_blob = b64decode(text)
        response = KMS_CLIENT.decrypt(KeyId=key_arn, CiphertextBlob=ciphertext_blob)
        return response['Plaintext'].decode('utf-8')
