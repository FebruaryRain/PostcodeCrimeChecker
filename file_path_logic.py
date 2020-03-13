from pathlib import Path
from read_files import open_a_file_and_retrieve_contents 

## This module will create the file paths for the various file paths we need.

def get_postcode_data_filepath():
    """
    This function takes no arguments and will only return "/Devon_postcodes" as 
    intepreted by a Path object in order that this can be called to get the 
    postcode data when this is called.
    """
    return Path("Devon_postcodes/postcodes.csv")

def get_month_string(number):
    """
    Takes in an integer number indicating the month of the year.
    Returns the appropriate string for use in the file path.
    Assesses if the value is between 0 and 10 for "0number".
    Assesses if the value is 10-12 for "number".
    If value is not in 1-12 it returns a value error. 
    """
    if 0 < number < 10:
        return "0" + str(number)
    if 13 > number >= 10:
        return str(number)
    else: 
        return ValueError

def get_crime_data_filepaths(month):
    month_string = get_month_string(month)
    return "./Devon_and_Cornwall_crime_data_2019/2019-" + month_string + "/2019-" + month_string + "-devon-and-cornwall-street.csv"


#####
## Tests
#####

def get_postcode_data_filepath_should_return_correct_filepath():
    assert(get_postcode_data_filepath() == Path("Devon_postcodes/postcodes.csv"))
    return

def crime_data_filepaths_should_return_correct_file_path_when_supplied_1():
    list_of_crime_data_file_paths_returns = ""
    list_of_crime_data_file_paths_expected = Path("Devon_and_Cornwall_crime_data_2019\\2019-01\\2019-01-devon-and-cornwall-street.csv")
    list_of_crime_data_file_paths_returns = crime_data_filepaths(1)
    assert(list_of_crime_data_file_paths_expected == list_of_crime_data_file_paths_returns)
    return

def get_month_should_give_all_month_strings_correctly():
    # Arrange
    expected_months = ["01","02","03","04","05","06","07","08","09","10","11","12"]
    returned_months = []
    
    # Act
    for i in range(1,13):
        returned_months.append(get_month_string(i))

    # Assert
    assert(returned_months == expected_months)
    return

def get_month_should_return_value_error_for_wrong_values():
    # Arrange
    wrong_values = [0, -5, 13]
    # Act and Assert
    for value in wrong_values:
        assert(get_month_string(value) == ValueError)
    return
    

def get_crime_data_filepaths_should_give_correct_month_strings():
    expected_paths = [
        "./Devon_and_Cornwall_crime_data_2019/2019-01/2019-01-devon-and-cornwall-street.csv",
        "./Devon_and_Cornwall_crime_data_2019/2019-02/2019-02-devon-and-cornwall-street.csv",
        "./Devon_and_Cornwall_crime_data_2019/2019-03/2019-03-devon-and-cornwall-street.csv",
        "./Devon_and_Cornwall_crime_data_2019/2019-04/2019-04-devon-and-cornwall-street.csv",
        "./Devon_and_Cornwall_crime_data_2019/2019-05/2019-05-devon-and-cornwall-street.csv",
        "./Devon_and_Cornwall_crime_data_2019/2019-06/2019-06-devon-and-cornwall-street.csv",
        "./Devon_and_Cornwall_crime_data_2019/2019-07/2019-07-devon-and-cornwall-street.csv",
        "./Devon_and_Cornwall_crime_data_2019/2019-08/2019-08-devon-and-cornwall-street.csv",
        "./Devon_and_Cornwall_crime_data_2019/2019-09/2019-09-devon-and-cornwall-street.csv",
        "./Devon_and_Cornwall_crime_data_2019/2019-10/2019-10-devon-and-cornwall-street.csv",
        "./Devon_and_Cornwall_crime_data_2019/2019-11/2019-11-devon-and-cornwall-street.csv",
        "./Devon_and_Cornwall_crime_data_2019/2019-12/2019-12-devon-and-cornwall-street.csv"
    ]
    returned_paths = []
    
    #Act
    for i in range(1,13):
        returned_paths.append(get_crime_data_filepaths(i))
    
    #Assert
    assert(expected_paths == returned_paths)
    return

if __name__ == "__main__":
    get_postcode_data_filepath_should_return_correct_filepath()
    # crime_data_filepaths_should_return_correct_sub_10_file_path_when_supplied()
    # crime_data_filepaths_should_return_correct_greater_than_10_file_path_when_supplied()
    # crime_data_filepaths_should_return_correct_file_path_when_supplied_1()

    get_month_should_give_all_month_strings_correctly()
    get_month_should_return_value_error_for_wrong_values()
    get_crime_data_filepaths_should_give_correct_month_strings()

    # Manual testing items, leave commented unless testing.

    #print(open_a_file_and_retrieve_contents(get_postcode_data_filepath()))
    #print(open_a_file_and_retrieve_contents(crime_data_filepaths(1)))