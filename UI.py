"""
This module is to act as the User Interface (UI) for the program. 
To begin, create a function call to "load_menu()". 
The program will then run from there, and the generate_report module and function are called within confirm_data() 
to create the final report. 
"""

from extract_valid_postcodes import get_postcode_list
import generate_report
import messages


#####
## Global Variables Initialisation
#####

postcode_list = get_postcode_list()

default_postcode_value = ""
default_radius_value = 0
default_data_sort_value = 0
default_filename_value = ""

bcorrect_data = False
arguments_dict = {'postcode': default_postcode_value,
                'radius': default_radius_value,
                'data_sort': default_data_sort_value,
                'file_name': default_filename_value}


def clear_screen():
    """Returns new lines seperated with a line of '*'"""
    print("\n"*5+"******************************************")
    return

def load_menu():
    """Takes in all functions, Returns user input options for running all functions"""

    messages.start_message()
    pause = input()
    clear_screen()
    messages.opening_message()
    messages.menu_selection()
    print("") # To get a single line separation
    messages.inform_current_values_below()
    print(arguments_dict)
    print("")

    while True:
            try:
                menuChoice = int(input())
                break
            except ValueError:
                messages.invalid_value()

    if menuChoice == 1:
        select_postcode()
    elif menuChoice == 2:
        select_radius()
    elif menuChoice == 3:
        select_sort_data()
    elif menuChoice == 4:
        select_file_name()
    elif menuChoice == 5:
        confirm_data(bcorrect_data)
    elif menuChoice == 6:
        restart_program()
    elif menuChoice == 7:
        messages.help_message()
        load_menu()
    elif menuChoice == 8:
        messages.inform_program_exiting()
        quit()
    else:
        messages.invalid_value()
        load_menu()

#1#
def select_postcode():
    """Takes in user inputted postcode, stores this value in the program"""

    messages.request_user_EX_postcode() 
    while True:
        usr_postcode = str(input()).upper() 
        try:
            if usr_postcode == "6":
                restart_program()
            elif usr_postcode == "7":
                messages.help_message()
            elif usr_postcode == "8":
                messages.inform_program_exiting()
                quit()

            if usr_postcode[0] == 'E' and usr_postcode[1] == 'X':
                if len(usr_postcode) == 7 and usr_postcode.isalnum():
                    if check_postcode_in_list(usr_postcode):
                        messages.inform_postcode_value(usr_postcode)
                        arguments_dict['postcode'] = usr_postcode
                        break
                    else:
                        messages.error_postcode_not_in_list_of_existing()
                        messages.instruction_postcodes()
                elif len(usr_postcode) == 6:
                    first_three = usr_postcode[:3] 
                    back_three = usr_postcode[3:]
                    usr_postcode = first_three + " " + back_three
                    if check_postcode_in_list(usr_postcode):
                        messages.inform_postcode_value(usr_postcode)
                        arguments_dict['postcode'] = usr_postcode
                        break
                    else:
                        messages.error_postcode_not_in_list_of_existing()
                        messages.instruction_postcodes()
                else:
                    messages.invalid_value()
            else:
                messages.request_user_EX_postcode()
        except IndexError:
            if usr_postcode == "":
                messages.invalid_value()
                messages.instruction_no_empty_strings()
                messages.instruction_postcodes()
        except:
            messages.invalid_value()
            messages.instruction_postcodes()
    load_menu()

def check_postcode_in_list(postcode):
    """
    Takes one argument, postcode, once formatted as it is expected to be (as in the postcodes.csv file's postcodes).
    Checks that the postcode supplied is in the list of the postcodes derived from the extract_valid_postcodes module.
    Returns True if the postcode is present, false if not. 
    """
    if postcode in postcode_list:
        return True
    else:
        return False

