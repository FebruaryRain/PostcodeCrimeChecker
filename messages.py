"""
This module is to act as a central location for all messages to be displayed to the user.
This is to aid in ensuring consistent formatting and grammar across all messages. 
"""

def start_message():
    print("Press Enter to continue")
    return

def opening_message():
    print("Welcome to the Postcode Crime Checker \nPlease select from the following options:")
    return

def menu_selection():
    print("1. Postcode Selection \n2. Radius \n3. Data Sort Mode \n4. Input name for save file \n5. Confirm \n6. Restart \n7. Help \n8. Quit")
    return

def invalid_value():
    print("Invalid Value, please try again")
    return

def help_message(): 
    print("""
    Help: \n
    1. Postcode Selection: Enter the postcode you wish to search, it must be entered without spaces and should start with 'EX'. \n
    2. Radius: Select the radius to be searched from 1,2 and 5km. \n
    3. Sort the data: Select a type of sorting to use on the data, choices include distance, date and crime category. \n
    4. Select File Name: Enter a file name to be used to save your data. \n
    5. Confirm: Performs a check to confirm with the user if the data inputted is correct before proceeding. \n
    6. Restart: Restarts the program removing any stored data. \n
    7. Help: Provides a list of all menu choices and what they do. \n
    8. Quit: Exits the program.
    
    Note, if at any time you input "6", "7", or "8", these will be treated as Restart, Help, Quit commands - respectively.
    """)
    return

def request_user_filename():
    print("Enter Desired File Name:")
    return

def request_user_EX_postcode():
    print("Please enter the 'EX' postcode to be searched without spaces.")
    return

def request_user_search_radius():
    print("Which radius(km) should be searched? 1,2 or 5")

def request_user_sort_preference():
    print("How would you like to sort the data?")
    user_sort_options()
    return

def user_sort_options():
    print("1. Distance")
    print("2. Date")
    print("3. Crime Category")
    print("3. No Sort")

def inform_filename_save(usr_filename):
    print("\n" + "File name to be save in the Reports folder as:")
    inform_filename_value(usr_filename)
    return

def inform_value_not_set():
    print("An option not been set")
    return

def request_confirmation():
    print("Confirm the following values (Y/N) \n")
    return

def inform_postcode_value(postcode):
    print("Postcode set as: " + postcode)
    return

def inform_radius_value(radius):
    print("Radius set as: " + str(radius) + "km")
    return

def inform_sort_value(sortmode):
    print("Data Sort Mode set as: " + sortmode)
    return

def inform_filename_value(file_name):
    print("File Name set as: " + file_name + ".csv")
    return

def remind_user_to_set_value(value_to_set):
    print("Please ensure you have set the following value:", value_to_set)
    return

def confirm_values_set():
    print("\n" + "Values have been confirmed.")
    return

def inform_returning_to_menu():
    print("\n" + "Returning to menu screen")
    return

def inform_need_Y_or_N():
    print("Invalid Value, Please Enter 'Y' or 'N'.")

def inform_program_restarted_arg_dict_cleared():
    print("\n" + "Program has been restarted and all values wiped.")
    return

def inform_program_exiting():
    print("Program terminating.")

def instruction_file_names():
    print("File names must contain alphabetical or numerical characters only, with no spaces")
    return

def error_please_close_file():
    print("Error, please ensure that you do not have a file of the same name provided open.")
    return

def error_could_not_write_to_file():
    print("""
    Error, could not write to the file, the data return in the search was not of the correct data type. \n
    Please ensure that all future inputs are correct, if the problem persists please contact Appledore Tech Support.
    """)

def current_values_below():
    print("Current values are:")
    return

def error_inform_user_postcode_not_in_list():
    print("An error occured, please check that the centre postcode provided is a valid one.")
    return