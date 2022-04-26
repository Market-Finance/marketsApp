# Import Libraries


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