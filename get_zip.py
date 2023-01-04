import sys
from geopy.geocoders import Nominatim

def get_zip_code(latitude, longitude):
    geolocator = Nominatim(user_agent="ti_green_signal")
    location = geolocator.reverse(str(latitude) + ", " + str(longitude))
    print (location.address)
    #print (location.raw['address']['postcode'])
    return location.raw['address']['postcode']
   


if __name__ == '__main__':
    if len(sys.argv) >=3:
        zipcode = get_zip_code(sys.argv[1], sys.argv[2])
        print('zip code {0}'.format(zipcode))
    else:
        print("program expects two inputs: latitude longitude")
