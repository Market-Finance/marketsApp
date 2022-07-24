# Import Libraries
import os
import pandas as pd
import numpy as np 
import requests
import json
import time
import random
import sys
from shared.fun_request import miner

# Override default settings
sys.setrecursionlimit(10000)

import shared.function_mover as fm
import shared.query_string as qs

def main(name:str):
    """
    DESCRIPTION: The purpose of this function is to pass a the query string 
                 and extract trending tickers for a given stock
    INPUT: query string dictionary
    OUTPUT: trending tickers dictionary    
    """
    # Auto complete read data from blob storage
    querystring_list= fm.auto_complete_mover_in()
    trending_tickers_list= list()

    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-trending-tickers"
    
    # Extract trending ticker stocks, and load it to blob and datalake
    for querystring in querystring_list:
        trending_tickers_dict= miner(url, querystring)
        trending_tickers_list.append(trending_tickers_dict)
    
    # Moving out the file to blob and data lake
    fm.trending_tickers_mover_out(trending_tickers_list)

    return "Success!"
