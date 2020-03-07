from pathlib import Path
from read_files import open_a_file_and_retrieve_contents 

## This module will create the file paths for the various file paths we need.

def postcode_data_filepath():
    """
    This function takes no arguments and will only return "/Devon_postcodes" as 
    intepreted by a Path object in order that this can be called to get the 
    postcode data when this is called.
    """
    return Path("Devon_postcodes/postcodes.csv")

def crime_data_filepaths(iterable_int):
    """
    The function take an integer as an argument. 
    From this, it will construct the correct file path in order to obtain the crime 
    data .csv file path, for use in the readfiles.py module.
    """
    str_int = str(iterable_int)
    top_folder_path = "Devon_and_Cornwall_crime_data_2019"
    sub_folder_path = ""
    file_path = ""
    if iterable_int <10:
        sub_folder_path = "/2019-0" + str_int
        file_path = "/2019-0" + str_int + "-devon-and-cornwall-street.csv"
    else:
        sub_folder_path = "/2019-" + str_int
        file_path = "/2019-" + str_int + "-devon-and-cornwall-street.csv"
    return Path(top_folder_path + sub_folder_path + file_path)

#####
## Tests
#####

def postcode_data_filepath_should_return_correct_filepath():
    assert(postcode_data_filepath() == Path("Devon_postcodes/postcodes.csv"))
    return

def crime_data_filepaths_should_return_correct_file_path_when_supplied_1():
    list_of_crime_data_file_paths_returns = ""
    list_of_crime_data_file_paths_expected = Path("Devon_and_Cornwall_crime_data_2019\\2019-01\\2019-01-devon-and-cornwall-street.csv")
    list_of_crime_data_file_paths_returns = crime_data_filepaths(1)
    assert(list_of_crime_data_file_paths_expected == list_of_crime_data_file_paths_returns)
    return

def crime_data_filepaths_should_return_correct_sub_10_file_path_when_supplied():
    list_of_crime_data_file_paths_returns = []
    list_of_crime_data_file_paths_expected = [
        Path("Devon_and_Cornwall_crime_data_2019/2019-01/2019-01-devon-and-cornwall-street.csv"),
        Path("Devon_and_Cornwall_crime_data_2019/2019-02/2019-02-devon-and-cornwall-street.csv"),
        Path("Devon_and_Cornwall_crime_data_2019/2019-03/2019-03-devon-and-cornwall-street.csv"),
        Path("Devon_and_Cornwall_crime_data_2019/2019-04/2019-04-devon-and-cornwall-street.csv"),
        Path("Devon_and_Cornwall_crime_data_2019/2019-05/2019-05-devon-and-cornwall-street.csv"),
        Path("Devon_and_Cornwall_crime_data_2019/2019-06/2019-06-devon-and-cornwall-street.csv"),
        Path("Devon_and_Cornwall_crime_data_2019/2019-07/2019-07-devon-and-cornwall-street.csv"),
        Path("Devon_and_Cornwall_crime_data_2019/2019-08/2019-08-devon-and-cornwall-street.csv"),
        Path("Devon_and_Cornwall_crime_data_2019/2019-09/2019-09-devon-and-cornwall-street.csv")]
    for i in range(1,10):
        list_of_crime_data_file_paths_returns.append(crime_data_filepaths(i))
    assert(list_of_crime_data_file_paths_expected == list_of_crime_data_file_paths_returns)
    return


def crime_data_filepaths_should_return_correct_greater_than_10_file_path_when_supplied():
    list_of_crime_data_file_paths_returns = []
    list_of_crime_data_file_paths_expected = [
        Path("Devon_and_Cornwall_crime_data_2019/2019-10/2019-10-devon-and-cornwall-street.csv"),
        Path("Devon_and_Cornwall_crime_data_2019/2019-11/2019-11-devon-and-cornwall-street.csv"),
        Path("Devon_and_Cornwall_crime_data_2019/2019-12/2019-12-devon-and-cornwall-street.csv")]
    for i in range(10, 13):
        list_of_crime_data_file_paths_returns.append(crime_data_filepaths(i))
    assert(list_of_crime_data_file_paths_expected == list_of_crime_data_file_paths_returns)

if __name__ == "__main__":
    postcode_data_filepath_should_return_correct_filepath()
    crime_data_filepaths_should_return_correct_sub_10_file_path_when_supplied()
    crime_data_filepaths_should_return_correct_greater_than_10_file_path_when_supplied()
    crime_data_filepaths_should_return_correct_file_path_when_supplied_1()

    # Manual testing items, leave commented unless testing.

    #print(open_a_file_and_retrieve_contents(postcode_data_filepath()))
    #print(open_a_file_and_retrieve_contents(crime_data_filepaths(1)))