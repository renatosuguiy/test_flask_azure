from http import HTTPStatus
from flask import jsonify
import os, uuid
from azure.storage.blob import (
    BlobServiceClient,
    BlobClient,
    ContainerClient,
    __version__,
)


def return_name(name):
    result = {"msg": name}

    return jsonify(result), HTTPStatus.OK


def list_files_azure():

    try:
        print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")
        connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        print("\nListing blobs...")

        # Quick start code goes here
        # List the blobs in the container
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        container_name = "container-renato"
        container_client = blob_service_client.get_container_client(container_name)

        blob_list = container_client.list_blobs()
        for blob in blob_list:
            print(f"\n{blob.name}")
        return jsonify({"result": "blob_list"})

    except Exception as ex:
        print("Exception:")
        print(ex)


def create_container():
    try:
        print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")
        connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

        # Quick start code goes here

        # Create the BlobServiceClient object which will be used to create a container client
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)

        # Create a unique name for the container
        container_name = "novo-container2"

        # Create the container
        container_client = blob_service_client.create_container(container_name)

        return {"msg": f"Created container {container_name}"}, HTTPStatus.OK
    except Exception as ex:
        print("Exception:")
        print(ex)

        return jsonify({"msg": str(ex)}), HTTPStatus.INTERNAL_SERVER_ERROR
