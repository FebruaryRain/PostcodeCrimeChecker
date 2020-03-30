"""
This module is to act as the User Interface (UI) for the program. 
To begin, create a function call to "load_menu()". 
The program will then run from there, and the generate_report module and function are called within confirm_data() 
to create the final report. 
"""

import messages
import generate_report

#####
## Global Variables Initialisation
#####

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
    print("\n"*5+"******************************************")
    return

def load_menu():
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
                    messages.inform_postcode_value(usr_postcode)
                    arguments_dict['postcode'] = usr_postcode
                    break
                elif len(usr_postcode) == 6:
                    first_three = usr_postcode[:3] 
                    back_three = usr_postcode[3:]
                    usr_postcode = first_three + " " + back_three
                    messages.inform_postcode_value(usr_postcode)
                    arguments_dict['postcode'] = usr_postcode
                    break
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
    
#2#
def select_radius():
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
    for char in input:
        if char.isalnum():
            pass
        else:
            return False
    return True

#5#
def confirm_data(bcorrect_data):
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
    reset_argument_dictionary()
    messages.inform_program_restarted_arg_dict_cleared()
    load_menu()

def reset_argument_dictionary():
    arguments_dict['postcode'] = default_postcode_value
    arguments_dict['radius'] = default_radius_value
    arguments_dict['data_sort'] = default_data_sort_value
    arguments_dict['file_name'] = default_filename_value
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

if __name__ == "__main__":
    reset_argument_dictionary_should_reset_values_in_arguments_dict()


