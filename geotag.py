import json
from geopy import Nominatim
from datetime import datetime 

class GeoTag:

    def __init__(self, latitude, longitude):

        # We get a nominatim instance and specify the name of the application in user_agent.
        geolocator = Nominatim(user_agent="GeoTag - Tag Generator")
        
        # We get the name of the location from the coordinates
        self.location = geolocator.reverse(f"{latitude}, {longitude}").address
        
        self.coordinates = {
            "latitude": latitude,
            "longitude": longitude
        }
        
        # We set the date and time at which this tag was created
        self.creationDate = round(datetime.now().timestamp()*1000)

    # Returns a serialized JSON object of the tag
    def to_json(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    
