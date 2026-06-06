import requests

class Weather:
    """Creates a Weather object getting an apikey as input
    and either a city name or lat and lon coordinates.

    Package use example:

    # Create a weather object using a city name:
    # The api key below is not guaranteed to work.
    # Get your own apikey from https://openweathermap.org
    # And wait a couple of hours for the apikey to be activated

    >>> weather1 = Weather(
    ...     apikey="26631f0f41b95fb9f5ac0df9a8f43c92",
    ...     city="Madrid"
    ... )

    # Using latitude and longitude coordinates
    >>> weather2 = Weather(
    ...     apikey="26631f0f41b95fb9f5ac0df9a8f43c92",
    ...     lat=41.1,
    ...     lon=-4.1
    ... )

    # Get complete weather data for the next 12 hours:
    >>> weather1.next_12h()

    # Simplified data for the next 12 hours:
    >>> weather1.next12h_simplified()

    """

    def __init__(self, apikey, city=None, lat=None, lon=None):

        if city is not None:
            geocoding_api = f"http://api.openweathermap.org/geo/1.0/direct?q={city.replace(' ', '-').lower()}&limit=1&appid={apikey}"
            coords = requests.get(geocoding_api).json()
            if not coords:
                raise ValueError("City not found.")

            lat, lon = coords[0]['lat'], coords[0]['lon']

        if lat is None or lon is None:
            raise ValueError(
                "Provide either a city name or both latitude and longitude."
            )

        forecast_api = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={apikey}&units=metric"
        forecast = requests.get(forecast_api)
        forecast.raise_for_status()

        data = forecast.json()

        if data.get("cod") != "200":
            raise ValueError("Invalid latitude/longitude.")

        self.data = data


    def next_12h(self):
        """ returns 12 hr complete weather data as a dict"""

        return self.data['list'][:4]

    def next_12h_simplified(self):
        """ returns simplified 12 hr weather data (date and time, temperature, humidity, prediction) as a list of dicts"""

        simple_forecast = []
        for forecast in self.data['list'][:4]:
            simple_forecast.append({"Date and Time": forecast['dt_txt'],"Temperature": forecast['main']['temp'],"Humidity": forecast['main']['humidity'],"Prediction": forecast['weather'][0]['description']})

        return simple_forecast


