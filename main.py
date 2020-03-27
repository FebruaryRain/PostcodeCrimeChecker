import UI

def run():
    """
    This is the function which will call the UI, will then also call the rest of the program in generate_report().
    Takes no arguments. Returns nothing.
    """
    UI.load_menu()
    return
    # Run James' UI
        # Which passes all arguments in a DICTIONARY
        ## We will have a "get_arguments_dictionary()" function in the UI for all also to grab this info.
        # arguments_dict = {"postcode":"usr_postcode","radius": int_value, "data_sort": "sort_code", "file_name": "usr_filename"}
        # Passes this dict to everyone
        # NEEDS to do input validation to ensure that nothing is passed on which is incorrect and will break a later func.


run()

