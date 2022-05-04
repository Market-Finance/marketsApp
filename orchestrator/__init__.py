import logging
import json
import os
from datetime import datetime
import azure.functions as func
import azure.durable_functions as df

from . import function_mover as fm
from . import query_string as qs


def orchestrator_function(context: df.DurableOrchestrationContext):

    # Auto complete read data from blob storage
    auto_complete_list= fm.auto_complete_mover_in()

    # Extract trending ticker stocks, and load it to blob and datalake
    querystring_list= qs.trending_tickers_query_string(auto_complete_list)
    trending_tickers_activity= [
        context.call_activity('trending_tickers', querystring) for
            querystring in querystring_list]
    
    trending_tickers_list= yield context.task_all(trending_tickers_activity)
    fm.trending_tickers_mover_out(trending_tickers_list)
    del trending_tickers_list

    # Extract stock quotes, and load it to blob and datalake
    querystring_list= qs.quotes_query_string(auto_complete_list)
    quotes_activity= [
        context.call_activity('quotes', querystring) for 
            querystring in querystring_list]

    quotes_list= yield context.task_all(quotes_activity)
    fm.quotes_mover_out(quotes_list)
    del quotes_list 
    
    # Popular_watchlist extract and load
    popular_watchlist_list= yield context.call_activity('popular_watchlist', "None")

    # Watchlist_details extract and load
    querystring_list= qs.watchlist_details_query_string_list(popular_watchlist_list)
    watchlist_details_activity= [ 
        context.call_activity('watchlist_details', querystring) 
            for querystring in querystring_list]

    watchlist_details_list= yield context.task_all(watchlist_details_activity)
    
    # Watchlist_performance extract and load
    querystring_list= qs.watchlist_performance_query_string_list(watchlist_details_list)
    watchlist_performance_activity= [
        context.call_activity('watchlist_performance', querystring)
            for querystring in querystring_list]

    watchlist_performance_list= yield context.task_all(watchlist_performance_activity)
    
    # Moving out all the files to blob and data lake storage
    fm.trending_tickers_mover_out(trending_tickers_list)
    del trending_tickers_list
    fm.watchlist_performance_mover_out(watchlist_performance_list)
    del watchlist_performance_list
    fm.watchlist_details_mover_out(watchlist_details_list)
    del watchlist_details_list
    fm.popular_watchlist_mover_out(popular_watchlist_list)
    del popular_watchlist_list       

    return "Success!"

main= df.Orchestrator.create(orchestrator_function)