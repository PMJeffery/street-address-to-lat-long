import csv
"""
Optional: Chagne the geocoder to anything that is natively supported in GeoCoders: https://github.com/geopy/geopy/tree/master/geopy/geocoders
Default: Photon
"""
from geopy.geocoders import Photon
"""
Optional: change the user_agent from 'http' to anything else
"""
geolocator = Photon(user_agent="http")
"""
Input file must be a plain text file. Ex: addresses.txt
Each address must be in their own row
"""
def get_location_by_address(address):
    """
    This function returns the latitude and longitude of a given address
    :param address: Address in string format
    :return: latitude and longitude
    """
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None
''' Outputs a CSV file, with Header, as Address, Latitude, Longitude, per row '''
with open('addresses.txt', 'r') as input_file, open('output.csv', 'w', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    csv_writer.writerow(['Address', 'Latitude', 'Longitude'])
    for address in input_file:

        address = address.strip()
        lat, long = get_location_by_address(address)
        csv_writer.writerow([address, lat, long])
