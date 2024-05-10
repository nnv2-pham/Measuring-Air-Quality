# Import the CSV library.
import csv
# Import the sys module.
import sys
# Import the itertools module.
import itertools
# Import the datetime library.
from datetime import datetime
# Initialize a sql_100.
sql_100 = "THE FIRST 100 INSERTS TO `readings` TABLE VALUES \n"
# Intialize the row_count to 1.
row_count = 1
# Open the "clean.csv" file in the read mode.
with open("clean.csv", "r") as csvfile:
     # Create a CSV Dict reader object.
    reader = csv.DictReader(csvfile, delimiter = ";")
    # Create the "for" loop iterate every row through reader.
    for row in itertools.islice(reader, 100):
        # Format the "Date Time".
        dt = datetime.fromisoformat(row["Date Time"][:-6])
        dt.strftime("%Y-%m-%d %H:%M:%S")
        dt = row["Date Time"]
        # Format the "DateStart".
        ds = datetime.fromisoformat(row["DateStart"][:-6])
        ds.strftime("%Y:%m:%d %H:%M:%S")
        ds = row["DateStart"]
        # Format the "DateEnd".
        if row["DateEnd"]:
            de = datetime.fromisoformat(row["DateEnd"][:-6])
            de.strftime("%Y:%m:%d %H:%M:%S")
            de = row["DateEnd"]
        # Delete the "Location" column from reading "clean.csv" because the `reading` table do not have "Location" column.
        del row["Location"]
        # Delete the "geo_point_2d" column from reading "clean.csv" because the `reading` table do not have "geo_point_2d" column.
        del row["geo_point_2d"]
        # Create a for loop to iterate each "value" in a row and change it to a string.
        readings = ["'" + str(value) + "'" for value in row.values()]
        # Join all the readings statement into one string.
        sql = ".".join(readings)
        # Replace some positions which it do not have values to NULL in sql file.
        sql = sql.replace("''", "NULL")
        # Replace the "True" in string to 'True' in boolean in the sql file.
        sql = sql.replace("'True'", "True")
        # Replace the "Flase" in string to 'False' in boolean int in the sql file.
        sql = sql.replace("'False'", "False")
        # Create the sql_100.
        sql_100 = sql_100 + "(" + str(row_count) + "," + sql + ")," + "\n"
        # The row_count is incremented by 1.
        row_count += 1
# Open the "insert-100.sql" file in write mode.
with open ("insert-100.sql", "w") as csvfile:
    # Write the "insert-100.sql" file.
    csvfile.write(sql_100 + "\n")


