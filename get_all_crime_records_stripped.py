"""
This module allows the user to get all crime records, stripped to only those rows we know we want in the final report.
Use by importing and calling only for the "get_all_crime_records_stripped()" function. 
"""
from file_reader import open_a_file_and_retrieve_contents
from file_path_logic import get_crime_data_filepaths


def get_all_crime_records_stripped():
    """
    Takes in the single list of all crime records.
    To get all crime records, enter the argument "all_crime_records()", importing this function from this module to do so. 
    Returns these records without the 12th, 9th, 8th, 4th, 3rd elements as these were decided to be superfluous.
    These are removed, starting at the back so that removing an element doesn't change other element's positions.
    Remember that the elements are 0 indexed, so it is element-1 that we remove.
    """
    all_crime_records = create_unified_list_of_crime_records(read_all_records())
    for record in all_crime_records:
        record.pop(11)
        record.pop(8)
        record.pop(7)
        record.pop(3)
        record.pop(2)
    return all_crime_records


def create_unified_list_of_crime_records(records_by_month):
    """
    Takes in the list of each months' records.
    Returns these as one list, no separate list per month.
    Does this by iterating through the records_by_month, then iterating through each of their records and adding these to a new list.
    """
    all_records = []
    for file in records_by_month:
        for row in file:
            all_records.append(row)
    return all_records


def read_all_records():
    """
    Takes no arguments as it is to go through all files in the known file structure.
    Returns a list with each months' records a seperate list. 
    Does this by reading, with the read_files module, each of the files and extracting the csv data.
    Therefore, returns a list with 12 elements (one for each month of the year).
    """
    all_month_records = []
    for month in range(1,13):
        file_path = get_crime_data_filepaths(month)
        all_month_records.append(open_a_file_and_retrieve_contents(file_path))
    return all_month_records


#####
# Tests
#####


def read_all_records_should_return_list_of_twelve_records_lists():
    # Arrange
    expected_length_return = 12
    # Act
    returned_length= len(read_all_records())
    # Assert
    assert(expected_length_return == returned_length)


def create_unified_list_of_records_should_return_len_of_136145():
    # Quick note, the number 136145 was determined by writing a short program to count the number of records,
    # followed by a check of what the average per file would be and a look at how many roughly there are in there 
    # as a quick check. Seems to be fine for now. 
    # As the list length is just too long to copy and check against, we assess the length of the list instead.

    # Arrange
    expected_length = 136145
    records_by_month = read_all_records()
    # Act
    returned_length = len(create_unified_list_of_crime_records(records_by_month))
    # Assert
    assert(expected_length == returned_length)


def get_all_crime_records_stripped_should_return_records_without_unwanted_rows():
    # sample of a row we act on: ['', '2019-01', 'Devon & Cornwall Police', 'Devon & Cornwall Police', '-4.544128', '50.829232', 'On or near Lansdown Close', 'E01018936', 'Cornwall 001A', 'Anti-social behaviour', '', '']
    # A quick reminder on the columns and which ones we want
    # 1     Crime ID,               WANT
    # 2     Month,                  WANT
    # 3     Reported by,
    # 4     Falls within,
    # 5     Longitude,              WANT
    # 6     Latitude,               WANT
    # 7     Location,               WANT
    # 8     LSOA code,
    # 9     LSOA name,
    # 10    Crime type,             WANT
    # 11    Last outcome category,  WANT
    # 12    Context
    # So Remove 12,9,8,4,3 (elements 11,8,7,3,2 to be done in that order!)
    # Arrange
    expected_return = ['', '2019-01', '-4.544128', '50.829232', 'On or near Lansdown Close', 'Anti-social behaviour', '',]
    actual_return = []
    # Act
    actual_return = get_all_crime_records_stripped()[0]
    # Assert
    assert(actual_return == expected_return)


if __name__ == "__main__":
    
    read_all_records_should_return_list_of_twelve_records_lists()
    create_unified_list_of_records_should_return_len_of_136145()
    get_all_crime_records_stripped_should_return_records_without_unwanted_rows()