import os

from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from dotenv import load_dotenv


def retrive_secret(secret_name: str):
    credential = DefaultAzureCredential()

    keyVaultName = os.getenv("KEY_VAULT_NAME")
    KVUri = f"https://{keyVaultName}.vault.azure.net"

    client = SecretClient(vault_url=KVUri, credential=credential)

    retrieved_secret = client.get_secret(secret_name)

    return retrieved_secret.value
