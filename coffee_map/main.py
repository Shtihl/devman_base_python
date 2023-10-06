import json
import os
import requests
import folium
from geopy import distance
from flask import Flask
from dotenv import load_dotenv


def fetch_coordinates(apikey, address):
    base_url = "https://geocode-maps.yandex.ru/1.x"
    response = requests.get(
        base_url,
        params={
            "geocode": address,
            "apikey": apikey,
            "format": "json",
        },
    )
    response.raise_for_status()
    found_places = response.json()["response"]["GeoObjectCollection"]["featureMember"]

    if not found_places:
        return None

    most_relevant = found_places[0]
    lon, lat = most_relevant["GeoObject"]["Point"]["pos"].split(" ")
    return lat, lon


def get_user_place(apikey):
    return fetch_coordinates(apikey, input("Где вы находитесь: "))


def get_coffee_base():
    with open("coffee.json", "r", encoding="CP1251") as coffee:
        coffee_json = coffee.read()
    return coffee_json


def get_distance(coffee_base, user_place):
    coffee_distance_list = []
    for coffee_id in range(0, len(coffee_base) - 1):
        coffee_name = coffee_base[coffee_id]["Name"]
        coffee_place = (
            coffee_base[coffee_id]["Latitude_WGS84"],
            coffee_base[coffee_id]["Longitude_WGS84"],
        )
        coffee_distance = {
            "title": coffee_name,
            "distance": distance.distance(user_place, coffee_place).km,
            "latitude": coffee_place[0],
            "longitude": coffee_place[1],
        }
        coffee_distance_list.append(coffee_distance)
    return coffee_distance_list


def get_coffee_distance(coffee):
    return coffee["distance"]


def create_map(user_place, number_of_point, coffee_distance_list):
    coffee_map = folium.Map(
        location=user_place, tiles="cartodb positron", zoom_start=13
    )
    markers_list = sorted(coffee_distance_list, key=get_coffee_distance)[
        0:number_of_point
    ]
    for marker in markers_list:
        folium.Marker(
            location=[marker["latitude"], marker["longitude"]],
            tooltip=marker["title"],
            popup=marker["title"],
            icon=folium.Icon(icon="cloud"),
        ).add_to(coffee_map)
    coffee_map.save("index.html")


def hello_world():
    with open("index.html") as file:
        return file.read()


def main():
    load_dotenv()
    apikey = os.environ["GEOCODER_API_KEY"]
    user_place = get_user_place(apikey)
    number_of_point = 5
    coffee_base = json.loads(get_coffee_base())
    coffee_distance = get_distance(coffee_base, user_place)
    create_map(user_place, number_of_point, coffee_distance)
    app = Flask(__name__)
    app.add_url_rule("/", "coffee_map", hello_world)
    app.run("0.0.0.0")


if __name__ == "__main__":
    main()
