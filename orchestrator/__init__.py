from enum import auto
import logging
import json
import os
from datetime import datetime
import profile
import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    #activity_function_list= ["trending_tickersSubOrch"]
    #"marketSubOrch", "trending_tickersSubOrch", "quotesSubOrch"

    # Run multiple device provisioning flows in parallel
    #provisioning_tasks=[]
    #for func_name in activity_function_list:
        #provision_task= context.call_sub_orchestrator(func_name)
        #provisioning_tasks.append(provision_task)

    #yield context.task_all(provisioning_tasks)
    
    provision_trending_task= context.call_sub_orchestrator("trending_tickersSubOrch")
    provision_market_task= context.call_sub_orchestrator("marketSubOrch")
    provision_quotes_task= context.call_sub_orchestrator("quotesSubOrch")

    yield context.task_all(provision_trending_task)
    yield context.task_all(provision_market_task)
    yield context.task_all(provision_quotes_task)

    return "Success"

main= df.Orchestrator.create(orchestrator_function)