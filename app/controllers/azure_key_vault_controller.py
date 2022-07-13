import os

from flask import jsonify
from azure.identity import DefaultAzureCredential
from azure.keyvault.keys import KeyClient


def create_key():
    credential = DefaultAzureCredential()
    keyVaultName = os.getenv("KEY_VAULT_NAME")
    KVUri = f"https://{keyVaultName}.vault.azure.net"

    key_client = KeyClient(vault_url=KVUri, credential=credential)

    # Create an RSA key
    rsa_key = key_client.create_rsa_key("rsa-key-name", size=2048)
    print(rsa_key.name)
    print(rsa_key.key_type)

    # Create an elliptic curve key
    ec_key = key_client.create_ec_key("ec-key-name", curve="P-256")
    print(ec_key.name)
    print(ec_key.key_type)

    return {"msg": "ok"}


def retrive_key():
    credential = DefaultAzureCredential()

    keyVaultName = os.getenv("KEY_VAULT_NAME")
    KVUri = f"https://{keyVaultName}.vault.azure.net"

    key_client = KeyClient(vault_url=KVUri, credential=credential)
    key = key_client.get_key("ec-key-name")
    print(key.key)
    return jsonify({"key": key.key})


"""
#Create and retrive a secrete from azure
import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

keyVaultName = os.environ["KEY_VAULT_NAME"]
KVUri = f"https://{keyVaultName}.vault.azure.net"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

secretName = input("Input a name for your secret > ")
secretValue = input("Input a value for your secret > ")

print(f"Creating a secret in {keyVaultName} called '{secretName}' with the value '{secretValue}' ...")

client.set_secret(secretName, secretValue)

print(" done.")

print(f"Retrieving your secret from {keyVaultName}.")

retrieved_secret = client.get_secret(secretName)

print(f"Your secret is '{retrieved_secret.value}'.")
print(f"Deleting your secret from {keyVaultName} ...")

poller = client.begin_delete_secret(secretName)
deleted_secret = poller.result()

print(" done.")
"""
