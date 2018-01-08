from flask import Flask, render_template

app = Flask("Application")


@app.route("/")
@app.route("/exemple/<exemple>")
def accueil(exemple=None):
    lieux = []
    if exemple:
        lieux = ["Col. Lugdunum", "Augustomagus"]
    return render_template("accueil.html", nom="Gazetteer", lieux=lieux)



# Ce if permet de vérifier que ce fichier est celui qui est courrament exécuté. Cela permet par exemple d'éviter
# de lancer une fonction quand on importe ce fichier depuis un autre fichier.
# En python, lorsque l'on exécute un script avec la commande `python script.py`
# Le fichier `script.py` a en __name__ la valeur __main__.
if __name__ == "__main__":
    app.run()
