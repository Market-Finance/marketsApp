# Import Libraries
import os
import pandas as pd
import numpy as np 
import requests
import json 
import time 
import random 
import sys
from shared.fun_request import *

# Override default settings
sys.setrecursionlimit(10000)

import shared.function_mover as fm
import shared.query_string as qs

def main(name:str):
    """
    DESCRIPTION: The purpose of the method is to pass a query string
                 and extract market quotes for a given stock
    INPUT: query string dictionary 
    OUTPUT: dictionary market quotes
    """
    # Auto complete read data from blob storage
    querystring_list= fm.auto_complete_mover_in()
    quotes_list= list()
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"
    
    # Extract market quotes and load it to blob and datalake
    for querystring in querystring_list:
        quotes_dict= miner(url, querystring)
        quotes_list.append(quotes_dict) 
    
    # Moving out the file to blob and data lake
    fm.quotes_mover_out(quotes_list)

    return "Success!"