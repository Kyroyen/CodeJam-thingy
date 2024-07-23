from geopy import distance
import pandas as pd
import requests
import math


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


def road_distance(city1: str, city2: str) -> float:
    pass


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

    coords1 = Database.get_coordinates(city)
    coords2 = Database.get_coordinates(city2)

    print("ground distance b/w them is: {}".format(
        ground_distance(coords1, coords2)
    ))
    print("spatial distance b/w them is: {}".format(
        spatial_distance(coords1, coords2)
    ))
