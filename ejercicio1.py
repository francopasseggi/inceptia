import requests

class GeoAPI:
    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT =  "-35.836948753554054"
    LON = "-61.870523905384076"

    @classmethod
    def is_hot_in_pehuajo(cls):
        
        # api call, return false if error
        url = "http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}".format(lat=cls.LAT, lon=cls.LON, key=cls.API_KEY)
        response = requests.get(url)
        
        if response.status_code != 200:
            return False

        # parse response
        data = response.json()
        temp = data["main"]["temp"]

        return temp > 28