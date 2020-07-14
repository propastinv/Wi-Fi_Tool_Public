from settings import *
from opencage.geocoder import OpenCageGeocode

def reverse_geocode(latitude,longitude):
     KEY = GEO_KEY
     geocoder = OpenCageGeocode(KEY)
     try:
          results = geocoder.reverse_geocode(latitude, longitude)
          region = results[0]['components']['state']
          city = results[0]['formatted']
          address = (str(region) + ',' + str(city))
          # print(address)
     except Exception:
          print("feilure")
     else:
          return address
