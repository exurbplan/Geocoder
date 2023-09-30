# Libraries
import pandas as pd
from geopy.geocoders import GoogleV3

# Dataframe:
data = pd.read_csv(r'***')

def geocode_location(location):
    print("Geocoding:", location)  # Add this line
    geolocator = GoogleV3(api_key='***')
    location = geolocator.geocode(location)
    if location is not None:
        return location.latitude, location.longitude
    else:
        
        return None, None


data['Latitude'], data['Longitude'] = zip(*data['***'].apply(geocode_location))

data.to_csv('geocoded_data.csv', index=False)
