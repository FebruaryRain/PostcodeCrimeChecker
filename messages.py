"""
This module is to act as a central location for all messages to be displayed to the user.
This is to aid in ensuring consistent formatting and grammar across all messages. 
The messages are separated into sections to aid in navigation:
 - other - general
 - errors
 - informs
 - instructions
 - requests
"""

import default_values_config

#####
# Global Variables, used in inform_logic functions
#####

default_postcode_value = default_values_config.cfg_default_postcode_value 
default_radius_value = default_values_config.cfg_default_radius_value
default_data_sort_value = default_values_config.cfg_default_data_sort_value
default_filename_value = default_values_config.cfg_default_filename_value 

#####
# other - general
#####

def confirm_values_set():
    print("\n" + "Values have been confirmed.")
    return

def help_message(): 
    print("""Help: 
1. Postcode Selection: Enter the postcode you wish to search, it must be entered without spaces and should start with 'EX'.
2. Radius: Select the radius to be searched from 1,2 and 5km. 
3. Sort the data: Select a type of sorting to use on the data, choices include distance, date and crime category. 
4. Select File Name: Enter a file name to be used to save your data. 
5. Confirm: Performs a check to confirm with the user if the data inputted is correct before proceeding. 
6. Restart: Restarts the program removing any stored data. 
7. Help: Provides a list of all menu choices and what they do. 
8. Quit: Exits the program.

Note, if at any time you input "6", "7", or "8", these will be treated as Restart, Help, Quit commands - respectively.
    """)
    return

def invalid_value():
    print("Invalid Value, please try again")
    return

def menu_selection():
    print("""1. Postcode Selection 
2. Radius 
3. Data Sort Mode 
4. Input name for save file 
5. Confirm 
6. Restart 
7. Help 
8. Quit
    """)
    return

def opening_message():
    print("""Welcome to the Postcode Crime Checker 
Please select from the following options:
    """)
    return

def remind_user_to_set_value(value_to_set):
    print("Please ensure you have set the following value:", value_to_set)
    return

def start_message():
    print("Press Enter to continue")
    return

#####
# errors
#####

def error_could_not_write_to_file():
    print("""Error, could not write to the file, the data return in the search was not of the correct data type. 
Please ensure that all future inputs are correct, if the problem persists please contact Appledore Technical Support.
    """)
    return

def error_inform_user_postcode_not_in_list():
    print("Error, please check that the centre postcode provided is valid.")
    return

def error_please_close_file():
    print("Error, please ensure that you do not have a file of the same name provided open.")
    return

def error_postcode_not_in_list_of_existing():
    print("Error, please ensure that the postcode you enter exists, as the one provided does not match any in the records.")
    return

#####
# inform_values_logic
#####

def postcode_inform_logic(postcode):
    if postcode == default_postcode_value:
        return "Not yet set"
    else: 
        return str(postcode)

def radius_inform_logic(radius):
    if radius == default_radius_value:
        return "Not yet set"
    else:
        radius_inform = str(radius) + "Km"
        return radius_inform

def data_sort_inform_logic(data_sort):
    if data_sort == 1:
        return "Distance"
    elif data_sort == 2:
        return "Date"
    elif data_sort == 3:
        return "Crime Category"
    elif data_sort == 4:
        return "No Sort"
    else:
        return "Not yet set"

def file_name_inform_logic(file_name):
    if file_name == default_filename_value:
        return "Not yet set"
    else: 
        return file_name

#####
# informs
#####

def inform_current_values_below(arg_dict):
    print("Current values are:")
    line = "Postcode: " + postcode_inform_logic(arg_dict["postcode"]) + "; Radius: " + radius_inform_logic(arg_dict["radius"]) + "; Data_sort: " + data_sort_inform_logic(arg_dict["data_sort"]) + "; Filename: " + file_name_inform_logic(arg_dict["file_name"])
    print(line)
    return

def inform_filename_save(usr_filename):
    print("\n" + "File name to be save in the Reports folder as:")
    inform_filename_value(usr_filename)
    return

def inform_filename_value(file_name):
    print("File Name set as: " + file_name + ".csv")
    return

def inform_need_Y_or_N():
    print("Invalid Value, Please Enter 'Y' or 'N'.")
    return

def inform_postcode_value(postcode):
    print("Postcode set as: " + postcode)
    return

def inform_program_exiting():
    print("Program terminating.")
    return

def inform_program_restarted_arg_dict_cleared():
    print("\n" + "Program has been restarted and all values wiped.")
    return

def inform_radius_value(radius):
    print("Radius set as: " + str(radius) + "km")
    return

def inform_returning_to_menu():
    print("\n" + "Returning to menu screen")
    return

def inform_sort_value(sortmode):
    print("Data Sort Mode set as: " + sortmode)
    return

