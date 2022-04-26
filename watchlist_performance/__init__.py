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

def main(queryString):
    """
    DESCRIPTION: The purpose of this function is to pass a query string 
                 and extract market watchlist performance for a given stock
    INPUT: query string dictionary
    OUTPUT: market watchlist performance dictionary
    """
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-watchlist-performance"
    watchlist_performance_dict= miner(url, queryString)
    return watchlist_performance_dict