#Задача 3. May the force be with you

import json
import requests


def get_world_name(path: str) -> str:
    response = requests.get(url=path)
    if response.status_code == 200:
        return dict(json.loads(response.text))["name"]


def get_pilot_info(path: str) -> dict:
    response = requests.get(url=path)
    if response.status_code == 200:
        pilot_data = dict(json.loads(response.text))
        return {
            "name": pilot_data["name"],
            "height": pilot_data["height"],
            "mass": pilot_data["mass"],
            "homeworld": get_world_name(pilot_data["homeworld"]),
            "homeworld_url": pilot_data["homeworld"]
        }


def get_millennium_falcon_info() -> dict:
    response = requests.get(url="https://swapi.dev/api/starships/10")

    if response.status_code == 200:
        ship_data = dict(json.loads(response.text))

        return {
            "ship_name": ship_data["name"],
            "max_atmosphering_speed": ship_data["max_atmosphering_speed"],
            "starship_class": ship_data["starship_class"],
            "pilots": [get_pilot_info(pilot_api_page) for pilot_api_page in ship_data["pilots"]]

        }


info = get_millennium_falcon_info()
print(info)
with open("ship_data.json", "w", encoding="UTF-8") as file:
    json.dump(info, file, indent=4)

