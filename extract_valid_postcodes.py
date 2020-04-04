"""
This module will extract a list of all postcodes in the postcodes.csv file.
This is then used in UI.py to ensure that the user only gives a postcode in the file.
If this check isn't performed, the run will fail and the program with it.
"""

from file_reader import open_file_retrieve_contents_bar_headers
from file_path_logic import get_postcode_data_filepath

def extract_all_postcodes():
    """
    Takes no arguments.
    Returns a list with all of the postcodes in the postcodes.csv file.
    Extracts the postcodes, which are always found in [0] of the records and appends to a list, which is returned.
    """
    all_records = get_all_postcode_records()
    all_postcodes = []
    POSTCODE = 0
    for record in all_records:
        all_postcodes.append(record[POSTCODE])
    return all_postcodes

def get_all_postcode_records():
    """
    Takes no arguments.
    Returns all of the records in postcodes.csv
    Uses file_reader and file_path_logic to get the information needed from postcodes.csv
    """
    return open_file_retrieve_contents_bar_headers(get_postcode_data_filepath())

def get_postcode_list():
    """
    Getter method to get the postcode_list, the list of all postcodes in postcodes.csv
    """
    return postcode_list

postcode_list = extract_all_postcodes()

#####
# Tests
#####

def extract_all_postcodes_should_return_representative_sample_OK():
    # Arrange
    expected_return = ["DT1 1AA", "DT1 1AB", "DT1 1AD", "DT1 1AE", "DT1 1AF"]
    # Act
    actual_return = extract_all_postcodes()[:5]
    # Assert
    assert(expected_return == actual_return)
    return

## In the below tests, we use the length of the return as a shorthand to ensure that we are 
## reading the whole postcodes file correctly. 

def get_all_postcode_records_should_return_correct_length_list():
    # Arrange
    expected_length = 68638
    # Act
    actual_length = len(get_all_postcode_records())
    # Assert
    assert(expected_length == actual_length)
    return

def extract_all_postcodes_should_return_correct_length_list():
    # Arrange
    expected_length = 68638
    # Act
    actual_length = len(extract_all_postcodes())
    # Assert
    assert(expected_length == actual_length)
    return

if __name__ == "__main__":
    extract_all_postcodes_should_return_representative_sample_OK()
    get_all_postcode_records_should_return_correct_length_list()
    extract_all_postcodes_should_return_correct_length_list()