#2#
def select_radius():
    """Takes in a user specified radius, returns confirmation that this value has been stored."""

    messages.request_user_search_radius()
    check = False
    while check == False:
        while True:
            try:
                usr_radius = int(input())
                break
            except ValueError:
                messages.invalid_value()
            
        if usr_radius == 1:
            check = True
        elif usr_radius == 2:
            check = True
        elif usr_radius == 5:
            check = True
        elif usr_radius == 6:
            restart_program()
        elif usr_radius == 7:
            messages.help_message()
            messages.request_user_search_radius()
        elif usr_radius == 8:
            messages.inform_program_exiting()
            quit()
        else:
            check = False
            messages.invalid_value()
            
        if check == True:
            arguments_dict['radius'] = usr_radius
            print("\n")
            messages.inform_radius_value(usr_radius)
    load_menu()

#3#
def select_sort_data():
    """Takes in user selection of sort mode to specifiy how to sort data."""

    messages.request_user_sort_preference()
    check = False
    sortmode = ''
    while check == False:
        while True:
                try:
                    sort_code = int(input())
                    break
                
                except ValueError:
                    messages.invalid_value()

        if sort_code == 1:
            sortmode = 'Distance'
            check = True
        elif sort_code == 2:
            sortmode = 'Date'
            check = True
        elif sort_code == 3:
            sortmode = 'Crime Category'
            check = True
        elif sort_code == 4:
            sortmode = 'No Sort'
            check = True
        elif sort_code == 6:
            restart_program()
        elif sort_code == 7:
            messages.help_message()
            messages.request_user_sort_preference()
        elif sort_code == 8:
            messages.inform_program_exiting()
            quit()
        else:
            check = False
            messages.invalid_value()
                
        if check == True:
            arguments_dict['data_sort'] = sort_code
            messages.inform_sort_value(sortmode)
    load_menu()

#4#
def select_file_name():
    """Takes in file_name variable and user submitted name, to return an overrided file_name."""

    while True:   
        messages.instruction_file_names()
        messages.request_user_filename()
        usr_filename = str(input())
        if usr_filename == "":
            messages.invalid_value()
        elif usr_filename == "6":
            restart_program()
        elif usr_filename == "7":
            messages.help_message()
            messages.instruction_file_names()
        elif usr_filename == "8":
            messages.inform_program_exiting()
            quit()
        elif check_input_is_alnum(usr_filename):
            arguments_dict['file_name'] = usr_filename
            messages.inform_filename_save(usr_filename)
            break
        else:
            messages.invalid_value()
    load_menu()

def check_input_is_alnum(input):
    """
    Performs a check that the user's inputted string's charaters are alphanumeric only.
    Takes a string argument.
    Returns True if all characters are alphanumeric ([a-Z], [0-9]) and False if any are not.
    Does this by iterating through each inputted character and calls .isalnum() from standard string library.
    """
    for char in input:
        if char.isalnum():
            pass
        else:
            return False
    return True

#5#
def confirm_data(bcorrect_data):
    """Takes in postcode, radius, data_sort and file_name variables.
    Returns a confirmation that these variables are correct.
    Completes this by asking the user to confirm."""

    postcode = arguments_dict['postcode']
    radius = arguments_dict['radius']
    data_sort = arguments_dict['data_sort']
    file_name = arguments_dict['file_name']

    if postcode == "":
        messages.inform_value_not_set()
        messages.remind_user_to_set_value("Postcode")
        messages.inform_returning_to_menu()
        load_menu()

    if data_sort == 1:
        sortmode = 'Distance'
    elif data_sort == 2:
        sortmode = 'Date'
    elif data_sort == 3:
        sortmode = 'Crime Category'
    elif data_sort == 4:
        sortmode = 'No Sort'
    else:
        sortmode = 'ERROR'

    if radius == 0:
        messages.inform_value_not_set()
        messages.remind_user_to_set_value("Radius")
        messages.inform_returning_to_menu()
        load_menu()
    elif sortmode == 'ERROR':
        messages.inform_value_not_set()
        messages.remind_user_to_set_value("Data Sort")
        messages.inform_returning_to_menu()
        load_menu()

    messages.request_confirmation()
    messages.inform_postcode_value(postcode)
    messages.inform_radius_value(radius)
    messages.inform_sort_value(sortmode)
    messages.inform_filename_value(file_name)

    while True:
        confirm = str(input()).upper()
        if confirm == "6":
            restart_program()
        elif confirm == "7":
            messages.help_message()
            messages.request_confirmation()
            messages.inform_postcode_value(postcode)
            messages.inform_radius_value(radius)
            messages.inform_sort_value(sortmode)
            messages.inform_filename_value(file_name)
        elif confirm == "8":
            messages.inform_program_exiting()
            quit()

        if confirm == "Y":
            messages.confirm_values_set()
            generate_report.generate_report(arguments_dict)
            bcorrect_data = True
            break
        elif confirm == "N":
            messages.inform_returning_to_menu()
            bcorrect_data = False
            break
        
        else:
            messages.inform_need_Y_or_N()
    load_menu()

