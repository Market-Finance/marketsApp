# Import Libraries
import os
import pandas as pd
import numpy as np
import requests
import csv
import json
from itertools import groupby
import sys
import random
import time

from shared.fun_request import *

# Override default settings
sys.setrecursionlimit(10000)

# Get vault secrets for rapid API Host Name and API Key 
x_rapidapi_hname= os.environ["X_RAPIDAPI_HOST"]
x_rapidapi_kname= os.environ["X_RAPIDAPI_KEY"]

def popular_watchlist(name:str):
    """
    DESCRIPTION: The purpose of this function is to extract get_popular watchlists
    INPUT: NONE
    OUTPUT: get popular watchlists dictionary
    """
    err_mes = 'You have exceeded the rate limit per second for your plan, MEGA, by the API provider'
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-popular-watchlists"

    headers = {
        'x-rapidapi-host': x_rapidapi_hname,
        'x-rapidapi-key': x_rapidapi_kname
    }

    try:
        response= requests.request("GET", url, headers= headers)
        payload= response.json()
    
        if err_mes in list(payload.values()):
            time.sleep(random.random()+ 4)
            return popular_watchlist(name)
        else:
            return payload
    
    except ValueError:
        pass

def main(name:str):
    popular_watchlist_dict= popular_watchlist(name)
    return popular_watchlist_dict