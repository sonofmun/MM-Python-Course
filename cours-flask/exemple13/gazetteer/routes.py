from flask import render_template


from .app import app
from .modeles.donnees import Place


@app.route("/")
def accueil():
    # On a bien sûr aussi modifié le template pour refléter le changement
    lieux = Place.query.all()
    return render_template("pages/accueil.html", nom="Gazetteer", lieux=lieux)


@app.route("/place/<int:place_id>")
def lieu(place_id):
    # On a bien sûr aussi modifié le template pour refléter le changement
    unique_lieu = Place.query.get(place_id)
    return render_template("pages/place.html", nom="Gazetteer", lieu=unique_lieu)
