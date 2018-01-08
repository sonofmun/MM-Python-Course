from flask import Flask

app = Flask("Application")


@app.route("/")
def index():
    return "Hello world !"


@app.route("/places/<place_id>")
def chemin_place(place_id):
    return "On est sur " + place_id

# Ce if permet de vérifier que ce fichier est celui qui est courrament exécuté. Cela permet par exemple d'éviter
# de lancer une fonction quand on importe ce fichier depuis un autre fichier.
# En python, lorsque l'on exécute un script avec la commande `python script.py`
# Le fichier `script.py` a en __name__ la valeur __main__.
if __name__ == "__main__":
    app.run()
