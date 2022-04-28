# -*- coding: utf-8 -*-
"""
Script designed to access CaPa data, there are two sources for this data
The first is from Environment Canada, and the second is archived data from the 
University of Saskatchewan
Created on Mon Apr 25 09:09:16 2022

@author: KEmmelkamp
"""


import datetime as dt
import requests, gdal, osr, sys

time = dt.datetime.fromisoformat('2011-04-07 23')
value = int(str(time.strftime("%H")))/6

def GetCapaNames(start_date = "2011-04-06 00", end_date = "2011-04-06 00"):
    """ Create a index of file names to loop throughto be used with Download
        CaPa Data
    :param start_date: beginning timeframe for download as String, this value
    should be divisible by 6 hours; if not it will choose
    :param end_date: end timeframe for download as String
    :return file_names: an index of filenames to download
    """

    file_names = []
    #check if start date is
    if dt.datetime.fromisoformat(start_date)< dt.datetime(2011, 4, 6, 00):
        start_date = dt.datetime(2011, 4, 6, 00)
        print("Dataset does not include dates before 2011-04-06 00:00:00\n"
              + "Datetime automatically set to 2011-04-06 00:00:00")
    
    print(dt.datetime.fromisoformat(start_date))
    
    if dt.datetime.fromisoformat(start_date) > dt.datetime.fromisoformat(end_date):
        print("End date cannot be before start date, please choose a relevant date period")
        sys.exit(1)
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
        saves the file in the download folder, 
    :param start_date: beginning timeframe for download as String, p
    :param end_date: end timeframe for download as String
        these two parameters should be formatted like this yyyymmddhh
        ie. 2011040600 (which is the earliest this dataset goes)
        hours is optional, if hour is included it will automatically assume
        hours as 00
    :return null:
    """
    #url to datasource, may want to make this a variable in case the url ever changes
    Remote_URL = "https://collaboration.cmc.ec.gc.ca/science/outgoing/capa.grib/"
    
    file_names = GetCapaNames(start_date=start_date, end_date=end_date)
    output_files = []
    for file in file_names:
        data = requests.get(Remote_URL + file)
        output_files.append("download_files/" + file)
        with open(("download_files/" + file), 'wb') as download:
            download.write(data.content)
            
    return output_files


def ReprojectCapa(fname, epsgID=4326):
    """Reproject the data from original projection (EPSG:3413) to a projection
    of the users choice
    By default this function uses band 1, which is accumulated precipitation 
    over 6 hours
    
    :param fname: file name of data as a string, this should be the downloaded
                  grib2 file from the download_files which should have been 
                  downloaded using GetCapaData function

    :param epsgID: espg ID chosen by user as an unsigned integer, chosen to be 
     EPSG:4326 by default
    
    :return null:
    """
    #in name
    Download_Path = "download_files/" + fname
    print(Download_Path)
    #out name
    FoutName = fname.replace(".grib2", ".tif")
    PrjPath = "projected_files/" + FoutName
    print(PrjPath)
    #set source projection
    #this is hard coded as the dataset only comes in this projection
    src_srs = osr.SpatialReference()
    src_srs.ImportFromEPSG(3413)
    
    #set target projection
    tgt_srs = osr.SpatialReference()
    tgt_srs.ImportFromEPSG(epsgID)
    
    #open dataset and set projection
    ds = gdal.Open(Download_Path)
    ds.SetProjection(src_srs.ExportToWkt())
    
    gdal.Warp(destNameOrDestDS=PrjPath, 
                        srcDSOrSrcDSTab=ds,
                        dstSRS=(tgt_srs))


