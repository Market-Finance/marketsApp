from function_mover import *
from query_string import *


def trending_tickers_operator(context, auto_complete_list):
    """
    DESCRIPTION: The purpose of this operator function is to extract 
                 trending tickers stocks, and read it to blob and datalake
    INPUT: context, and auto_complete_list
    OUTPUT: none
    """
    # extract trending ticker stocks, and read it to blob and datalake
    querystring_list= trending_tickers_query_string(auto_complete_list)
    trending_tickers_activity= [
        context.call_activity('trending_tickers', querystring) for
            querystring in querystring_list if querystring]

    trending_tickers_list= yield context.task_all(trending_tickers_activity)
    trending_tickers_mover_out(trending_tickers_list)
    

def quotes_operator(context, auto_complete_list):
    """
    DESCRIPTION: The purpose of this operator function is to extract quotes
                 stock, and read it to blob and datalake
    INPUT: context, and auto_complete_list
    OUTPUT: none
    """
    # extract stock quotes, and read it to blob and datalake
    querystring_list= quotes_query_string(auto_complete_list)
    quotes_activity= [
        context.call_activity('quotes', querystring) for 
            querystring in querystring_list if querystring]

    quotes_list= yield context.task_all(quotes_activity)
    quotes_mover_out(quotes_list)
    