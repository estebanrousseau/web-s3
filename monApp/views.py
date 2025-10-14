from .app import app
from flask import render_template, request
from monApp.models import Auteur
from monApp.models import Livre
from monApp.forms import FormAuteur
from monApp.forms import FormLivre
from monApp.forms import LoginForm
from flask import url_for , redirect
from .app import db
from flask_login import logout_user, login_user, login_required

@app.route('/auteur/')
def createAuteur():
    unForm = FormAuteur()
    return render_template("auteur_create.html", createForm=unForm)


@app.route('/auteurs/<idA>/delete/')
@login_required
def deleteAuteur(idA):
    unAuteur = Auteur.query.get(idA)
    unForm = FormAuteur(idA=unAuteur.idA, Nom=unAuteur.Nom)
    return render_template("auteur_delete.html",selectedAuteur=unAuteur, deleteForm=unForm)

@app.route('/auteur/erase/', methods=("POST",))
def eraseAuteur():
    deletedAuteur = None
    unForm = FormAuteur()
    # recherche de l'auteur à supprimer
    idA = int(unForm.idA.data)
    deletedAuteur = Auteur.query.get(idA)
    # suppression
    db.session.delete(deletedAuteur)
    db.session.commit()
    return redirect(url_for('getAuteurs'))


@app.route('/auteur/insert/', methods=("POST",))
@login_required
def insertAuteur():
    insertedAuteur = None
    unForm = FormAuteur()
    if unForm.validate_on_submit():
        insertedAuteur = Auteur(Nom=unForm.Nom.data)
        db.session.add(insertedAuteur)
        db.session.commit()
        insertedId = insertedAuteur.idA
        return redirect(url_for('viewAuteur', idA=insertedId))
    return render_template("auteur_create.html", createForm=unForm)

@app.route('/auteur/save/', methods=("POST",))
def saveAuteur():
    updatedAuteur = None
    unForm = FormAuteur()
    # recherche de l'auteur à modifier
    idA = int(unForm.idA.data)
    updatedAuteur = Auteur.query.get(idA)
    # si les données saisies sont valides pour la mise à jour
    if unForm.validate_on_submit():
        updatedAuteur.Nom = unForm.Nom.data
        db.session.commit()
        return redirect(url_for('viewAuteur', idA=updatedAuteur.idA))
    return render_template("auteur_update.html", selectedAuteur=updatedAuteur, updateForm=unForm)


@app.route('/auteurs/<idA>/view/')
@login_required
def viewAuteur(idA):
    unAuteur = Auteur.query.get(idA)
    unForm = FormAuteur (idA=unAuteur.idA , Nom=unAuteur.Nom)
    return render_template("auteur_view.html",selectedAuteur=unAuteur, viewForm=unForm)


@app.route('/about/')
def about():
    return render_template("about.html",title ="R3.01 Dev Web avec Flask",name= app.config['ABOUT']) 

@app.route('/auteurs/<idA>/update/')
@login_required
def updateAuteur(idA):
    unAuteur = Auteur.query.get(idA)
    unForm = FormAuteur(idA=unAuteur.idA , Nom=unAuteur.Nom)
    return render_template("auteur_update.html",selectedAuteur=unAuteur, updateForm=unForm)


@app.route('/contact/')  
def contact(): 
    return render_template("contact.html",title ="R3.01 Dev Web avec Flask",name= app.config['CONTACT']) 

@app.route('/')
@app.route('/index/')
def index():
# si pas de paramètres
    if len(request.args)==0:
        return render_template("index.html",title="R3.01 Dev Web avec Flask",name="Cricri")
    else :
        param_name = request.args.get('name')
        return render_template("index.html",title="R3.01 Dev Web avec Flask",name=param_name) 

@app.route('/auteurs/')
def getAuteurs():
    lesAuteurs = Auteur.query.all()
    return render_template('auteurs_list.html', title="R3.01 Dev Web avec Flask", auteurs=lesAuteurs)
    

@app.route('/livres/')
def getLivres():
    lesLivres = Livre.query.all()
    return render_template('livre_list.html', title="R3.01 Dev Web avec Flask", livres=lesLivres)

@app.route('/livres/<Idl>/view/')
@login_required
def viewLivre(Idl):
    unLivre = Livre.query.get(Idl)
    unForm = FormLivre(Idl= unLivre.Idl , Titre = unLivre.Idl)
    return render_template("livre_view.html",selectedLivre=unLivre, viewForm=unForm)    

@app.route('/livres/<Idl>/update/')
@login_required
def updateLivre(Idl):
    unLivre = Livre.query.get(Idl)
    unForm = FormLivre(Idl= unLivre.Idl , Titre = unLivre.Idl)
    return render_template("livre_update.html",selectedAuteur=unLivre, updateForm=unForm)

@app.route("/login/", methods=("GET", "POST"))
def login():
    unForm = LoginForm()
    unUser = None
    if not unForm.is_submitted():
        unForm.next.data = request.args.get('next')
    elif unForm.validate_on_submit():
        unUser = unForm.get_authenticated_user()
        if unUser:
            login_user(unUser)
            next_url = unForm.next.data or url_for("index", name=unUser.Login)
            return redirect(next_url)
    return render_template("login.html", form=unForm)

@app.route ("/logout/")
def logout():
    logout_user()
    return redirect ( url_for ('index'))



if __name__ == "__main__":
    app.run()