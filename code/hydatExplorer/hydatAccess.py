# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 15:21:04 2022

@author: KEmmelkamp
"""


import pandas as pd
import geopandas as gpd
import numpy as np
from shapely.geometry import Point

def get_station_data(conn, stationNo=None,stationName=None,provTerr=None):
    """ Query the station information table from the HYDAT sqlite3 database,
        open as pandas dataframe, there are several parameters which the 
        table can be filtered as, will filter data first by stationNo, then
        by name, then by province, will only filter by dataset in the order
        given
    :param conn: the SQLite3 connection object (will throw error if this is
                 not included)
    :param stationNo: the station number, by default if no value is given
                      this script will return the entire table
    :param stationName: the station name as a string, by default this is none,
                        exact name as listed by WSC, will return no value if
                        string is incorrect
    :param provTerr: the initials for a province or territory as specified by
                     WSC
    :return df: returns a pandas dataframe, will be filtered if one of the
                three options has been selected
    """
    df = pd.read_sql_query("SELECT * FROM STATIONS", 
                           con = conn)
    
    if stationNo != None:
        is_station = df["STATION_NUMBER"]==stationNo
        filtered_df = df[is_station]
    elif stationName != None:
        is_station = df["STATION_NAME"]==stationName
        filtered_df = df[is_station]
    elif provTerr != None:
        is_station = df["PROV_TERR_STATE_LOC"]==provTerr
        filtered_df = df[is_station]
    else:
        filtered_df = df
    
    return filtered_df


def gauge_search(conn, lat, lon, distance):
    """ Search for a gauge based on a reference location (lat,lon) and the 
        distance from the reference location
        This script is very much a work in progress and does not work properly
    :param conn: the SQLite3 connection object (will throw error if this is
                 is not included)
    :param lat: (float) latitude in decimal degrees of the reference location
    :param lon: (float) longitude in decimal degrees of the reference location
    :param distance: (float) distance in kilometers which user would like to 
                     search from the reference location
    :return GaugeList: a list of gauges within the requested radius
    """
    #take lat and lon inputs and create site location from this

    geoSiteLocation = gpd.GeoSeries(data=[Point(lon,lat)],
                                    crs="EPSG:4326"
                                    ).to_crs("EPSG:2957")
    siteBuffer = geoSiteLocation.buffer(distance=distance*1000)  

    #utm13SiteLocation = geoSiteLocation = geoSiteLocation.to_crs("EPSG:2957")
    #get hydat dataframe (hdf stands for hydat dataframe)
    hdf = pd.read_sql_query("SELECT * FROM STATIONS", con = conn)
    #create geopandas dataframe object from hydat dataframe
    geohdf = gpd.GeoDataFrame(hdf, 
                              geometry=gpd.points_from_xy(
                                  hdf.LONGITUDE, 
                                  hdf.LATITUDE),
                              crs="EPSG:4326"
                              ).to_crs("EPSG:2957")
    
    #siteBufferExtended = gpd.GeoSeries(np.repeat(siteBuffer.geometry, 
    #                                             geohdf.shape[0]))
    #gaugeCheck = siteBuffer.within(geohdf.geometry[100])


    geohdf_2 = geohdf.assign(newVar=geohdf.geometry.within(siteBuffer))
    return  geohdf, geohdf_2

def extract_gauge_info(conn, 
                       stationNo=None, 
                       stationName=None, 
                       provTerr=None):
    """Query the station hydat database to return all relevant data which 
       would include all the relevant gauge data from STATION's table in the
       hydat database with the STN_DATA_RANGE table.
    :param conn: the SQLite3 connection object (will throw error if this is
                 not included)
    :param stationNo: the station number, by default if no value is given
                      this script will return the entire table
    :param stationName: the station name as a string, by default this is none,
                        exact name as listed by WSC, will return no value if
                        string is incorrect
    :param provTerr: the initials for a province or territory as specified by
                     WSC
    :return full_record: the gauge information which includes the record length
    
    
    """
    df_stations = pd.read_sql_query("SELECT * FROM STATIONS",
                           con = conn)
    df_record = pd.read_sql_query("SELECT * FROM STN_DATA_RANGE",
                                  con = conn)
    
    # manipulate table to include only the values we care about
    df_record = df_record.groupby(
        df_record['STATION_NUMBER']).aggregate(
            {'YEAR_FROM' : 'min', 'YEAR_TO' : 'max', 'RECORD_LENGTH' : 'max'})
    df_station_data = pd.merge(left = df_stations,
                               right = df_record,
                               left_on='STATION_NUMBER',
                               right_on='STATION_NUMBER')
    
    
    
    return df_stations, df_record, df_station_data











