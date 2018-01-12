""" Ce script a pour but de générer un ensemble de données tests pour le cours sur Flask

Les données originelles sont toutes issues de https://pleiades.stoa.org

"""
from requests import get
from csv import writer
import os


dir_path, _ = os.path.split(os.path.realpath(__file__))  # On utilise la variable nommée "_" par convention
                                                         #  pour des données d'un tuple que l'on ne veut pas
target_path = os.path.join(dir_path, "..", "csv", "pleiades.csv")

places_to_retrieve = [462247, 511337, 59687, 187410, 462283, 874299107,
                      264408879, 423052, 79368, 599578, 727090, 570180, 138369, 695491849, 589981]
csv_list = [
    ["place_id", "place_nom", "place_description", "place_longitude", "place_latitude", "place_type"]
]

for index, place in enumerate(places_to_retrieve):
    response = get("https://pleiades.stoa.org/places/{}/json".format(place))
    data = response.json()
    lat, long = tuple(data["reprPoint"])
    description = data["description"]
    nom = data["title"]
    place_type = data["placeTypes"][0]
    csv_list.append([index, nom, description, long, lat, place_type])

with open(target_path, "w") as f:
    csv_writer = writer(f)
    for row in csv_list:
        csv_writer.writerow(row)
