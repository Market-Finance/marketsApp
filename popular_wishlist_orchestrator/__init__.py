import logging
import json
import os
from datetime import datetime
import azure.functions as func
import azure.durable_functions as df
from query_string import *
from function_mover import *

def orchestrator_function(context: df.DurableOrchestrationContext):
    
    #  popular_watchlist extract and load
    popular_watchlist_list= yield context.call_activity('popular_watchlist', "None")
    popular_watchlist_mover_out(popular_watchlist_list)
    
    # watchlist_details extract and load
    querystring_list= watchlist_details_query_string_list(popular_watchlist_list)
    watchlist_details_activity= [ 
        context.call_activity('watchlist_details', querystring) 
            for querystring in querystring_list if querystring]
    
    watchlist_details_list= yield context.task_all(watchlist_details_activity)
    watchlist_details_mover_out(watchlist_details_list)

    # watchlist_performance extract and load
    querystring_list= watchlist_performance_query_string_list(watchlist_details_list)
    watchlist_performance_activity= [
        context.call_activity('watchlist_performance', querystring)
            for querystring in querystring_list if querystring]

    watchlist_performance_list= yield context.task_all(watchlist_performance_activity)
    watchlist_performance_mover_out()

    return 'Success'

main= df.Orchestrator.create(orchestrator_function)