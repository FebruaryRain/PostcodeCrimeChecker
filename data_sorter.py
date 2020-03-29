from radius_filter import within_radius

def data_sorter(lat, long, radius, data, sort):
    '''
    Sorts data by user dfined paramters of distance, date or category, if no parameters are defined then the output data isn't sorted,
    please look in radius_filter for the column headings 
    '''
    sorted_list = []
    DISTANCE = 1
    DATE = 2
    CRIME_CAT = 3
    NONE = 4
    if sort == DISTANCE:
        sorted_list = sorted(within_radius(lat, long, radius, data), key=lambda x: x[-1])
    elif sort == DATE:
        sorted_list = sorted(within_radius(lat, long, radius, data), key=lambda x: x[1])
    elif sort == CRIME_CAT:
        sorted_list = sorted(within_radius(lat, long, radius, data), key=lambda x: x[5])
    else:
        sorted_list = within_radius(lat,long,radius,data)
    return sorted_list

#Tests#

def test_data_sorter_distance():
    #Arrange
    lat = 50.827973
    long = -4.544117
    radius = 5
    sort = 1 #Distance
    data = [['1', '12/2019', '-4.546005', '50.836045', '', 'violence'], ['2', '11/2019', '-4.513619', '50.819101', '', 'shoplifting'], ['3', '03/2018', '-4.512393', '50.829857', '', 'Anti-social behaviour'], ['4', '01/2019', '-4.528076', '50.829401', '', 'criminal damage']]
    expected = [['1', '12/2019', '-4.546005', '50.836045', '', 'violence', 0.907], ['4', '01/2019', '-4.528076', '50.829401', '', 'criminal damage', 1.138], ['3', '03/2018', '-4.512393', '50.829857', '', 'Anti-social behaviour', 2.238], ['2', '11/2019', '-4.513619', '50.819101', '','shoplifting', 2.359]]
    #Act 
    sort_distance = data_sorter(lat,long,radius,data,sort) 
    #Assert 
    assert(sort_distance == expected) 
    
def test_data_sorter_date():
    #Arrange
    lat = 50.827973
    long = -4.544117
    radius = 5
    sort = 2 #Date
    data = [['1', '2019-12', '-4.546005', '50.836045', '', 'violence'], ['2', '2019-11', '-4.513619', '50.819101', '', 'shoplifting'], ['3', '2018-03', '-4.512393', '50.829857', '', 'Anti-social behaviour'], ['4', '2019-01', '-4.528076', '50.829401', '', 'criminal damage']]
    expected = [['3', '2018-03', '-4.512393', '50.829857', '', 'Anti-social behaviour', 2.238], ['4', '2019-01', '-4.528076', '50.829401', '', 'criminal damage', 1.138], ['2', '2019-11', '-4.513619', '50.819101', '','shoplifting', 2.359], ['1', '2019-12', '-4.546005', '50.836045', '', 'violence', 0.907]]
    #Act 
    sort_date = data_sorter(lat,long,radius,data,sort) 
    #Assert 
    assert(sort_date == expected)   
    
def test_data_sorter_category():
    #Arrange
    lat = 50.827973
    long = -4.544117
    radius = 5
    sort = 3 #Sort Category
    data = [['1', '2019-12', '-4.546005', '50.836045', '', 'violence'], ['2', '2019-11', '-4.513619', '50.819101', '', 'shoplifting'], ['3', '2018-03', '-4.512393', '50.829857', '', 'hate crime'], ['4', '2019-01', '-4.528076', '50.829401', '', 'criminal damage']]
    expected = [['4', '2019-01', '-4.528076', '50.829401', '', 'criminal damage', 1.138],['3', '2018-03', '-4.512393', '50.829857', '', 'hate crime', 2.238], ['2', '2019-11', '-4.513619', '50.819101', '','shoplifting', 2.359], ['1', '2019-12', '-4.546005', '50.836045', '', 'violence', 0.907]]
    #Act 
    sort_category = data_sorter(lat,long,radius,data,sort) 
    #Assert 
    assert(sort_category == expected)      
    
def test_data_sorter_none():
    #Arrange
    lat = 50.827973
    long = -4.544117
    radius = 5
    sort = 4 #None
    data = [['1', '2019-12', '-4.546005', '50.836045', '', 'violence'], ['2', '2019-11', '-4.513619', '50.819101', '', 'shoplifting'], ['3', '2018-03', '-4.512393', '50.829857', '', 'hate crime'], ['4', '2019-01', '-4.528076', '50.829401', '', 'criminal damage']]
    expected = [['1', '2019-12', '-4.546005', '50.836045', '', 'violence', 0.907], ['2', '2019-11', '-4.513619', '50.819101', '', 'shoplifting', 2.359], ['3', '2018-03', '-4.512393', '50.829857', '', 'hate crime', 2.238], ['4', '2019-01', '-4.528076', '50.829401', '', 'criminal damage', 1.138]]
    #Act 
    sort_none = data_sorter(lat,long,radius,data,sort) 
    #Assert 
    assert(sort_none == expected) 
     
    
if __name__ == '__main__':
      test_data_sorter_distance()
      test_data_sorter_date()
      test_data_sorter_category()
      test_data_sorter_none()
      
