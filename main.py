"""
This is the main module, to be called in the running of the program.
Calling the program from this module ensures that tests are not run from the conditional 
if __name__ == "__main__" statement, found at the bottom of each module. 
"""

import UI

def run():
    """
    This is the function which will call the UI, will then also call the rest of the program in generate_report().
    Takes no arguments. Returns nothing.
    """
    UI.load_menu()
    return

run()