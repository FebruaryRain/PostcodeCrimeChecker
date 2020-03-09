import csv
from pathlib import Path

def open_a_file_and_retrieve_contents(filepath):
    """
    This function takes in a file path to a .csv file as an argument.
    The function will return a list, which contains lists derived from the values found in each row 
    of the given .csv file.

    The order of the elements reflects the following headers:

    FOR POSTCODES CSV FILE:
    Postcode
    Positional Quality Indicator
    Eastings
    Northings
    Country Code
    NHS regional health authority code
    NHS health authority code
    Administrative county code
    Administrative district code
    Administrative ward code
    ETRS89GD-Lat
    ETRS89GD-Long

    FOR CRIME DATA FILES:
    Crime ID
    Month
    Reported by
    Falls within
    Longitude
    Latitude
    Location
    LSOA code
    LSOA name
    Crime type
    Last outcome category
    Context
    """
    with open(filepath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        all_records = []
        for row in csv_reader:
            all_records.append(row)
        csv_file.close
    return all_records

# First thoughts, we want the following headings from postcodes: 
# Postcode
# ETRS89GD-Lat
# ETRS89GD-Long
# The rest appear to be cruft we don't directly need.

# We can then pass this off to the geodist module in order to then get the starting distance. 

# We then likely will be interested in the below headers from the crime statistics:
    #Crime ID
    #Longitude
    #Latitude
    #Location
    #Crime type
    #Last outcome category

#####
## Tests
#####

def open_a_file_and_retrieve_contents_should_return_representative_sample_ok_when_given_valid_input():
    file = Path("Devon_postcodes/postcodes.csv")
    file2 = Path("Devon_and_Cornwall_crime_data_2019/2019-01/2019-01-devon-and-cornwall-street.csv")

    output1 = open_a_file_and_retrieve_contents(file)
    output2 = open_a_file_and_retrieve_contents(file2)

    test_sample1 = [['Postcode', 'Positional Quality Indicator', 'Eastings', 'Northings', 'Country Code', 'NHS regional health authority code', 'NHS health authority code', 'Administrative county code', 'Administrative district code', 'Administrative ward code', 'ETRS89GD-Lat', 'ETRS89GD-Long'], ['DT1 1AA', '10', '368730', '90722', 'E92000001', 'E19000002', 'E18000010', 'E10000009', 'E07000052', 'E05010590', '+50.71527036', '-2.44427954'], ['DT1 1AB', '10', '369874', '90687', 'E92000001', 'E19000002', 'E18000010', 'E10000009', 'E07000052', 'E05010589', '+50.71501621', '-2.42807300'], ['DT1 1AD', '10', '369245', '90319', 'E92000001', 'E19000002', 'E18000010', 'E10000009', 'E07000052', 'E05010590', '+50.71167397', '-2.43695132'], ['DT1 1AE', '10', '369076', '90500', 'E92000001', 'E19000002', 'E18000010', 'E10000009', 'E07000052', 'E05010590', '+50.71329261', '-2.43936007']]
    test_sample2 = [['Crime ID', 'Month', 'Reported by', 'Falls within', 'Longitude', 'Latitude', 'Location', 'LSOA code', 'LSOA name', 'Crime type', 'Last outcome category', 'Context'], ['', '2019-01', 'Devon & Cornwall Police', 'Devon & Cornwall Police', '-4.544128', '50.829232', 'On or near Lansdown Close', 'E01018936', 'Cornwall 001A', 'Anti-social behaviour', '', ''], ['', '2019-01', 'Devon & Cornwall Police', 'Devon & Cornwall Police', '-4.544117', '50.827973', 'On or near The Strand', 'E01018936', 'Cornwall 001A', 'Anti-social behaviour', '', ''], ['', '2019-01', 'Devon & Cornwall Police', 'Devon & Cornwall Police', '-4.544556', '50.830572', 'On or near Belle Vue Avenue', 'E01018936', 'Cornwall 001A', 'Anti-social behaviour', '', ''], ['', '2019-01', 'Devon & Cornwall Police', 'Devon & Cornwall Police', '-4.544556', '50.830572', 'On or near Belle Vue Avenue', 'E01018936', 'Cornwall 001A', 'Anti-social behaviour', '', '']]

    assert(test_sample1 == output1[0:5])
    assert(test_sample2 == output2[0:5])


if __name__ == "__main__":
    open_a_file_and_retrieve_contents_should_return_representative_sample_ok_when_given_valid_input()

