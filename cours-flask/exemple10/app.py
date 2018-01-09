from flask import Flask, render_template

app = Flask("Application")

lieux = {
    0: {
        "nom": "Col. Lugdunum",
        "moderne": "Lyon",
        "latlong": [45.762095775, 4.822438025],
        "type": "ville",
        "description": "Col. Lugdunum was a Roman military colony from 43 BC and a major center in Gaul. Marcus "
                       "Agrippa was involved in its expansion and two Roman emperors, Claudius and Caracalla, "
                       "were born there."
    },
    1: {
        "nom": "Samarobriva Ambianorum",
        "moderne": "Amiens",
        "type": "ville",
        "description": "An ancient place, cited: BAtlas 11 C3 Samarobriva Ambianorum ",
        "latlong": [49.8936075, 2.297948]
    }
}


@app.route("/")
def accueil():
    return render_template("pages/accueil.html", nom="Gazetteer", lieux=lieux)


@app.route("/place/<int:place_id>")
def lieu(place_id):
    return render_template("pages/place.html", nom="Gazetteer", lieu=lieux[place_id])


# Ce if permet de vérifier que ce fichier est celui qui est courrament exécuté. Cela permet par exemple d'éviter
# de lancer une fonction quand on importe ce fichier depuis un autre fichier.
# En python, lorsque l'on exécute un script avec la commande `python script.py`
# Le fichier `script.py` a en __name__ la valeur __main__.
if __name__ == "__main__":
    app.run(debug=True)
