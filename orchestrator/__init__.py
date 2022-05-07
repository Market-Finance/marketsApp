from enum import auto
import logging
import json
import os
from datetime import datetime
import profile
import azure.functions as func
import azure.durable_functions as df

from shared import funcion_mover as fm

def orchestrator_function(context: df.DurableOrchestrationContext):
    activity_function_list= ["auto_completeSubOrch", "marketSubOrch"]

    # Run multiple device provisioning flows in parallel
    provisioning_tasks=[]
    for func_name in activity_function_list:
        provision_task= context.call_sub_orchestrator(func_name)
        provisioning_tasks.append(provision_task)

    yield context.task_all(provisioning_tasks)

    return "Success"

main= df.Orchestrator.create(orchestrator_function)