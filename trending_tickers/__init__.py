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

def main(querystring):
    """
    DESCRIPTION: The purpose of this function is to pass a the query string 
                 and extract trending tickers for a given stock
    INPUT: query string dictionary
    OUTPUT: trending tickers dictionary    
    """
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-trending-tickers"
    trending_tickers_dict= miner(url, querystring)
    return trending_tickers_dict
