from file_reader import open_a_file_and_retrieve_contents
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



# def get_all_crime_records_stripped():
#     """
#     Takes in the single list of all crime records.
#     To get all crime records, enter the argument "all_crime_records()", importing this function from this module to do so. 
#     Returns these records without the 12th, 9th, 8th, 4th, 3rd elements as these were decided to be superfluous.
#     This is done by adding the details sequentially to a new list, assigning the value of this new list to the record.
#     """
#     all_crime_records = create_unified_list_of_crime_records(read_all_records())
    
#     for record in all_crime_records:
#         wanted_details = []
#         wanted_details.append(record[0])
#         wanted_details.append(record[1])
#         wanted_details.append(record[4])
#         wanted_details.append(record[5])
#         wanted_details.append(record[6])
#         wanted_details.append(record[9])
#         wanted_details.append(record[10])
#         wanted_details.append(record[11])
#         record = wanted_details
#     return all_crime_records


filepath = Path("Devon_and_Cornwall_crime_data_2019/2019-01/2019-01-devon-and-cornwall-street.csv")


Test11 = "Test11"
Test12 = "Test12"
Test13 = "Test13"
Test14 = "Test14"
Test21 = "Test21"
Test22 = "Test22"
Test23 = "Test23"
Test24 = "Test24"
Test51 = "Test51"
Test52 = "Test52"
Test53 = "Test53"
Test54 = "Test54"
default_postcode_value = "EX230LP"
default_radius_value = 5
default_data_sort_value = 4
default_filename_value = Test54