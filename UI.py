import messages

def clear_screen():
    print("\n"*5+"******************************************")

def load_menu():
    
    pause = input()
    clear_screen()
    print(messages.opening_message)
    print(messages.menu_selection)
    print("\n")
    print(arguments_dict)
    print("\n")

    while True:
            try:
                menuChoice = int(input())
                break
            except ValueError:
                print(messages.invalid_value)

    if menuChoice == 1:
        select_postcode(arguments_dict['postcode'])
    elif menuChoice == 2:
        select_radius(arguments_dict['radius'])
    elif menuChoice == 3:
        sort_data(arguments_dict['data_sort'])
    elif menuChoice == 4:
        set_file_name(arguments_dict['file_name'])
    elif menuChoice == 5:
        confirm_data(correct_data, **arguments_dict)
    elif menuChoice == 6:
        restart_program(**arguments_dict)
    elif menuChoice == 7:
        print(messages.help_message)
        load_menu()
    elif menuChoice == 8:
        quit()
    else:
        print(messages.invalid_value)
        load_menu()
#1#
def select_postcode(postcode):
    print("Please enter the 'EX' postcode to be searched without spaces.")       

    while True:
        usr_postcode = str(input()).upper() 
        if usr_postcode[0] == 'E' and usr_postcode[1] == 'X':
            if len(usr_postcode) == 7 and usr_postcode.isalnum():
                print("Postcode set as: " + usr_postcode )
                arguments_dict['postcode'] = usr_postcode
    
            elif len(usr_postcode) == 6:
                usr_postcode = usr_postcode.split()
                usr_postcode = ''.join(usr_postcode)
                print("Postcode set as: " + usr_postcode)
                arguments_dict['postcode'] = usr_postcode
            else:
                print(messages.invalid_value)
        else:
            print("Please enter an 'EX' postcode.")

    load_menu()
    
#2#
def select_radius(radius):
    print("Which radius(km) should be searched? 1,2 or 5")
    check = False
    while check == False:
        while True:
            try:
                usr_radius = int(input())
                break
            except ValueError:
                print(messages.invalid_value)
            
        if usr_radius == 1:
            check = True
        elif usr_radius == 2:
            check = True
        elif usr_radius == 5:
            check = True
        else:
            check = False
            print(messages.invalid_value)
            
        if check == True:
            arguments_dict['radius'] = usr_radius
            print("\n" + "Using radius: " + str(usr_radius) + "km")
        
        
    load_menu()

#3#
def sort_data(data_sort):

    print("How would you like to sort the data?")
    print("1. Distance")
    print("2. Date")
    print("3. Crime Category")
    check = False
    sortmode = ''
    while check == False:
        while True:
                try:
                    sort_code = int(input())
                    break
                
                except ValueError:
                    print(messages.invalid_value)

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
            print(messages.invalid_value)
                
        if check == True:
            arguments_dict['data_sort'] = sort_code
            print("\n" + "Sorting data by " + sortmode + ".")
    load_menu()

#4#
def set_file_name(file_name):
    print("Enter Desired File Name:")
    usr_filename = str(input())
    print("\n" + "File name saved as: " + usr_filename + ".csv")
    arguments_dict['file_name'] = usr_filename
    load_menu()

#5#
def confirm_data(correct_data, postcode, radius, data_sort, file_name):

    if data_sort == 1:
        sortmode = 'Distance'
    elif data_sort == 2:
        sortmode = 'Date'
    elif data_sort == 3:
        sortmode = 'Crime Category'
    else:
        sortmode = 'ERROR'

    if radius == 0:
        print('Please set the radius to be searched.')
        load_menu()
    elif sortmode == 'ERROR':
        print('Please select a method of sorting the data.')
        load_menu()
        

    print("Confirm the following values (Y/N) \n")
    print("Postcode: " + postcode)
    print("Radius: " + str(radius) + "km")
    print("Sorting by: " + sortmode)
    print("File Name: " + file_name + ".csv")

    while True:
        confirm = str(input()).upper()


        if confirm == "Y":
            print("\n" + "Values have been confirmed.")

            correct_data = True
            break
        
        elif confirm == "N":
            print("\n" + "Please re-enter correct information.")

            correct_data = False
            break
        
        else:
            print("Invalid Value, Please Enter 'Y' or 'N'.")
              
    load_menu()
    

#6#
def restart_program(postcode, radius, data_sort, file_name):

    arguments_dict['postcode'] = ''
    arguments_dict['radius'] = 0
    arguments_dict['data_sort'] = 0
    arguments_dict['file_name'] = ''
    print("\n" + "Program has been restarted and all values wiped.")
    
    load_menu()


###START OF PROGRAM###


usr_postcode = "test"
usr_radius = 0
sort_code = 0
usr_filename = "testname"
correct_data = False

arguments_dict = {'postcode': usr_postcode,
                'radius': usr_radius,
                'data_sort': sort_code,
                'file_name': usr_filename}
    
load_menu()


###TESTS###

def restart_program_should_reset_values_in_arguments_dict():

    #Arrange
    expected_return = {'postcode': '', 'radius': 0, 'data_sort': 0, 'file_name': ''}
    
    #Act
    restart_program()
    actual_return = arguments_dict

    #Assert
    assert(expected_return == actual_return)
    return

if __name__ == "__main__":
    restart_program_should_reset_values_in_arguments_dict()
    
                                

