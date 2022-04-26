# Import Libraries
import os
import pandas as pd
import numpy as np
import requests
import json
import time
import random
import sys

# Override default settings
sys.setrecursionlimit(10000)

# Get vault secrets for rapid API host Name and API Key
x_rapidapi_hname= os.environ["X_RAPIDAPI_HOST"]
x_rapidapi_kname= os.environ["X_RAPIDAPI_KEY"]

def miner(url, querystring):
    """
    DESCRIPTION: THe purpose of this method is to pass query string, API
    url and extract response dictionary 
    INPUT: querystring, url
    OUTPUT: API response dictionary
    """
    err_mes= 'You have exceeded the rate limit per second for your plan, MEGA, by the API provider'

    headers= {
            'x-rapidapi-host': x_rapidapi_hname, 
            'x-rapidapi-key' : x_rapidapi_kname
    }

    try:
        response= requests.request("GET", url, headers= headers, params= querystring)
        payload= response.json()

        if err_mes in list(payload.values()):
            time.sleep(random.random()+ 4)
            return miner(url, querystring)

        else:
            return payload

    except ValueError:
        pass
    