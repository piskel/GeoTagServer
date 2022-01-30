import json
from geopy import Nominatim
from datetime import datetime 

class GeoTag:

    def __init__(self, latitude, longitude):

        geolocator = Nominatim(user_agent="GeoTag - Tag Generator")
        
        self.location = geolocator.reverse(f"{latitude}, {longitude}").address
        
        self.coordinates = {
            "latitude": latitude,
            "longitude": longitude
        }

        self.creationDate = round(datetime.now().timestamp()*1000)






    
    def to_json(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    
