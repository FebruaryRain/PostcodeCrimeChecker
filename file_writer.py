"""
This module serves to write the final reports to the correct file location. 
The report content is written to the Reports folder. 
The file_name is always a string. 
The correct filepath is then found using a relative filepath in the file_path_logic 
module. 
"""

import csv
from file_path_logic import report_file_path
from file_reader import open_file_retrieve_contents
import messages

def write_report_to_file(report_content, file_name):
    """
    Takes in 2 arguments. report_content refers to the path of the report your trying to read and file_name is the string file name given to the 
    report by assigning it to file_name.
    This function does not return anything.
    This function generates a report by calling the file_writer function after inserts the relevant column headers
    """
    if type(report_content) == list:
        column_headers = ["Crime ID", "Month","Longitude","Latitude","Location","Crime type", "Last outcome category", "Distance (Km)"]
        report_content.insert(0, column_headers)
        file_writer(report_content, file_name)
        return
    else:
        messages.error_could_not_write_to_file()
        return

def file_writer(report_content, file_name):
    """
    Takes in 2 arguments. report_content refers to the path of the report you're trying to read. 
    file_name is the name of the file you're writing to.
    It reads a .csv file and then writes said .csv file under a new file name into the reports folder named as "file_name".
    """
    try:
        with open(report_file_path(file_name), 'w', newline='') as file_written:
            file_writer = csv.writer(file_written)
            for row in report_content:
                file_writer.writerow(row)
            file_written.close
    except PermissionError: 
        messages.error_please_close_file()
    return

# tests

def write_report_to_file_should_create_the_write_to_file():
    # arrange
    test_content = [["Crime ID", "Month","Longitude","Latitude","Location","Crime type", "Last outcome category", "Distance (Km)"]]
    test_file_name = "test2"
    expected_file_content = [["Crime ID", "Month","Longitude","Latitude","Location","Crime type", "Last outcome category", "Distance (Km)"],["Crime ID", "Month","Longitude","Latitude","Location","Crime type", "Last outcome category", "Distance (Km)"]]
    # act
    write_report_to_file(test_content, test_file_name)
    actual_file_content = open_file_retrieve_contents(report_file_path('test2'))
    # assert
    assert(expected_file_content == actual_file_content)
    return

def file_writer_should_create_written_csv_in_report_folder():
    # arrange
    test_file_name = "test3"
    expected_file = [["Crime ID", "Month","Longitude","Latitude","Location","Crime type", "Last outcome category", "Distance (Km)"]]
    test_data = [["Crime ID", "Month","Longitude","Latitude","Location","Crime type", "Last outcome category", "Distance (Km)"]]
    # act
    file_writer(test_data, test_file_name)
    actual_file = open_file_retrieve_contents(report_file_path(test_file_name))
    # assert
    assert(expected_file == actual_file)
    return

if __name__ == "__main__":
    write_report_to_file_should_create_the_write_to_file()
    file_writer_should_create_written_csv_in_report_folder()
