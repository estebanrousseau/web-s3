from monApp.models import Auteur
def test_auteur_init():
    auteur = Auteur("Cricri DAL")
    assert auteur.Nom == "Cricri DAL"