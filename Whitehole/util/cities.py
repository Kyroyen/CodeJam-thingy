import pandas as pd
import requests


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
