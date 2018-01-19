from .utilisateurs import mon_utilisateur
from ..application import nom_dapplication


def qui_fait_quoi():
    print(mon_utilisateur + " utilise " + nom_dapplication)