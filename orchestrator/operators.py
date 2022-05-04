import azure.durable_functions as df

from . import function_mover as fm
from . import query_string as qs


def trending_tickers_operator(context, auto_complete_list):
    """
    DESCRIPTION: The purpose of this operator function is to extract 
                 trending tickers stocks, and read it to blob and datalake
    INPUT: context, and auto_complete_list
    OUTPUT: none
    """
    # extract trending ticker stocks, and read it to blob and datalake
    querystring_list= qs.trending_tickers_query_string(auto_complete_list)
    trending_tickers_activity= [
        context.call_activity('trending_tickers', querystring) for
            querystring in querystring_list]

    trending_tickers_list= yield context.task_all(trending_tickers_activity)
    fm.trending_tickers_mover_out(trending_tickers_list)
    

def quotes_operator(context, auto_complete_list):
    """
    DESCRIPTION: The purpose of this operator function is to extract quotes
                 stock, and read it to blob and datalake
    INPUT: context, and auto_complete_list
    OUTPUT: none
    """
    # extract stock quotes, and read it to blob and datalake
    querystring_list= qs.quotes_query_string(auto_complete_list)
    quotes_activity= [
        context.call_activity('quotes', querystring) for 
            querystring in querystring_list]

    quotes_list= yield context.task_all(quotes_activity)
    fm.quotes_mover_out(quotes_list)
    

    # Watchlist_performance extract and load it to blob and datalake
    querystring_list= qs.watchlist_performance_query_string_list(watchlist_details_list)
    watchlist_performance_activity= [
        context.call_activity('watchlist_performance', querystring)
            for querystring in querystring_list]

    watchlist_performance_list= yield context.task_all(watchlist_performance_activity)
    fm.watchlist_performance_mover_out(watchlist_performance_list)    
    
    # Auto complete read data from blob storage
    auto_complete_list= fm.auto_complete_mover_in()

    # Extract trending ticker stocks, and load it to blob and datalake
    querystring_list= qs.trending_tickers_query_string(auto_complete_list)
    trending_tickers_activity= [
        context.call_activity('trending_tickers', querystring) for
            querystring in querystring_list]
    
    trending_tickers_list= yield context.task_all(trending_tickers_activity)
    fm.trending_tickers_mover_out(trending_tickers_list)

    # Extract stock quotes, and load it to blob and datalake
    querystring_list= qs.quotes_query_string(auto_complete_list)
    quotes_activity= [
        context.call_activity('quotes', querystring) for 
            querystring in querystring_list]

    quotes_list= yield context.task_all(quotes_activity)
    fm.quotes_mover_out(quotes_list)
           
    return "Success"







        # Popular_watchlist extract and load it to blob and datalake
    popular_watchlist_list= yield context.call_activity('popular_watchlist', "None")
    fm.popular_watchlist_mover_out(popular_watchlist_list)

    # Watchlist_details extract and load it to blob and datalake
    querystring_list= qs.watchlist_details_query_string_list(popular_watchlist_list)
    watchlist_details_activity= [ 
        context.call_activity('watchlist_details', querystring) 
            for querystring in querystring_list]

    watchlist_details_list= yield context.task_all(watchlist_details_activity)
    fm.watchlist_details_mover_out(watchlist_details_list)  

    # Watchlist_performance extract and load it to blob and datalake
    querystring_list= qs.watchlist_performance_query_string_list(watchlist_details_list)
    watchlist_performance_activity= [
        context.call_activity('watchlist_performance', querystring)
            for querystring in querystring_list]

    watchlist_performance_list= yield context.task_all(watchlist_performance_activity)
    fm.watchlist_performance_mover_out(watchlist_performance_list)

    # Auto complete read data from blob storage
    auto_complete_list= fm.auto_complete_mover_in()

    # Extract trending ticker stocks, and load it to blob and datalake
    querystring_list= qs.trending_tickers_query_string(auto_complete_list)
    trending_tickers_activity= [
        context.call_activity('trending_tickers', querystring) for
            querystring in querystring_list]
    
    trending_tickers_list= yield context.task_all(trending_tickers_activity)
    fm.trending_tickers_mover_out(trending_tickers_list)

    # Extract stock quotes, and load it to blob and datalake
    querystring_list= qs.quotes_query_string(auto_complete_list)
    quotes_activity= [
        context.call_activity('quotes', querystring) for 
            querystring in querystring_list]

    quotes_list= yield context.task_all(quotes_activity)
    fm.quotes_mover_out(quotes_list)