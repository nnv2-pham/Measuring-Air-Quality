# Import the CSV library.
import csv
# Create an empty list of data.
data = []
# Intialize the count_line to 0.
count_line = 0
# Open the "air-quality-data-continuous.csv" file in read mode.
with open("air-quality-data-continuous.csv", "r") as file:
    # Read all lines in the "air-quality-data-continuous.csv" file.
    data = file.readlines()
# Print the total lines in the "air-quality-data-continuous.csv" file.
print("The 'air-quality-data-continuous' CSV file has " + str(len(data)) + " lines") 
# Open the "crop.csv" file in write mode.
with open("crop.csv", "w") as file:
    # Skip the header row in the "air-quality-data-continuous.csv" file.
    file.write(data.pop(0))
    # Create a for loop to iterate each row through data.
    for i, row in enumerate (data):
        # Check if the row of the first column has value or an empty.
        if (row[0] == ';'):
            # Print all lines has an empty Date Time.
            print("Line " + str(i) + " has an empty Date Time")
            # Continue to the next iteration.
            continue
         # Check and filter out some rows where the values in "Date Time" column before 2010.
        if (int(row[0:4]) >= 2010):
            # Write to file.
            file.write(row)
            # The count_line is incremented by 1.
            count_line += 1
# Print the total lines in the "crop.csv".
print ("The 'crop.csv' file has " + str(count_line + 1) + " lines")
