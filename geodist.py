# geogdist.py
# Version 0.2

import math

def distance( latlngA, latlngB):
    '''
    distance( (latA,lngA), (latB,lngB) ) -> float (distance in km)

    Returns the approximate straight line distance between two nearby points
    on the surface of the Earth assuming a sphere. 
    With the default value of R of 6371.009 the distance will be in kilometers.
    See also: https://en.wikipedia.org/wiki/Geographical_distance
    '''
    R = 6371.009 # approximate radius of earth surface (radius from center
                 # of the sphere in km)
    latA, lngA = latlngA
    lngA = math.radians(lngA)
    latA = math.radians(latA)
    latB, lngB = latlngB
    lngB = math.radians(lngB)
    latB = math.radians(latB)
    x = ( lngB - lngA ) * math.cos( (latA + latB) / 2 )
    y = latB - latA
    d = math.sqrt( x*x + y*y ) * R
    return d

## Tests
def distance_should_return_correct_distances_when_given_two_valid_points():
    list_of_lat_and_longs_1 = [
        (-2.44427954,50.71527036),
        (-4.40200942,50.97137163)
    ]
    list_of_lat_and_longs_2 = [
        (-4.544128,50.829232),
        (-4.714629,50.462646),
        (-4.467377,50.457415),
        (-5.057535,50.421859),
        (-3.988073,50.740558)
    ]
    list_of_lat_long_returns_1 = []
    list_of_lat_long_expected_1 = [
        233.83515970684675, 
        254.00367188668648, 
        226.77176534446895, 
        292.39922075200764, 
        171.6851984351975
    ]

    list_of_lat_long_returns_2 = []
    list_of_lat_long_expected_2 = [
        22.316295380280835, 
        66.24261329441788, 
        57.44009423308353, 
        94.98070603992166, 
        52.666246628324394
    ] 
    for coord in list_of_lat_and_longs_2:
        list_of_lat_long_returns_1.append(distance(list_of_lat_and_longs_1[0], coord))
    for coord in list_of_lat_and_longs_2:
        list_of_lat_long_returns_2.append(distance(list_of_lat_and_longs_1[1], coord))
    assert(list_of_lat_long_returns_1 == list_of_lat_long_expected_1)
    assert(list_of_lat_long_returns_2 == list_of_lat_long_expected_2)
    #print(list_of_lat_long_returns_1)
    #print(list_of_lat_long_returns_2)
    return

if __name__ == "__main__":
    # Testing
    # TODO: Please verify the function by providing suitable test cases and
    # using asserts. The test should cover the cases your program is to deal
    # with, e.g. do not verify the correct distance between New York and London
    # For your testing allow a tolerance for the distance calculation as the
    # calculation is an approximation.

    #print(distance( (-4.544128,50.829232), (-4.544117,50.827973)))
    distance_should_return_correct_distances_when_given_two_valid_points()
