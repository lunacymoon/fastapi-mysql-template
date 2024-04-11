from base64 import b64decode

from aws_encryption_sdk import (
    CommitmentPolicy,
    EncryptionSDKClient,
    StrictAwsKmsMasterKeyProvider,
)

client = EncryptionSDKClient(commitment_policy=CommitmentPolicy.REQUIRE_ENCRYPT_ALLOW_DECRYPT)


def decrypt(key_arn: str, ciphertext: bytes) -> bytes:
    kms_kwargs = dict(key_ids=[key_arn])
    master_key_provider = StrictAwsKmsMasterKeyProvider(**kms_kwargs)
    cycled_plaintext, _ = client.decrypt(source=ciphertext, key_provider=master_key_provider)
    return cycled_plaintext


def decrypt_user_name(key_arn: str, user_name: str) -> str:
    return decrypt(key_arn, b64decode(user_name)).decode('utf-8')
