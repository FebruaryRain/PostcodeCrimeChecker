import messages
import generate_report

#####
## Global Variables Initialisation
#####
# default_postcode_value = ""
# default_radius_value = 0
# default_data_sort_value = 0
# default_filename_value = ""
### For Testing
default_postcode_value = "EX230LP"
default_radius_value = int("5")
default_data_sort_value = int("1")
default_filename_value = "spooge"
###

correct_data = False
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
    print("\n")
    print(arguments_dict)
    print("\n")

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
        confirm_data(correct_data, **arguments_dict)

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
        if usr_postcode[0] == 'E' and usr_postcode[1] == 'X':
            if len(usr_postcode) == 7 and usr_postcode.isalnum():
                messages.inform_postcode_value(usr_postcode)
                arguments_dict['postcode'] = usr_postcode
                break
    
            elif len(usr_postcode) == 6:
                usr_postcode = usr_postcode.split()
                usr_postcode = ''.join(usr_postcode)
                messages.inform_postcode_value(usr_postcode)
                arguments_dict['postcode'] = usr_postcode
                break
            else:
                messages.invalid_value()
        else:
            messages.request_user_EX_postcode()

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
        else:
            check = False
            messages.invalid_value()
                
        if check == True:
            arguments_dict['data_sort'] = sort_code
            messages.inform_sort_value(sortmode)
    load_menu()

#4#
def select_file_name():
    messages.instruction_file_names()
    while True:
        messages.request_user_filename()
        usr_filename = str(input())
        if check_input_is_alnum(usr_filename):
            arguments_dict['file_name'] = usr_filename
            messages.inform_filename_save(usr_filename)
            break
        else:
            messages.invalid_value()
            messages.instruction_file_names()
    load_menu()

def check_input_is_alnum(input):
    for char in input:
        if char.isalnum():
            pass
        else:
            return False
    return True

#5#
def confirm_data(correct_data, postcode, radius, data_sort, file_name):

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

        if confirm == "Y":
            messages.confirm_values_set()
            generate_report.generate_report(arguments_dict)
            correct_data = True
            break

        elif confirm == "N":
            messages.inform_returning_to_menu()
            correct_data = False
            break
        
        else:
            messages.inform_need_Y_or_N()
    load_menu()
    

#6#
def restart_program():
    reset_argument_dictionary()
    load_menu()

def reset_argument_dictionary():
    arguments_dict['postcode'] = default_postcode_value
    arguments_dict['radius'] = default_radius_value
    arguments_dict['data_sort'] = default_data_sort_value
    arguments_dict['file_name'] = default_filename_value
    messages.inform_program_restarted_arg_dict_cleared()


###START OF PROGRAM###
    
#load_menu()


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

#if __name__ == "__main__":
    #reset_argument_dictionary_should_reset_values_in_arguments_dict()


