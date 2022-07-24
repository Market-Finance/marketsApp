import logging
import json
import os
from datetime import datetime
import azure.functions as func
import azure.durable_functions as df

import shared.function_mover as fm
import shared.query_string as qs 

def orchestrator_function(context: df.DurableOrchestrationContext):
    # Auto complete read data from blob storage
    auto_complete_list= fm.auto_complete_mover_in()

    # Extract stock quotes, and load it to blob and datalake
    querystring_list= qs.quotes_query_string(auto_complete_list)
    quotes_activity= [
        context.call_activity('quotes', querystring) for
            querystring in querystring_list]
    quotes_list= yield context.task_all(quotes_activity)

    # Moving out all the files to blob and data lake storage
    fm.quotes_mover_out(quotes_list)

    return "Success!"

main= df.Orchestrator.create(orchestrator_function)
