# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 11:09:24 2022

@author: KEmmelkamp
"""

import sqlAccess as sa
import hydatAccess as ha

def main():
    # server address, ideally this would be some address in the P-Drive
    database = "data/Hydat.sqlite3"
    
    # create a database connection
    conn = sa.create_connection(database)
    #sa.query_table_names(conn=conn)
    ds,dr,dsd = ha.extract_gauge_info(conn=conn)

    
    conn.close()
    return ds,dr,dsd
    
if __name__ == "__main__":
   ds,dr,dsd = main()

