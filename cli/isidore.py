import click
import requests
import math
import csv

ISIDORE = "https://api.isidore.science/resource/search"


def parser_reponse_isidore(data):
    """ Fait une recherche sur Isidore

    :param data: JSON Parsed Data
    :type q: dict
    :returns: Tuple (
        Nombre de Résultats,
        Nombre de Pages,
        Liste de résultat sous forme de dictionnaire {title, desc, author, date}
    )
    """
    # On récupère le nombre de résultats
    nb_items = int(data["response"]["replies"]["meta"]["@items"])
    # On récupère le nombre de résultats par page
    items_per_page = int(data["response"]["replies"]["meta"]["@pageItems"])
    # Le nombre total de page est l'arrondi supérieur de la division nb_items / items_per_page
    total_page = math.ceil(nb_items / items_per_page)

    # On crée une liste vide dans laquelle on enregistrera les données
    items = []
    # Pour chaque réponse
    for item in data["response"]["replies"]["content"]["reply"]:
        # On ajoute à items un nouvel objet
        items.append({
            "uri": item["@uri"],
            "title": item["isidore"]["title"],
            "date": item["isidore"]["date"]["normalizedDate"],
            "author": []
        })
        # Les auteurs peuvent être plusieurs : dans ce cas, on a une liste sur laquelle on bouclera
        # On utilise items[-1] car il s'agit du dernier item ajouté
        if isinstance(item["isidore"]["enrichedCreators"]["creator"], list):
            for author in item["isidore"]["enrichedCreators"]["creator"]:
                items[-1]["author"].append(author["@normalizedAuthor"])
        else:
            items[-1]["author"].append(item["isidore"]["enrichedCreators"]["creator"]["@normalizedAuthor"])

        # Des fois, le titre est un dictionnaire aussi ou une liste
        if isinstance(items[-1]["title"], dict):
            items[-1]["title"] = items[-1]["title"]["$"]
        if isinstance(items[-1]["title"], list):
            items[-1]["title"] = items[-1]["title"][0]
            # Et des fois, dans cette liste de titre, on a aussi des dictionnaires...
            if isinstance(items[-1]["title"], dict):
                items[-1]["title"] = items[-1]["title"]["$"]

    return nb_items, total_page, items


def cherche_isidore(q, full=False):
    """ Chercher sur isidore en faisant une requête

    :param q: Chaine de recherche
    :type q: str
    :param full: Recherche complète (itère sur toutes les pages)
    :type full: bool
    :returns: Tuple (
        Nombre de Résultats,
        Nombre de Pages,
        Liste de résultat sous forme de dictionnaire {uri, title, desc, author, date}
    )
    """
    # On crée un objet pour récuperer tous les items
    total_items = []

    # On exécute la requête
    params = {"output": "json", "q": q}
    req = requests.get(ISIDORE, params=params)

    # On la parse
    nb_items, total_page, items = parser_reponse_isidore(req.json())

    # On ajoute chacune des valeurs d'items à total_items
    total_items.extend(items)

    return nb_items, total_page, items


@click.command()
@click.argument("query", type=str)
@click.option("-o", "--output", "output_file", type=click.File(mode="w"), default=None,
              help="File in which to write, in a CSV manner, the results")
def run(query, output_file):
    """ Exécute une recherche sur Isidore.science en utilisant [QUERY]
    """
    nb_items, total_page, items = cherche_isidore(query)
    print("Nombre de résultats : {}".format(nb_items))
    print("Nombre de résultats affichés : {}".format(len(items)))
    for item in items:
        print("{}; {}".format(item["title"], "& ".join(item["author"])))

    if output_file:
        writer = csv.writer(output_file)
        writer.writerow(["date", "title", "author", "uri"])
        for item in items:
            writer.writerow([item["date"], item["title"], ", ".join(item["author"]), item["uri"]])


# Si ce fichier est le fichier executé directement par python
# Alors on exécute la commande
if __name__ == "__main__":
    run()
