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
# informs
#####

def inform_current_values_below():
    print("Current values are:")
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
