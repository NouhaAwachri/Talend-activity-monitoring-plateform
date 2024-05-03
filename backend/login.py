from flask import Blueprint, url_for, render_template, redirect, request, flash
from flask_login import LoginManager, login_user
from werkzeug.security import check_password_hash

from models import db, Users

login = Blueprint('login', __name__, template_folder='../frontend')
login_manager = LoginManager()
login_manager.init_app(login)

@login.route('/login', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if not email or not password:
            flash('Veuillez remplir tous les champs', 'error')
            return redirect(url_for('login.show'))

        user = Users.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('home.show'))
            else:
                flash('Mot de passe incorrect', 'error')
                return redirect(url_for('login.show'))
        else:
            flash('Utilisateur introuvable', 'error')
            return redirect(url_for('login.show'))
    else:
        return render_template('login.html')
