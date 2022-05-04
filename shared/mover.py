# Import Libraries
import os
import json
from io import StringIO
import azure.functions as func
import azure.durable_functions as df
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
from azure.storage.filedatalake import DataLakeServiceClient
from azure.storage.blob import BlobServiceClient
from datetime import datetime

# Get vault secrets for blob, datalake and key_valult
key_vault_name= os.environ["KEY_VAULT_NAME"]
blob_secret_key= os.environ["ABS_SECRET_NAME"]
datalake_secret_key= os.environ["ADLS_SECRET_NAME"]
key_vault_url= f"https://{key_vault_name}.vault.azure.net"

# Authenticate and securely retrieve Key Vault secret for access key value.
az_credential= DefaultAzureCredential()

def blob_container_service_client():
    """
    DESCRIPTION: The purpose of this function is to establish a datalake service client
    INPUT: NONE
    OUTPUT: ads_container_client: object
    """
    abs_acct_name= 'blobmarketfinance'
    abs_container_name= 'marketessential'
    abs_acct_url= f'https://{abs_acct_name}.blob.core.windows.net/'
    
    # Initialize Azure Service SDK Client for blob storage
    ads_service_client= BlobServiceClient(
        account_url= abs_acct_url,
        credential= az_credential
    )
    ads_container_client= ads_service_client.get_container_client(container=abs_container_name)
    return ads_container_client

def datalake_service_client():
    """
    DESCRIPTION: The purpose of this function is to establish a datalake service client
    INPUT: NONE
    OUTPUT: adls_service_client: object
    """
    adls_acct_name= 'dlakemarketfinance'
    adls_acct_url= f'https://{adls_acct_name}.dfs.core.windows.net/'

    # Initialize Azure Service SDK Client for data lake
    adls_service_client= DataLakeServiceClient(
        account_url= adls_acct_url, 
        credential= az_credential
    )
    return adls_service_client

def return_blob_files(container_client):
    """
    DESCRIPTION: The purpose of this function is to return all the blob files
    INPUT: container_cliet
    OUTPUT: list of blob files
    """
    blob_files= [blob for blob in container_client.list_blobs()]
    return blob_files

def blob_storage_download(file_path:str, file_name:str): 
    """
    DESCRIPTION: The purpose of this function is to download a given json file 
                 to Azure function's deployment memory
    INPUT: file_path:str, file_name:str
    OUTPUT: json file or dict
    """
    blob_path= f'{file_path}/{file_name}'
    container_client= blob_container_service_client()
    blob_client= container_client.get_blob_client(blob=blob_path)

    # Retrive extract blob file
    blob_download= blob_client.download_blob()

    # Download the blob octet-stream file into string
    blob_data= StringIO(blob_download.content_as_text())

    # Read blob file string as json, dictionary
    blob_data= StringIO(blob_download.content_as_text())
    str_values= blob_data.getvalue()
    data_dict= list(eval(str_values))
    return data_dict

def blob_storage_upload(inMemory_data, file_path:str, file_name:str):
    """
    DESCRIPTION: The purpose of this function is to upload a given json file to a 
                 specific blob storage location  
    INPUT: inMemory_data, file_path, file_name
    OUTPUT: Dictionary with interested_key
    """
    blob_path= f'{file_path}/{file_name}'
    container_client= blob_container_service_client()
    blob_client= container_client.get_blob_client(blob=blob_path)

    # Upload json file to blob
    response= blob_client.upload_blob(str(inMemory_data))
    return response

def data_lake_storage_upload(inMemory_data, file_path, file_name):
    """
    DESCRIPTION: The purpose of this function is to upload a given json file to a
                 specific location to data lake storage
    INPUTS: data: json, file_path:str, file_name:str
    RETURNS: bool: True or False
    """
    service_client= datalake_service_client()
    now = datetime.today().strftime("%Y%m%d_%H%M%S")
    filesystem_name= 'processed-data'
    data_type= 'json'
    datalake_path= f'{file_path}/{file_name}_{now}.{data_type}'
    file_client= service_client.get_file_client(filesystem_name, datalake_path)

    # encode the dictionary to bytes
    encode_inMemory_data= json.dumps(inMemory_data).encode('utf-8')
    
    # Upload json file to Data Lake 
    file_client.upload_data(data= encode_inMemory_data, overwrite= True)
    return True

def blob_storage_delete(file_path, file_name): 
    """
    DESCRIPTION: The purpose of this function is to delete a given json file in
                 blob storage
    INPUTS: file_path:str, file_name:str
    RETURN: bool: True or False 
    """
    container_client= blob_container_service_client()
    blob_path= f'{file_path}/{file_name}'
    blob_client= container_client.get_blob_client(blob=blob_path)
    blob_client.delete_blob(delete_snapshots='include')
    return True