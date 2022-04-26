from shared import mover as mo

def auto_complete_mover_in():
    """
    DESCRIPTION: The purpose of this function is to download auto-complete
                 from blob storage location 
    INPUT: None
    OUTPUT: encoded string 
    """
    # Blob file path and file_name source
    blob_file_path= 'MarketFinance/common'
    blob_file_name= 'auto_complete.json'

    data= mo.blob_storage_download(blob_file_path, blob_file_name)
    return data

def quotes_mover_out(inMemory_data):
    """
    DESCRIPTION: The purpose of this function is to move mined quotes 
                 to this desired blob storage and data lake location
    INPUT: None
    OUTPUT: status string
    """
    # Blob file path and file_name destination
    blob_file_path= 'MarketFinance/market'
    blob_file_name= 'quotes.json'

    # Data Lake path and file_name destination
    data_lake_file_path= 'market/quotes'
    data_lake_file_name= 'quotes'

    mo.blob_storage_upload(inMemory_data, blob_file_path, blob_file_name)
    mo.data_lake_storage_upload(inMemory_data, data_lake_file_path, data_lake_file_name)

    return "Success!"

def trending_tickers_mover_out(inMemory_data):
    """
    DESCRIPTION: The purpose of this function is to move mined trending tickers
                 to this desired blob storage and data lake location
    INPUT: None
    OUTPUT: status string
    """
    # Blob file path and file_name destination
    blob_file_path= 'MarketFinance/market'
    blob_file_name= 'trending_tickers.json'

    # Data Lake path and file_name destination
    data_lake_file_path= 'market/trending_tickers'
    data_lake_file_name= 'trending_tickers'

    mo.blob_storage_upload(inMemory_data, blob_file_path, blob_file_name)
    mo.data_lake_storage_upload(inMemory_data, data_lake_file_path, data_lake_file_name)

    return "Success!"

