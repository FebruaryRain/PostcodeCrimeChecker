"""
This module serves to act as the filter which determines if crime records fall within the user defined 
radius around a given postcode's central point. 
It takes in the lat and long of the postcode, the radius, and all of the data. 
It returns a list of all the records which are within the radius of the postcode, as well as appending 
the distance as a final value to those records. 
"""

from geodist import distance, distance_to_3_dp

def within_radius(lat,long,radius,data):
    '''This prints all the crime data within the given radius as list of lists, in the format [crime id, date, long, lat, near where the crime was located, crime type, last outcome category, distance from given postcode(km)] '''
    within_radius = []
    LAT_POS = 3
    LONG_POS = 2
    for row in data:
        try:
            distance_from_centre = distance_to_3_dp((lat,long), (float(row[LAT_POS]),float(row[LONG_POS])))
            if distance_from_centre <= radius:
                row.append(distance_from_centre) 
                within_radius.append(row) 
            else:
                pass  
        except:
            pass
    return within_radius 

#####
#Tests#
#####

def test_radius_filter_1():
    #Arrange
    lat = 50.827973
    long = -4.544117
    radius = 1
    data = [['1', '12/2019', '-4.546005', '50.836045'],['2', '11/2019', '-4.513619', '50.819101'],['3', '03/2018', '-4.512393', '50.829857']]
    expected = [['1', '12/2019', '-4.546005', '50.836045', 0.907]]
    #Act 
    filter1 = within_radius(lat,long,radius,data)  
    #Assert
    assert(filter1 == expected) 
    
def test_radius_filter_2():
    #Arrange
    lat = 50.827973
    long = -4.544117
    radius = 2
    data = [['1', '12/2019', '-4.546005', '50.836045'],['2', '2019-01', '-4.513619', '50.819101'],['','2019-01', '-4.458826', '50.761501']]
    expected = [['1', '12/2019', '-4.546005', '50.836045', 0.907]]
    #Act 
    filter2 = within_radius(lat,long,radius,data)  
    #Assert
    assert(filter2 == expected) 
    
def test_radius_filter_5():
    #Arrange
    lat = 50.827973
    long = -4.544117
    radius = 5
    data = [['1', '12/2019', '-4.546005', '50.836045'],['2', '2019-01','-4.513619', '50.819101'],['','2019-01', '-4.458826', '50.761501'], ['6','2019-01', '-4.484190', '50.875585']]
    expected = [['1', '12/2019', '-4.546005', '50.836045', 0.907],['2', '2019-01', '-4.513619', '50.819101', 2.359]]
    #Act 
    filter5 = within_radius(lat,long,radius,data)  
    #Assert
    assert(filter5 == expected)     

if __name__ == '__main__':
    test_radius_filter_1()
    test_radius_filter_2()
    test_radius_filter_5() 