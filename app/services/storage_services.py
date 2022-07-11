from http import HTTPStatus
from flask import jsonify
import os, uuid
from azure.storage.blob import (
    BlobServiceClient,
    BlobClient,
    ContainerClient,
    __version__,
)


def download_graph():

    try:
        download_file_path = "./fig1.png"
        print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")
        connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

        # Quick start code goes here
        # List the blobs in the container
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        container_name = "container-renato"
        container_client = blob_service_client.get_container_client(container_name)

        with open(download_file_path, "wb") as download_file:
            download_file.write(container_client.download_blob("fig1.png").readall())
        return True

    except Exception as ex:
        print("Exception:")
        print(ex)
        return False
