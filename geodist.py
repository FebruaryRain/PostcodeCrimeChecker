"""
Module provided at project start.
Tests added. 
This module calculates the distances between two points.
It takes in two tuples with values of lat long as floats to represent GPS 
coordinates. 
Returns the distance between two points in Km. 
"""

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

def distance_to_3_dp(latlngA, latlngB):
    """
    Takes in 2 latitude/longitude tuples in the format (x,y).
    Returns the distance to 3 decimal places in km.
    Calls the distance function, provided by the lecturers.
    This is the function to call as the original is too precise to be useful. 
    """
    return round(distance( latlngA, latlngB), 3)

#####
## Tests
#####

def distance_should_return_correct_distances_when_given_two_valid_points():
    # Arrange
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
        148.20466391920365, 
        162.71939503946365, 
        145.67892684622396, 
        187.4254011154713, 
        108.69922499358259
    ]
    list_of_lat_long_returns_2 = []
    list_of_lat_long_expected_2 = [
        18.685155713789822, 
        60.698686464704565, 
        57.334468822257904, 
        76.58571912542108, 
        38.76803743069468
    ] 
    # Act
    for coord in list_of_lat_and_longs_2:
        list_of_lat_long_returns_1.append(distance(list_of_lat_and_longs_1[0], coord))
    for coord in list_of_lat_and_longs_2:
        list_of_lat_long_returns_2.append(distance(list_of_lat_and_longs_1[1], coord))
    # Assert
    assert(list_of_lat_long_returns_1 == list_of_lat_long_expected_1)
    assert(list_of_lat_long_returns_2 == list_of_lat_long_expected_2)
    return

if __name__ == "__main__":
    distance_should_return_correct_distances_when_given_two_valid_points()
