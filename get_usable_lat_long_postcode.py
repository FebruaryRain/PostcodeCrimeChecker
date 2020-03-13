"""
Module to get the usable lat and long in a tuple for use in the geodist module as the centre point. 
To use, make a call to function:
    get_postcode_centre_lat_long(postcode)
... where postcode is a valid postcode, correctly formatted. 
"""


from read_files import open_a_file_and_retrieve_contents
from file_path_logic import get_postcode_data_filepath

def remove_superfluous_columns_postcodes(postcode_row):
    """
    Takes in a list of values, a row from the postcodes csv file.
    Returns only the last 2 elements, the lat and long (in that order) without any further operation.
    Does this by returning only the 2nd to last to the end data.
    If a type other than list is provided, returns TypeError.
    """
    if type(postcode_row) == list:
        return postcode_row[-2:]
    else:
        return TypeError

## TODO do we need to add validation for a postcode to be valid?
def get_user_specified_postcode_row(postcode):
    """
    Takes in a postcode as a string, correctly formatted is a must right now.
    Returns the row that postcode is on in the postcodes csv file.
    Does so by iterating through the rows and returning the one who has the specified postcode.
    As there is only one data source for the postcodes data, the data is called for in this module at # PostcodeDataCall,
    rather than looking for it to come in as an argument.
    """
    POST_CODE = 0
    file_data = open_a_file_and_retrieve_contents(get_postcode_data_filepath()) # PostcodeDataCall
    for row in file_data:
        if row[POST_CODE] == postcode:
            return row
    return

def convert_postcodes_lat_and_long_data_to_usable_tuple_of_floats(postcodes_lat_long):
    """
    Takes in a list of two values, Latitude and Longitude, in that order, as they appear in postcodes.csv.
    Returns the values as floats, in an immutable tuple as we don't want further mutation of them at this point.
    Does this by using the float() function and then returning a tuple of the two values.
    If a type other than list is provided, returns TypeError.
    """
    if type(postcodes_lat_long) == list:
        latitude = 0
        longitude = 1
        lat,long = float(postcodes_lat_long[latitude]), float(postcodes_lat_long[longitude])
        return (lat, long)
    else:
        return TypeError

def get_postcode_centre_lat_long(postcode):
    """
    Takes in a postcode as a string, correctly formatted is a must right now.
    Returns the centre Lat Long as a float tuple, ready for GeoDist to begin calculations.
    Works by calling the supporting functions:
        get_user_specified_postcode_row(postcode)
        remove_superfluous_columns_postcodes(postcode_row)
        convert_postcodes_lat_and_long_data_to_usable_tuple_of_floats(lat_long_strings)
    """
    postcode_row = get_user_specified_postcode_row(postcode)
    lat_long_strings = remove_superfluous_columns_postcodes(postcode_row)
    lat_long_data = convert_postcodes_lat_and_long_data_to_usable_tuple_of_floats(lat_long_strings)
    return lat_long_data

#####
## Tests
#####

def remove_superfluous_columns_postcodes_should_return_correct_output():
    all_col_list = ["0","1","2","3","4","5","6","7","8","9","10","11",]
    wanted_col_list = ["10","11"]
    assert(remove_superfluous_columns_postcodes(all_col_list) == wanted_col_list)
    return

def remove_superfluous_columns_postcodes_should_return_exception_if_non_list_provided():
    non_list1 = 5
    non_list2 = "string"
    non_list3 = (5,5)
    assert(remove_superfluous_columns_postcodes(non_list1) == TypeError)
    assert(remove_superfluous_columns_postcodes(non_list2) == TypeError)
    assert(remove_superfluous_columns_postcodes(non_list3) == TypeError)
    return

def convert_postcodes_lat_and_long_data_to_usable_tuple_of_floats_should_return_correct_output():
    lat_long_list_strings = [["50.21565","5.01425"],["50.462646","-4.714629"],["50.457415","-4.467377"],["50.421859","-5.057535"],["50.740558","-3.988073"]]
    lat_long_list_floats_expected = [(50.21565,5.01425),(50.462646,-4.714629),(50.457415,-4.467377),(50.421859,-5.057535),(50.740558,-3.988073)]
    lat_long_list_floats_returns = []
    for value in lat_long_list_strings:
        lat_long_list_floats_returns.append(convert_postcodes_lat_and_long_data_to_usable_tuple_of_floats(value))
    assert(lat_long_list_floats_returns == lat_long_list_floats_expected)
    return

def convert_postcodes_lat_and_long_data_to_usable_tuple_of_floats_return_exception_if_non_list_provided():
    non_list1 = 5
    non_list2 = "string"
    non_list3 = (5,5)
    assert(convert_postcodes_lat_and_long_data_to_usable_tuple_of_floats(non_list1) == TypeError)
    assert(convert_postcodes_lat_and_long_data_to_usable_tuple_of_floats(non_list2) == TypeError)
    assert(convert_postcodes_lat_and_long_data_to_usable_tuple_of_floats(non_list3) == TypeError)
    return

def get_user_specified_postcode_row_should_return_correct_output():
    target_postcode = "DT1 1AA"
    expected_return = ["DT1 1AA","10","368730","90722","E92000001","E19000002","E18000010","E10000009","E07000052","E05010590","+50.71527036","-2.44427954"]
    assert(get_user_specified_postcode_row(target_postcode) == expected_return)
    return

def get_postcode_centre_lat_long_should_return_correct_output():
    target_postcode = "DT1 1AA"
    assert(get_postcode_centre_lat_long(target_postcode) == (50.71527036,-2.44427954))
    return


if __name__ == "__main__":
    remove_superfluous_columns_postcodes_should_return_correct_output()
    remove_superfluous_columns_postcodes_should_return_exception_if_non_list_provided()
    convert_postcodes_lat_and_long_data_to_usable_tuple_of_floats_should_return_correct_output()
    convert_postcodes_lat_and_long_data_to_usable_tuple_of_floats_return_exception_if_non_list_provided()
    get_postcode_centre_lat_long_should_return_correct_output()
    get_user_specified_postcode_row_should_return_correct_output()