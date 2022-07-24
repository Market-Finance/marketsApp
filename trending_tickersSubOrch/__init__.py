import logging
import json
import os
from datetime import datetime
import azure.functions as func
import azure.durable_functions as df

import shared.function_mover as fm
import shared.query_string as qs 

def orchestrator_function(context: df.DurbleOracleContext):
    # Auto complete read data from blob storage
    auto_complete_list= fm.auto_complete_mover_in()

    # Extract trending ticker stocks, and load it to blob and datalake
    querystring_list= qs.trending_tickers_query_string(auto_complete_list)
    trending_tickers_activity= [
        context.call_activity('trending_tickers', querystring) for
            querystring in querystring_list]
    trending_tickers_list= yield context.task_all(trending_tickers_activity)

    # Moving out all the files to blob and data lake storage
    fm.trending_tickers_mover_out(trending_tickers_list)

    return "Success!"

main= df.Orchestrator.create(orchestrator_function)