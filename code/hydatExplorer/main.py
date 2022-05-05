# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 11:09:24 2022

@author: KEmmelkamp
"""

import sqlAccess as sa

def main():
    # server address, ideally this would be some address in the P-Drive
    database = "data/Hydat.sqlite3"
    
    # create a database connection
    conn = sa.create_connection(database)
    tableNames = sa.query_table_names(conn=conn)
    for name in tableNames:
        print(name[0])
        sa.query_tables(conn=conn, tName=name[0])
        sa.query_column_names(conn=conn, tName=name[0])

    #query_tables(conn=conn, tName = "CONCENTRATION_SYMBOLS")
    
        
    conn.close()
    
if __name__ == "__main__":
    main()

