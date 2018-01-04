class ObjetExemple:

    def __init__(self):
        self.attribut_exemple = 5

    def change_valeur_attribut_exemple(self, valeur):
        self.attribut_exemple = valeur
        print("Il s'en passe des choses derrière")

objet_exemple = ObjetExemple()