# Import Libraries
from collections import defaultdict
import numpy as np

def watchlist_details_query_string_list(data:list):
    """
    DESCRIPTION: The purpose of this function is to extract the query string
    for the get-watchlist-details API
    INPUT: List of JSON [get_popular_watchlist]
    OUTPUT: List of query string- List of dictionaries
    """
    # loop through get_popular_watchlist json to extract symbol and region
    # and check for listed exchages
    query_list= list()
    for i in range(len(data)):
        for j in range(len(data[i]['finance']['result'])):
            for k in range(len(data[i]['finance']['result'][j]['portfolios'])):
                user_Id= data[i]['finance']['result'][j]['portfolios'][k]['userId']
                pfId= data[i]['finance']['result'][j]['portfolios'][k]['pfId']

                querydict= {"userId": user_Id, "pfId": pfId}
                query_list.append(querydict)

    return query_list


def watchlist_performance_query_string_list(data:list):
    """
    DESCRIPTION: The purpose of this method is to extract the
    query string for the get-watchlist-performance API
    INPUT: List of JSON [get-watchlist]
    OUTPUT: List of query strings- List of dictionaries
    """
    # Loop through get-watchlist-performance json to extract userId, pfId, 
    # Symbols, Region
    query_list = list()
    for d in range(len(data)):
        for fr in range(len(data[d]['finance']['result'])):
            for p in range(len(data[d]['finance']['result'][fr]['portfolios'])):
                pfId = data[d]['finance']['result'][fr]['portfolios'][p]['pfId']
                userId = data[d]['finance']['result'][fr]['portfolios'][p]['userId']
                symbol_list = list()
                for pot in range(len(data[d]['finance']['result'][fr]['portfolios'][p]['positions'])):
                    symbol = data[d]['finance']['result'][fr]['portfolios'][p]['positions'][pot]['symbol']
                    symbol_list.append(symbol)

                dict = {'pfId': pfId, 'userId': userId, 'symbols': symbol_list}
                query_list.append(dict)

# Create list of dictionaries with region and symbols
    query_dict_lists = list()
    for i in range(len(query_list)):
            symbols = (','.join(query_list[i]['symbols']))
            query_dict = {"userId": query_list[i]['userId'], "pfId": query_list[i]['pfId'], "symbols":symbols}
            query_dict_lists.append(query_dict)

    return query_dict_lists

def trending_tickers_query_string(data:list):
    """
    DESCRIPTION: The purpose of the method is to extract the query string
                 for the get-trending-tickers
    INPUT: List of JSON [auto-complete]
    OUTPUT: List of query strings- List of dictionaries
    """
    region_list = list()
    for i in range(len(data)):
        region = data[i]['region']
        region_list.append(region)

    queryString_list = [{"region": i} for i in np.unique(region_list)]

    return queryString_list

def quotes_query_string(data:list):
    """
    DESCRIPTION: The purpose of the method is to extract the query string 
                 for the get-quotes API 
    INPUT: List of JSON [auto-complete]
    OUTPUT: List of query strings - List of dictionaries
    """
    # Stock and region of interest- make sure its defined in the same order
    exchange= ('Australian', 'NASDAQ')
    regions= ('AU', 'US')

    query_dict_lists = list()
    for e in range(len(exchange)):
        # Loop through auto-complete json to extract symbols and regions 
        # and check for listed exchanges
        query_lists= list();
        for i in range(len(data)):
            for j in range(len(data[i]['auto_complete']['quotes'])):
                if data[i]['auto_complete']['quotes'][j]['exchDisp'] in exchange[e]:
                    query_list = (data[i]['auto_complete']['quotes'][j]['symbol'], regions[e])
                    query_lists.append(query_list)
        else:
            pass  

        # Chuck the listed exchange companies and region list
        chunk_list = list()
        for i in range(0, len(query_lists), 50):
            chunk = query_lists[i: i+49]
            chunk_list.append(chunk) 

        # Group the list by region and concatenate the symbols to a single string
        chunk_dict_lists= list()
        for i in range(len(chunk_list)):
            res = defaultdict(list)
            for v, k in chunk_list[i]: res[k].append(v)
            chunk_dict= [{'region':k, 'symbols':v} for k,v in res.items()]
            chunk_dict_lists.append(chunk_dict)

        # Create list of dictionaries with region and symbols
        for n in range(len(chunk_dict_lists)):
            for i in range(len(chunk_dict_lists[n])):
                symbols = (','.join(chunk_dict_lists[n][i]['symbols']))
                query_dict = {"region":regions[e], "symbols":symbols}
                query_dict_lists.append(query_dict)         

    return query_dict_lists