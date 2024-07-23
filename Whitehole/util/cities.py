from geopy import distance
from geopy.geocoders import Nominatim
from urllib.parse import urlencode
import requests
import pandas as pd
import math
import dotenv
import os

dotenv.load_dotenv()
geolocator = Nominatim(user_agent="CodeJamProject")
openrouteservice_api_key = os.getenv('OPENROUTESERVICE_API_KEY')


class Database:
    df = pd.read_csv("cities dataset/worldcities.csv")

    @classmethod
    def does_city_exist(cls, city_name: str) -> bool:
        return city_name in cls.df["city"].values

    @classmethod
    def get_coordinates(cls, city_name: str) -> (float, float):
        try:
            city_row = cls.df.loc[cls.df['city'] == city_name].iloc[0]
            lat = float(city_row['lat'])
            lon = float(city_row['lon'])
            return (lat, lon)

        except IndexError:
            raise ValueError(f"City {city_name} not found in dataset")


def fetch_city_geocode(city: str) -> (float, float):
    geocode_data = geolocator.geocode(city)
    if geocode_data:
        lat, lon = geocode_data.latitude, geocode_data.longitude
        return (lat, lon)
    else:
        raise ValueError("Could not get city geocode")


def degrees_to_radians(deg: float) -> float:
    return deg * math.pi / 180


def coords_in_radians(coords: (float, float)) -> (float, float):
    return tuple(map(degrees_to_radians, coords))


def ground_distance(coords1: (float, float), coords2: (float, float)) -> float:
    return distance.geodesic(coords1, coords2).km


def spatial_distance(coords1: (float, float), coords2: (float, float)) -> float:
    radius = 6371
    lat1, lon1 = coords_in_radians(coords1)
    lat2, lon2 = coords_in_radians(coords2)

    # Calculate the central angle using the sperical law of cosines
    cos_delta_sigma = math.sin(lat1) * math.sin(lat2) + \
        math.cos(lat1) * math.cos(lat2) * math.cos(lon2 - lon1)

    # Calculate the chord length
    chord_len = radius * math.sqrt(2 * (1 - cos_delta_sigma))

    return chord_len


def road_distance(coords1: (float, float), coords2: (float, float)) -> float | None:

    start_coords = '{},{}'.format(*coords1)
    end_coords = '{},{}'.format(*coords2)

    api_url = "https://api.openrouteservice.org/v2/directions/driving-car"
    params = {
        'api_key': openrouteservice_api_key,
        'start': start_coords,
        'end': end_coords
    }

    url = api_url + '?' + urlencode(params)

    try:
        response = requests.get(url)
        data = response.json()
        print(data)
        distance = data['features'][0]['properties']['segments'][0]['distance']
        return distance / 1000

    except Exception as e:
        print("openrouteservice error:", e)
        return None


if __name__ == "__main__":
    city = input("Enter name of a city: ")

    if Database.does_city_exist(city):
        print(f"{city} exists")
    else:
        print(f"{city} does not exists")

    try:
        coords = Database.get_coordinates(city)
        print(f"{city} is at {coords}")
    except ValueError:
        print(f"couldn't get {city}'s coordinates")

    city2 = input("\nEnter name of another city: ")

    # coords1 = Database.get_coordinates(city)
    # coords2 = Database.get_coordinates(city2)

    coords1 = fetch_city_geocode(city)
    coords2 = fetch_city_geocode(city2)

    print("ground distance b/w them is: {}".format(
        ground_distance(coords1, coords2)
    ))
    print("spatial distance b/w them is: {}".format(
        spatial_distance(coords1, coords2)
    ))
    print("road distance b/w them is: {}".format(
        road_distance(coords1, coords2)
    ))
