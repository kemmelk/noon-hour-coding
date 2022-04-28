# -*- coding: utf-8 -*-
"""
main function to run all capa files from
Created on Tue Apr 26 15:12:44 2022

@author: KEmmelkamp
"""
import os
import accessCaPa as acp

def main():
    StartDate = "2011-04-12 07"
    EndDate = "2011-04-13 11"
    
    acp.DownloadCapaData(start_date=StartDate, end_date=EndDate)
    
    download_files = os.listdir("download_files/")
    
    for file in download_files:
        if file.endswith(".grib2"):
            acp.ReprojectCapa(file)
    
if __name__ == "__main__":
    main()