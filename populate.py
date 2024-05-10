# Import the Pandas library.
import pandas as pd
# Import the Pymysql library.
import pymysql
# Import the SQLAlchemy library.
import sqlalchemy
# Import the sys module.
import sys
# Import the CSV library.
import csv
# Import create_engine from sqlalchemy library.
from sqlalchemy import create_engine

try:
    # Set the user and password.
    user = 'root'
    password = ''
    host = '127.0.0.1'
    port = 3306
    # Create the connection to the database.
    conn = create_engine('mysql+pymysql://' + user + ':' + password + '@' + host, echo = False)
   
    # Check to see if database 'pollution-db' exists in the system - ignore DROP TABLE if it does not.
    conn.execute ("DROP DATABASE IF EXISTS `pollution-db`")
    # Create the database 'pollution-db'.
    conn.execute("CREATE DATABASE `pollution-db`")
    # Get a database 'pollution-db' handle.
    conn.execute("USE `pollution-db`")

    # Read the 'schema.csv' file as a list one at a time to create 'schema_dataframe'.
    schema_dataframe = pd.read_csv("schema.csv", delimiter = ';', low_memory = False)
    # Reindex schema_dataframe to begin at 1.
    schema_dataframe.index += 1
    # Insert data from reading the 'schema.csv' file into the database.
    schema_dataframe.to_sql(
        "schema",
        con = conn,
        if_exists = "replace",
        index = True,
        index_label = "m_id",
    )
    # Add the relationship.
    conn.execute("ALTER TABLE `schema` ADD PRIMARY KEY (`m_id`);")

    # Read the 'clean.csv' file as a list one at a time to create 'stations_dataframe'.
    stations_dataframe = pd.read_csv("clean.csv", delimiter = ';', usecols=["SiteID","Location","geo_point_2d"])
    stations_dataframe = stations_dataframe.drop_duplicates("SiteID", keep = "last")
    # Reindex dataframe to begin at 1.
    stations_dataframe.index += 1
    # Insert data from reading the 'clean.csv' file into the database.
    stations_dataframe.to_sql(
        "stations",
        con = conn,
        if_exists = "replace",
        index = False,
    )
    # Add the relationship.
    conn.execute("ALTER TABLE `stations` ADD PRIMARY KEY (`SiteID`);")

    # Read the 'clean.csv' file as a list one at a time to create 'readings_dataframe'.
    readings_dataframe = pd.read_csv("clean.csv", delimiter = ';', usecols=["Date Time", "NOx", "NO2", "NO", "SiteID", "PM10", "NVPM10", "VPM10", "NVPM2.5", "PM2.5", "VPM2.5", "CO", "O3", "SO2", "Temperature", "RH", "Air Pressure", "DateStart", "DateEnd", "Current", "Instrument Type"], low_memory=False)
    # Reindex dataframe to begin at 1.
    readings_dataframe.index += 1
    # Insert data from reading the 'clean.csv' file into the database.
    readings_dataframe.to_sql(
        "readings",
        con = conn,
        if_exists = "replace",
        index = True,
        index_label = "r_id",
        chunksize = 10000
    )
    # Add the relationship.
    conn.execute("ALTER TABLE `readings` ADD PRIMARY KEY (`r_id`);")

# catch and report on any error.
# exit with 1 (non-error scripts automatically exit with 0).
except BaseException as err:
    print (f"An error occured: {err}")
    sys.exit(1)
