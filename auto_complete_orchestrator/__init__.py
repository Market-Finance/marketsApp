import logging
import json
import os
from datetime import datetime
import azure.functions as func
import azure.durable_functions as df
from function_mover import auto_complete_mover_in
from operators import *

def orchestrator_function_1(context: df.DurableOrchestrationContext):

    # Auto complete read data from blob storage
    auto_complete_list= auto_complete_mover_in()

    # Trending tickers extract and load
    trending_tickers_operator(context, auto_complete_list)

    # Quotes tickets extract and load
    quotes_operator(context, auto_complete_list)
    
    return 'Success'

main= df.Orchestrator.create(orchestrator_function_1) 