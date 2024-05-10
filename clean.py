# Import the CSV library.
import csv
# Create the stations dictionary.
stations = {
    "188": "AURN Bristol Centre",
    "203": "Brislington Depot",
    "206": "Rupert Street",
    "209": "IKEA M32",
    "213": "Old Market",
    "215": "Parson Street School",
    "228": "Temple Meads Station",
    "270": "Wells Road",
    "271": "Trailer Portway P&R",
    "375": "Newfoundland Road Police Station",
    "395": "Shiner's Garage",
    "452": "AURN St Pauls",
    "447": "Bath Road",
    "459": "Cheltenham Road \ Station Road",
    "463": "Fishponds Road",
    "481": "CREATE Centre Roof",
    "500": "Temple Way",
    "501": "Colston Avenue",
    "672": "Marlborough Street"
}
# Intialize the count_row to 1.
count_row = 1
# Intialize the count_mismatch to 0.
count_mismatch = 0
# Open and read the "crop.csv" file.
reader = csv.DictReader(open("crop.csv", "r"), delimiter=';')
# Open the "clean.csv" file in write mode.
with open("clean.csv", "w") as csv_file:
    # Create a CSV dict writer object.
    writer = csv.DictWriter(csv_file, delimiter = ';',  fieldnames = reader.fieldnames)
    # Write headers (field names).
    writer.writeheader()
    # Create a for loop to interate each row through reader.
    for row in reader:
        # Check if the value in both the "SiteID" column and the "Location" column do not match in the dictionary of stations.
        if(not(row['SiteID'], row['Location']) in stations.items()):
                # The count_mismatch is incremented by 1.
                count_mismatch += 1
                # Print all lines that mismatch between "SiteID" column and "Location" column. 
                print(f"Line {count_row}: Mismatch between SiteID {row['SiteID']} and Location {row['Location']}")
        # If the above condition is False.
        else:
            # The count_row is incremented by 1.
            count_row += 1
            # Write to file.
            writer.writerow(row)
# Print the total lines do not mismatch.
print("There are " + str(count_mismatch) + ' lines that mismatches and is deleted')
# Print the total lines in the "clean.csv".               
print("The 'crop.csv' file has " + str(count_row) + " lines")


