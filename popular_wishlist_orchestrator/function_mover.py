from shared import mover as mo


def popular_watchlist_mover_out(inMemory_data):
    """
    DESCRIPTION: The purpose of this function is to move mined popular watchlist
                 to this desired blob storage and data lake location
    INPUT: inMemeory_data
    OUTPUT: status string
    """
    # Blob file path and file_name destination
    blob_file_path= 'MarketFinance/market'
    blob_file_name= 'popular_watchlist.json'

     # Data Lake path and file_name destination
    data_lake_file_path= 'market/popular_watchlist'
    data_lake_file_name= 'popular_watchlist'    

    mo.blob_storage_upload(inMemory_data, blob_file_path, blob_file_name)
    mo.data_lake_storage_upload(inMemory_data, data_lake_file_path, data_lake_file_name)

    return "Success!"

def watchlist_details_mover_out(inMemory_data):
    """
    DESCRIPTION: The purpose of this function is to move mined watchlist details
                 to this desired blob storage and data lake location
    INPUT: inMemeory_data
    OUTPUT: status string
    """
    # Blob file path and file_name destination
    blob_file_path= 'MarketFinance/market'
    blob_file_name= 'watchlist_details.json'

    # Data Lake path and file_name destination
    data_lake_file_path= 'market/watchlist_details'
    data_lake_file_name= 'watchlist_details'    

    mo.blob_storage_upload(inMemory_data, blob_file_path, blob_file_name)
    mo.data_lake_storage_upload(inMemory_data, data_lake_file_path, data_lake_file_name)
    
    return "Success!"

def watchlist_performance_mover_out(inMemory_data):
    """
    DESCRIPTION: The purpose of this function is to move mined watchlist performance
                 to this desired blob storage and data lake location
    INPUT: inMemeory_data
    OUTPUT: status string
    """
    # Blob file path and file_name destination
    blob_file_path= 'MarketFinance/market'
    blob_file_name= 'watchlist_performance_mover.json'

    # Data Lake path and file_name destination
    data_lake_file_path= 'market/watchlist_performance_mover'
    data_lake_file_name= 'watchlist_performance_mover'    

    mo.blob_storage_upload(inMemory_data, blob_file_path, blob_file_name)
    mo.data_lake_storage_upload(inMemory_data, data_lake_file_path, data_lake_file_name)

    return "Success!"




