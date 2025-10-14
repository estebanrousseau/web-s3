def test_auteur_repr(testapp): #testapp est la fixture définie dans conftest.py
    with testapp.app_context():
        auteur=Auteur.query.get(1)
        assert repr(auteur) == "<Auteur (1) Victor Hugo>"