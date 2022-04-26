# Import Libraries
from itertools import groupby
import numpy as np

def watchlist_details_query_string_list(data:list):
    """
    DESCRIPTION: The purpose of the method is to extract the query string
    for the get-watchlist-details API
    INPUT: List of JSON [get_popular_watchlist]
    OUTPUT: List of query string - List of dictionaries
    """
    # loop through get_popular_watchlist json to extract symbol and region
    # and check for listed exchages
    query_lists = list()
    for i in range(len(data['finance']['result'])):
        for j in range(len(data['finance']['result'][i])):
            user_Id = data['finance']['result'][i]['portfolios'][j]['userId']
            pfId = data['finance']['result'][i]['portfolios'][j]['pfId']

            querydict = {"userId": user_Id, "pfId": pfId}
            query_lists.append(querydict)

    return query_lists

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

def quotes_query_string(data:list, exchange:list):
    """
    DESCRIPTION: The purpose of the method is to extract the query string 
                 for the get-quotes API
    INPUT: List of JSON [auto-complete]
    OUTPUT: List of query strings - List of dictionaries
    """
    # Loop through auto-complete json to extract symbol and region
    # and check for listed exchanges
    query_lists = list()
    for i in range(len(data)):
        for j in range(len(data[i]['auto_complete']['quotes'])):
            if data[i]['auto_complete']['quotes'][j]['exchDisp'] in exchange:
                query_list = (data[i]['auto_complete']['quotes'][j]['symbol'], data[i]['region'])
                query_lists.append(query_list)
            else:
                pass
    
    # Chuck the listed exchange companies and region list
    chunk_list = list()
    for i in range(0, len(query_lists), 50):
        chunk = query_lists[i: i+49]
        chunk_list.append(chunk) 
    
    # Group the list by region and concatenate the symbols
    chunk_dict_list = list()
    for i in range(len(chunk_list)):
        res = dict()
        for key, val in groupby(sorted(chunk_list[i], key = lambda ele: ele[1]), key = lambda ele: ele[1]):
            res[key] = [ele[0] for ele in val]
            chunk_dict_list.append(res)

    # Create list of dictionaries with region and symbols
    query_dict_lists = list()
    for i in range(len(chunk_dict_list)):
        for key in chunk_dict_list[i].keys():
            symbols = (','.join(chunk_dict_list[i][key]))
            query_dict = {"region":key, "symbols":symbols}
            query_dict_lists.append(query_dict)
 
    return query_dict_lists