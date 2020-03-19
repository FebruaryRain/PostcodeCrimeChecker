from read_files import open_a_file_and_retrieve_contents
from pathlib import Path

records = open_a_file_and_retrieve_contents(Path("Devon_postcodes/postcodes.csv"))

for row in records:
    if len(row[0]) <7:
        print(row[0], end = " ")
print("Finished")

def distance_to_1_dp(latlngA, latlngB):
    """
    Takes in 2 latitude/longitude tuples in the format (x,y).
    Returns the distance to 1 decimal place in km.
    Calls the distance function, provided by the lecturers.
    This is the function to call as the original is too precise to be useful. 
    """
    return round(distance( latlngA, latlngB), 1)

def distance_to_1_dp_should_return_data_rounded_correctly():
    list_of_lat_and_longs_1 = [
        (50.71527036,-2.44427954),
        (50.97137163,-4.40200942)
    ]
    list_of_lat_and_longs_2 = [
        (50.829232,-4.544128),
        (50.462646,-4.714629),
        (50.457415,-4.467377),
        (50.421859,-5.057535),
        (50.740558,-3.988073)
    ]
    list_of_lat_long_returns_1 = []
    list_of_lat_long_expected_1 = [
        148.2, 
        162.7, 
        145.7, 
        187.4, 
        108.7
    ]

    list_of_lat_long_returns_2 = []
    list_of_lat_long_expected_2 = [
        18.7, 
        60.7, 
        57.3, 
        76.6, 
        38.8
    ] 
    for coord in list_of_lat_and_longs_2:
        list_of_lat_long_returns_1.append(distance_to_1_dp(list_of_lat_and_longs_1[0], coord))
    for coord in list_of_lat_and_longs_2:
        list_of_lat_long_returns_2.append(distance_to_1_dp(list_of_lat_and_longs_1[1], coord))
    assert(list_of_lat_long_returns_1 == list_of_lat_long_expected_1)
    assert(list_of_lat_long_returns_2 == list_of_lat_long_expected_2)
    return

#    distance_to_1_dp_should_return_data_rounded_correctly()