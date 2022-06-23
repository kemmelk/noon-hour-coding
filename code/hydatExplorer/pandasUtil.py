# -*- coding: utf-8 -*-
"""
A few utilities to make my life easier while using python
Created on Mon Jun 20 14:39:34 2022

@author: KEmmelkamp
"""

import pandas as pd

def merge_rows(pd, data):
    """ Takes a pandas dataframe and merges any rows which appear to be 
        duplicates. Requires user input to decide which column to merge.
    
    """
