# import libraries
import os
import pandas as pd
import numpy as np
import requests
import csv
import json
import time
from itertools import groupby
import random
import sys

from shared.fun_request import miner

# Override default settings
sys.setrecursionlimit(10000)

def main(queryString):
    """
    DESCRIPTION: The purpose of the method is to pass a query string
    and extract market quotes for a given stock
    INPUT: query string dictionary
    OUTPUT: dictionary market quotes
    """
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-watchlist-detail"
    watchlist_details_dict= miner(url, queryString)
    return watchlist_details_dict

