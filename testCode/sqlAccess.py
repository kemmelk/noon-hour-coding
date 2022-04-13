# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 11:13:48 2022

@author: KEmmelkamp
"""

import sqlite3 

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection Successful")
    except sqlite3.OperationalError as e:
        print(e)
        
    return conn

def query_table_names(conn):
    """ Query an existing SQLite Database for the different table names
    :param conn: the Connection object
    :return: tableNames: a list of the available table names in the
    """
    cursor = conn.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tableNames = cursor.fetchall()
    
    cursor.close()
    
    return tableNames
    
def query_tables(conn, tName):
    """ Query a table using a specified name to print out 
        and return contents
    :param conn: the Connection Object
    :param tName: string value of Table name
    :return: table contents    
    """
    
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT * FROM {tName}")
    
    cursor.close()

def query_column_names(conn, tName):
    """ Query the column names for a given tablet 
        and return contents
    :param conn: the Connection Object
    :param tName: string value of Table name
    :return: table contents    
    """
    
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT * FROM {tName}")
    names = list(map(lambda x: x[0], cursor.description))
    print(names)
    
    cursor.close()
    
def query_column(conn, tName, cName):
    """ Query the column names for a given tablet 
        and return contents
    :param conn: the Connection Object
    :param tName: string value of Table name
    :param cName: string value of Column name
    :return: table contents    
    """
    
    
    
    
    
    
    
    