def inform_value_not_set():
    print("An option not been set")
    return

#####
# instructions
#####

def instruction_file_names():
    print("File names must contain alphabetical or numerical characters only, with no spaces")
    return

def instruction_no_empty_strings():
    print("Please do not enter empty strings")
    return

def instruction_postcodes():
    print("""Postcodes must contain alphabetical and numerical characters only, with no spaces. 
Postcodes must be either 6 or 7 characters long.""")
    return

def instruction_user_sort_options():
    print("""1. Distance
2. Date
3. Crime Category
4. No Sort
    """)
    return

#####
# requests
#####

def request_confirmation():
    print("Confirm the following values (Y/N) \n")
    return

def request_user_EX_postcode():
    print("Please enter the 'EX' postcode to be searched without spaces.")
    return

def request_user_filename():
    print("Enter Desired File Name:")
    return

def request_user_search_radius():
    print("Which radius(km) should be searched? 1,2 or 5")

def request_user_sort_preference():
    print("How would you like to sort the data?")
    instruction_user_sort_options()
    return

#####
# Tests
#####

def postcode_inform_logic_should_return_not_yet_set_when_default_value():
    # Arrange
    input_var = default_postcode_value
    expected = "Not yet set"
    # Act
    actual = postcode_inform_logic(input_var)
    # Assert
    assert (expected == actual)
    return

def postcode_inform_logic_should_return_passed_var_string_when_passed():
    # Arrange
    input_var = "EX230LP"
    expected = "EX230LP"
    # Act
    actual = postcode_inform_logic(input_var)
    # Assert
    assert (expected == actual)
    return

def radius_inform_logic_should_return_not_yet_set_when_default_value():
    # Arrange
    input_var = default_radius_value
    expected = "Not yet set"
    # Act
    actual = radius_inform_logic(input_var)
    # Assert
    assert (expected == actual)
    return

def radius_inform_logic_should_return_passed_var_string_when_passed():
    # Arrange
    input_var = 2
    expected = "2Km"
    # Act
    actual = radius_inform_logic(input_var)
    # Assert
    assert (expected == actual)
    return

def data_sort_inform_logic_should_return_not_yet_set_when_default_value():
    # Arrange
    input_var = default_data_sort_value
    expected = "Not yet set"
    # Act
    actual = data_sort_inform_logic(input_var)
    # Assert
    assert (expected == actual)
    return

def data_sort_inform_logic_should_return_passed_var_string_when_passed_1():
    # Arrange
    input_var = 1
    expected = "Distance"
    # Act
    actual = data_sort_inform_logic(input_var)
    # Assert
    assert (expected == actual)
    return

def data_sort_inform_logic_should_return_passed_var_string_when_passed_2():
    # Arrange
    input_var = 2
    expected = "Date"
    # Act
    actual = data_sort_inform_logic(input_var)
    # Assert
    assert (expected == actual)
    return

def data_sort_inform_logic_should_return_passed_var_string_when_passed_3():
    # Arrange
    input_var = 3
    expected = "Crime Category"
    # Act
    actual = data_sort_inform_logic(input_var)
    # Assert
    assert (expected == actual)
    return

def data_sort_inform_logic_should_return_passed_var_string_when_passed_4():
    # Arrange
    input_var = 4
    expected = "No Sort"
    # Act
    actual = data_sort_inform_logic(input_var)
    # Assert
    assert (expected == actual)
    return

def file_name_inform_logic_should_return_passed_var_string_when_passed():
    # Arrange
    input_var = default_filename_value
    expected = "Not yet set"
    # Act
    actual = file_name_inform_logic(input_var)
    # Assert
    assert (expected == actual)
    return

def file_name_inform_logic_should_return_not_yet_set_when_default_value():
    # Arrange
    input_var = "curtain_twitcher"
    expected = "curtain_twitcher"
    # Act
    actual = file_name_inform_logic(input_var)
    # Assert
    assert (expected == actual)
    return

if __name__ == "__main__":
    postcode_inform_logic_should_return_not_yet_set_when_default_value()
    postcode_inform_logic_should_return_passed_var_string_when_passed()
    radius_inform_logic_should_return_not_yet_set_when_default_value()
    radius_inform_logic_should_return_passed_var_string_when_passed()
    data_sort_inform_logic_should_return_not_yet_set_when_default_value()
    data_sort_inform_logic_should_return_passed_var_string_when_passed_1()
    data_sort_inform_logic_should_return_passed_var_string_when_passed_2()
    data_sort_inform_logic_should_return_passed_var_string_when_passed_3()
    data_sort_inform_logic_should_return_passed_var_string_when_passed_4()
    file_name_inform_logic_should_return_passed_var_string_when_passed()
    file_name_inform_logic_should_return_not_yet_set_when_default_value()