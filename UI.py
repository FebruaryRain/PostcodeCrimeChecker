def cls():
    print("\n" * 100)
## The \n * 100 is a bit much, can make do with more like 50 I think - have a play with it in a console and see the minimum 
## number of lines.
## Also, expand on the name; cls isn't especially expressive (though I did get it meant "clear last screen" after pondering it 
## for a while).
## On further reflection, we might even not clear the screen entirely, but rather do something like print("\n"*10+"***************************")
## to act as a discernable break between inputs and screen, thus error messages will be shown.


def load_menu():
    
    pause = input() # Why do we want a pause there? If there was a "Press any key to start" this would be better. There must be an instruction.
    cls()
    print("Welcome to the Postcode Crime Checker") ## See bottom of the page for notes on this.
    print("Please select from the following options:")
    print("1. Postcode Selection")
    print("2. Radius")
    print("3. Sort the data")
    print("4. Input name for save file")
    print("5. Confirm")
    print("6. Save Data")
    print("7. Restart")
    print("8. Quit")
    ## We want a help screen somewhere in here. We can issue instructions to the user, letting them know that they must select and then enter 
    ## values, and that this can be done in any order.
    print("\n")
    ## Have a line of "Current values:" in here.
    print(arguments_dict) # There is a prettier way to display this. I can discuss this with you later.
    print("\n")

    while True:
            try:
                menuChoice = int(input())
                break
            except ValueError:
                print("Invalid Value, please try again")

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
    #elif menuChoice == 6:
        #save_data(**arguments_dict)
    elif menuChoice == 7:
        restart_program(**arguments_dict)
    elif menuChoice == 8:
        quit()
    else:
        print("Invalid Input.")
        load_menu()
    return
#1#
def select_postcode(postcode):
    print("Postcode Selection")
    load_menu()
    #arguments_dict['postcode'] = usr_postcode

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
                print("Invalid Value, please try again")
            
        if usr_radius == 1:
            check = True
        elif usr_radius == 2:
            check = True
        elif usr_radius == 5:
            check = True
        else:
            check = False
            print("Invalid Value, please try again")
            
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
                    print("Invalid Value, please try again")

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
            print("Invalid Value, please try again")
                
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
#def save_data(postcode, radius, data_sort, file_name):

#7#
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


#### MESSAGES
## We can create a separate messages module (in due course) that will abstract all of that printing above. I think this will be 
## the most elegant way to do this, though let me know your thougts. 
## I've done an example here:

## In the messages.py:
## opening_message = "Welcome to the Postcode Crime Checker \n Please select from the following options:"
## menu_selection = "1. Postcode Selection \n2. Radius \n3. Sort the data \n4. Input name for save file \n5. Confirm \n6. Save Data \n7. Restart \n8. Quit"

## In the load_menu():
## print(opening_message) 
## print(menu_selection)

## We can then add other messages in the messages.py file as well. 

#### get_arguments_dictionary
## We need to be able to pass the arguments here off to the next person down the line. 
## I suggest creating a "get_arguments_dictionary" function which will return the arguments dictionary.
## That way we can all get the information at the start of our programs without any great hassle.

#### Postcode validation
## There is an issue on this. We need to ensure that the user enters a valid postcode.
## I'll discuss this with you in more detail later as there's a couple of ways we can do it.
## Either way, we want it to only accept EX postcodes.
## Also, postcode isn't saving properly every time, seems to change back to test a lot.

#### We need a way to move on to the rest of the program.
## Your module will go through to the next part of the program. 
## As such, we need a way to
## 1) Have the rest of the program execute (I suggest a call in the confirm section to the rest of the program, which will then conduct the work).
## 2) That approach ought to then allow us to restart the program - though we will need to be able to print that it worked OK,
## see my notes on cls() at the top for more.
