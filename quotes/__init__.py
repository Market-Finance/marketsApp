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

def main(querystring):
    """
    DESCRIPTION: The purpose of the method is to pass a query string
                 and extract market quotes for a given stock
    INPUT: query string dictionary 
    OUTPUT: dictionary market quotes
    """
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"
    quotes_dict= miner(url, querystring)
    return quotes_dict