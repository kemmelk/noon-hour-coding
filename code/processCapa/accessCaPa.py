# -*- coding: utf-8 -*-
"""
Script designed to access CaPa data, there are two sources for this data
The first is from Environment Canada, and the second is archived data from the 
University of Saskatchewan
Created on Mon Apr 25 09:09:16 2022

@author: KEmmelkamp
"""

import requests
import datetime as dt


def getCapaNames(start_date = "2011-04-06 00", end_date = "2011-04-06 00"):
    """ Create a index of file names to loop throughto be used with Download
        CaPa Data
    :param start_date: beginning timeframe for download as String
    :param end_date: end timeframe for download as String
    :return file_names: an index of filenames to download
    """
    print(start_date)
    print(end_date)
    file_names = []
    if dt.datetime.fromisoformat(start_date)< dt.datetime(2011, 4, 6, 00):
        print("Dataset does not include dates before 2011-04-06 00:00:00\n"
              + "Please choose a relevant date period")
    elif dt.datetime.fromisoformat(start_date) > dt.datetime.fromisoformat(end_date):
        print("End date cannot be before start date, please choose a relevant date period")
    else: 

        time_step = dt.datetime.fromisoformat(start_date)

        # creating the timesteps necessary to step through
        while time_step <= dt.datetime.fromisoformat(end_date):
            if time_step < dt.datetime(2012, 10, 3, 0):
                file_names.append(time_step.strftime("%Y%m%d%H") \
                                  + "_000_CMC_RDPA_APCP-006-0700cutoff_SFC_0_ps15km.grib2")
            else:
                file_names.append(time_step.strftime("%Y%m%d%H") \
                                  + "_000_CMC_RDPA_APCP-006-0700cutoff_SFC_0_ps10km.grib2")
            time_step = time_step + dt.timedelta(hours = 6)
        
    
    return file_names

    
def DownloadCapaData(start_date = "2011-04-06 00", end_date = "2011-04-06 00"):
    """ Download the CaPa data from the university of Saskatchewans database
        saves the file in the download folder
    :param start_date: beginning timeframe for download as String
    :param end_date: end timeframe for download as String
        these two parameters should be formatted like this yyyymmddhh
        ie. 2011040600 (which is the earliest this dataset goes)
        hours is optional, if hour is included it will automatically assume
        hours as 00
    """
 
    Remote_URL = "https://collaboration.cmc.ec.gc.ca/science/outgoing/capa.grib/"
    
    file_names = getCapaNames(start_date=start_date, end_date=end_date)
    output_files = []
    for file in file_names:
        data = requests.get(Remote_URL + file)
        output_files.append("output/" + file)
        with open(("output/" + file), 'wb') as download:
            download.write(data.content)
            
    return output_files



    