#6#
def restart_program():
    """
    Takes no arguments, returns nothing.
    Calls reset_argument_dictionary and sends the user back to the main menu.
    """
    reset_argument_dictionary()
    load_menu()

def reset_argument_dictionary():
    """Takes the variables postcode, radius, data_sort and file_name.
    Returns them as defaulted values.
    Informed the user that the arguments are cleared and that the program is restarting."""

    arguments_dict['postcode'] = default_postcode_value
    arguments_dict['radius'] = default_radius_value
    arguments_dict['data_sort'] = default_data_sort_value
    arguments_dict['file_name'] = default_filename_value
    messages.inform_program_restarted_arg_dict_cleared()
    return

###TESTS###

def reset_argument_dictionary_should_reset_values_in_arguments_dict():

    #Arrange
    expected_return = {'postcode': '', 'radius': 0, 'data_sort': 0, 'file_name': ''}
    
    #Act
    reset_argument_dictionary()
    actual_return = arguments_dict

    #Assert
    assert(expected_return == actual_return)
    return

def check_input_is_alnum_should_return_true_for_alnum_input():
    # Arrange
    inputs_list = ["12345","abcde","1A2DE","a1c45","AbCdE","aBcDe"]
    expected_return = True
    # Act
    actual_return = False # default that the test fails
    for element in inputs_list:
        actual_return = check_input_is_alnum(element)
        if not actual_return:
            break
    # Assert
    return

def check_input_is_alnum_should_return_false_for_invalid_input():
    # Arrange
    inputs_list = ["\\2345","_bcde","1A2D>","?1c45",":@~;']","!£$%^&*()"]
    expected_return = False
    # Act
    actual_return = True # default that the test fails
    for element in inputs_list:
        actual_return = check_input_is_alnum(element)
        if actual_return:
            break
    # Assert
    return

def check_postcode_in_list_should_return_true_for_postcode_in_list():
    # Arrange
    expected = True
    input_values = ["EX1 1AN", "EX348HU", "EX4 2WX", "EX230LP", "EX7 0QJ"]
    # Act
    for postcode in input_values:
        # Assert
        assert(expected == check_postcode_in_list(postcode))
    return

def check_postcode_in_list_should_return_false_for_postcode_not_in_list():
    # Arrange
    expected = False
    input_values = ["EX230PL", "EX7 0QK", "EX4 0ZK", "EX110FA", "EX5 0LT"]
    # Act
    for postcode in input_values:
        # Assert
        assert(expected == check_postcode_in_list(postcode))
    return

if __name__ == "__main__":
    reset_argument_dictionary_should_reset_values_in_arguments_dict()
    check_input_is_alnum_should_return_true_for_alnum_input()
    check_input_is_alnum_should_return_false_for_invalid_input()
    check_postcode_in_list_should_return_true_for_postcode_in_list()
    check_postcode_in_list_should_return_false_for_postcode_not_in_list()
