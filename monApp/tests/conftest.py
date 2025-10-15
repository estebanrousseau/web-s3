import pytest
from monApp import app, db
from monApp.models import Auteur

@pytest.fixture
def testapp():
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "WTF_CSRF_ENABLED": False})
    
    with app.app_context():
        db.create_all()
        # Ajouter un auteur de test
        auteur = Auteur(Nom="Victor Hugo")
        db.session.add(auteur)
        db.session.commit()

        livre = livre(10, "Harry pot de fleur", "url de fou", "", 4)
        db.session.add(livre)
        db.session.commit()
        
    yield app
    # Cleanup après les tests
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(testapp):
    return testapp.test_client()