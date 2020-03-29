"""
This module is to act as the file reading section. 
Call open_file_retrieve_contents_bar_headers(filepath) for all rows except for the headers row. 
Call open_file_retrieve_contents(filepath) for all rows including headers.
The "filepath" argument should be a call to one of the functions in file_path_logic module, 
as these return the Path (pathlib) version of a filepath string. 
"""

import csv

def open_file_retrieve_contents_bar_headers(filepath):
    """
    This function takes in a filepath to a .csv file as an argument, in order to pass to another function "open_file_retrieve_contents"
    """
    return remove_top_headers_row(open_file_retrieve_contents(filepath))

def open_file_retrieve_contents(filepath):
    """
    This function takes in a Path(filepath) to a .csv file as an argument.
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
    all_records = []
    with open(filepath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if len(row):
                all_records.append(row)
                
            else:
                pass
        csv_file.close
    return all_records

def remove_top_headers_row(records_list):
    return records_list[1:]

#####
## Tests
#####

def open_file_retrieve_contents_should_return_representative_sample_ok():
    # Arrange
    file = "Devon_postcodes/postcodes.csv"
    file2 ="Devon_and_Cornwall_crime_data_2019/2019-01/2019-01-devon-and-cornwall-street.csv"
    expected_return1 = [['Postcode', 'Positional Quality Indicator', 'Eastings', 'Northings', 'Country Code', 'NHS regional health authority code', 'NHS health authority code', 'Administrative county code', 'Administrative district code', 'Administrative ward code', 'ETRS89GD-Lat', 'ETRS89GD-Long'],['DT1 1AA', '10', '368730', '90722', 'E92000001', 'E19000002', 'E18000010', 'E10000009', 'E07000052', 'E05010590', '+50.71527036', '-2.44427954'], ['DT1 1AB', '10', '369874', '90687', 'E92000001', 'E19000002', 'E18000010', 'E10000009', 'E07000052', 'E05010589', '+50.71501621', '-2.42807300'], ['DT1 1AD', '10', '369245', '90319', 'E92000001', 'E19000002', 'E18000010', 'E10000009', 'E07000052', 'E05010590', '+50.71167397', '-2.43695132'], ['DT1 1AE', '10', '369076', '90500', 'E92000001', 'E19000002', 'E18000010', 'E10000009', 'E07000052', 'E05010590', '+50.71329261', '-2.43936007']]
    expected_return2 = [['Crime ID', 'Month', 'Reported by', 'Falls within', 'Longitude', 'Latitude', 'Location', 'LSOA code', 'LSOA name', 'Crime type', 'Last outcome category', 'Context'],['', '2019-01', 'Devon & Cornwall Police', 'Devon & Cornwall Police', '-4.544128', '50.829232', 'On or near Lansdown Close', 'E01018936', 'Cornwall 001A', 'Anti-social behaviour', '', ''], ['', '2019-01', 'Devon & Cornwall Police', 'Devon & Cornwall Police', '-4.544117', '50.827973', 'On or near The Strand', 'E01018936', 'Cornwall 001A', 'Anti-social behaviour', '', ''], ['', '2019-01', 'Devon & Cornwall Police', 'Devon & Cornwall Police', '-4.544556', '50.830572', 'On or near Belle Vue Avenue', 'E01018936', 'Cornwall 001A', 'Anti-social behaviour', '', ''], ['', '2019-01', 'Devon & Cornwall Police', 'Devon & Cornwall Police', '-4.544556', '50.830572', 'On or near Belle Vue Avenue', 'E01018936', 'Cornwall 001A', 'Anti-social behaviour', '', '']]
    # Act
    output1 = open_file_retrieve_contents(file)
    output2 = open_file_retrieve_contents(file2)
    # Assert
    assert(expected_return1 == output1[0:5])
    assert(expected_return2 == output2[0:5])
    return 

def remove_top_headers_row_should_omit_first_row():
    # Arrange
    sample_input = [["01"],["02"],["03"],["04"]]
    expected_return = [["02"],["03"],["04"]]
    # Act 
    returned_list = remove_top_headers_row(sample_input)
    # Assert
    assert(expected_return == returned_list)

def open_file_retrieve_contents_bar_headers_should_return_representative_sample_without_headers_ok():
    # Arrange
    file = "Devon_postcodes/postcodes.csv"
    file2 ="Devon_and_Cornwall_crime_data_2019/2019-01/2019-01-devon-and-cornwall-street.csv"
    expected_return1 = [['DT1 1AA', '10', '368730', '90722', 'E92000001', 'E19000002', 'E18000010', 'E10000009', 'E07000052', 'E05010590', '+50.71527036', '-2.44427954'], ['DT1 1AB', '10', '369874', '90687', 'E92000001', 'E19000002', 'E18000010', 'E10000009', 'E07000052', 'E05010589', '+50.71501621', '-2.42807300'], ['DT1 1AD', '10', '369245', '90319', 'E92000001', 'E19000002', 'E18000010', 'E10000009', 'E07000052', 'E05010590', '+50.71167397', '-2.43695132'], ['DT1 1AE', '10', '369076', '90500', 'E92000001', 'E19000002', 'E18000010', 'E10000009', 'E07000052', 'E05010590', '+50.71329261', '-2.43936007']]
    expected_return2 = [['', '2019-01', 'Devon & Cornwall Police', 'Devon & Cornwall Police', '-4.544128', '50.829232', 'On or near Lansdown Close', 'E01018936', 'Cornwall 001A', 'Anti-social behaviour', '', ''], ['', '2019-01', 'Devon & Cornwall Police', 'Devon & Cornwall Police', '-4.544117', '50.827973', 'On or near The Strand', 'E01018936', 'Cornwall 001A', 'Anti-social behaviour', '', ''], ['', '2019-01', 'Devon & Cornwall Police', 'Devon & Cornwall Police', '-4.544556', '50.830572', 'On or near Belle Vue Avenue', 'E01018936', 'Cornwall 001A', 'Anti-social behaviour', '', ''], ['', '2019-01', 'Devon & Cornwall Police', 'Devon & Cornwall Police', '-4.544556', '50.830572', 'On or near Belle Vue Avenue', 'E01018936', 'Cornwall 001A', 'Anti-social behaviour', '', '']]
    # Act
    output1 = open_file_retrieve_contents_bar_headers(file)
    output2 = open_file_retrieve_contents_bar_headers(file2)
    # Assert
    assert(expected_return1 == output1[0:4])
    assert(expected_return2 == output2[0:4])
    return 

def remove_top_headers_row_should_omit_first_row():
    # Arrange
    sample_input = [["01"],["02"],["03"],["04"]]
    expected_return = [["02"],["03"],["04"]]
    # Act 
    returned_list = remove_top_headers_row(sample_input)
    # Assert
    assert(expected_return == returned_list)

if __name__ == "__main__":
    open_file_retrieve_contents_should_return_representative_sample_ok()
    open_file_retrieve_contents_bar_headers_should_return_representative_sample_without_headers_ok()
    remove_top_headers_row_should_omit_first_row()
