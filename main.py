def run():
    # Run James' UI
        # Which passes all arguments in a DICTIONARY
        # arguments_dict = {"postcode":"usr_postcode","radius": int_value, "data_sort": "sort_code", "file_name": "usr_filename"}
        # Passes this dict to everyone
        # NEEDS to do input validation to ensure that nothing is passed on which is incorrect and will break a later func.
    # Sam's postcode centrepoint:
        # takes in arguments_dict, uses "postcode"; returns the lat/long centrepoint
    # Sam's Crime Reader
        # Returns a master list of all records, stripped to only the relevant columns
    # Roxy's radius filter
        # Takes in arguments_dict, uses "radius"; takes in Sam's lat/long centrepoint; returns list of rows in radius
    # Roxy's optional sorter
        # Takes in arguments_dict, uses "sort_code"; returns lists sorted according to code
    # Samir's file saver
        # Takes in arguments_dict, uses "usr_filename", writes the file to the specified filename in a "reports" directory.
    
    # We then need to also print the final report

    # NOTES ON THIS APPROACH
    # This would mean that we put the "keep doing this loop" in this module, not in James' UI
    # 


    # QUESTIONS TO POSE TO THE MODULE LEAD:
    # Can we use James' approach
    # Do we only ask for a file name if the file is more than x lines long (spec suggests this to be the case)
        

if __name__ == "__main__":
    # James' UI's returns
    # Goes to Sam's file reader
    # Gives input to Roxy's data sorter and filterer
    # Gives data to Samir's file creator
