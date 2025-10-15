from monApp.models import Livre

def test_auteur_init():
    livre = Livre(10, "Harry pot de fleur", "url de fou", "", 4)
    assert livre.Titre == "Harry pot de fleur"

def test_livre_repr(testapp): #testapp est la fixture définie dans conftest.py
    with testapp.app_context():
        liv = Livre.query.get(1)
        assert repr(liv) == "<Livre (101) Robin Hobb>"