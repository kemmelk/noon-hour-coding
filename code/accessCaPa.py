# -*- coding: utf-8 -*-
"""
Script designed to access CaPa data, there are two sources for this data
The first is from Environment Canada, and the second is archived data from the 
University of Saskatchewan
Created on Mon Apr 25 09:09:16 2022

@author: KEmmelkamp
"""

import requests

"""


remoteURL = "https://collaboration.cmc.ec.gc.ca/science/outgoing/capa.grib/2011040600_000_CMC_RDPA_APCP-006-0700cutoff_SFC_0_ps15km.grib2"
localFile = "local_copy.grib2"

data = requests.get(remoteURL)

with open(localFile, 'wb') as file:
    file.write(data.content)

"""

    
def DownloadCaPaData():
    """ Download the CaPa data from the university of Saskatchewans database
        saves the file in the download folder
    :param start_date: beginning timeframe for download as String
    :param end_date: end timeframe for download as String
        these two parameters should be formatted like this yyyymmddhh
        ie. 2011040600 (which is the earliest this dataset goes)
        hours is optional, if hour is included it will automatically assume
        hours as 00
    """
 
    Remote_URL = "https://collaboration.cmc.ec.gc.ca/science/outgoing/capa.grib/2011040600_000_CMC_RDPA_APCP-006-0700cutoff_SFC_0_ps15km.grib2"
    local_File = "download_files/local_copy.grib2"
    
    data = requests.get(Remote_URL)

    with open(local_File, 'wb') as file:
        file.write(data.content)

def main():
    DownloadCaPaData()
    
