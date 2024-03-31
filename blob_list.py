from azure.storage.blob import BlobServiceClient

def list_files_with_sas(account_url, container_name):
    blob_service_client = BlobServiceClient(account_url=account_url)

    container_client = blob_service_client.get_container_client(container_name)

    # List files in the container
    blob_list = container_client.list_blobs()

    # Print the names of the files
    print(f"Files in the '{container_name}' container:")
    for blob in blob_list:
        print(blob.name)

container_name = 'content'
account_url = 'https://michelleamesquita2.blob.core.windows.net'

list_files_with_sas( account_url, container_name)
