"""
This module serves to combine all of the logic to create the final report in one place.
The module has one function, generate_report(arguments_dictionary), and is called from
within UI.py (in confirm_data()). 
"""

import data_sorter
import file_path_logic
import file_reader
import file_writer
import get_all_crime_records_stripped
import get_usable_lat_long_postcode
import messages
from pathlib import Path
import UI

def generate_report(arguments_dictionary):
    """
    This is the section which will generate the report. It will take in the arguments dictionary, full of user specified arguments.
    It is called by confirm_data() in UI.py.
    It takes the arguments_dictionary from the UI as its argument, then passes it to the rest of the program. 
    """
    latitude_pos = 0
    longitude_pos = 1
    try:
        postcode_centre = get_usable_lat_long_postcode.get_postcode_centre_lat_long(arguments_dictionary['postcode'])
    except:
        messages.error_inform_user_postcode_not_in_list()
        return
    all_crime_records = get_all_crime_records_stripped.get_all_crime_records_stripped()
    sorted_data = data_sorter.data_sorter(postcode_centre[latitude_pos], postcode_centre[longitude_pos], arguments_dictionary['radius'], all_crime_records, arguments_dictionary['data_sort'])
    file_writer.write_report_to_file(sorted_data, arguments_dictionary['file_name'])
    return

## Tests

def generate_report_should_generate_valid_report():
    # Arrange
    test_arguments_dictionary = {'postcode': "EX230LP",
                                'radius': 1,
                                'data_sort': 1,
                                'file_name': "generate_report_test"}
    expected_report = file_reader.open_file_retrieve_contents(Path("Reports/Testing/Test11.csv"))
    # Act
    generate_report(test_arguments_dictionary)
    actual_report = file_reader.open_file_retrieve_contents(file_path_logic.report_file_path(test_arguments_dictionary['file_name']))
    # Assert
    assert(expected_report == actual_report)

if __name__ == "__main__":
    generate_report_should_generate_valid_report()
    