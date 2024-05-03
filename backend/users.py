from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash
from models import db, Users

users = Blueprint('users', __name__)

@users.route('/users')
@login_required
def show():
    # Vérifier si l'utilisateur actuel est l'utilisateur spécifique auquel vous voulez restreindre l'accès
    if current_user.email == 'hnaguech@dataraise.com':
        # Récupérer les utilisateurs depuis la base de données
        users = Users.query.all()

        return render_template('users.html', users=users)
    else:
        # Rediriger ou afficher un message d'erreur aux utilisateurs qui ne sont pas autorisés à accéder à la page
        return render_template('access_denied.html')


@users.route('/users/delete/<int:userid>', methods=['POST'])
@login_required
def delete(userid):
    # Récupérer l'utilisateur depuis la base de données
    user = Users.query.get(userid)

    if user:
        # Supprimer l'utilisateur de la base de données
        db.session.delete(user)
        db.session.commit()
        flash('User deleted successfully.')

    # Rediriger vers la page des utilisateurs
    return redirect(url_for('users.show'))


@users.route('/users/edit/<int:userid>', methods=['POST'])
@login_required
def edit(userid):
    # Récupérer l'utilisateur depuis la base de données
    user = Users.query.get(userid)
    if user:
        # Mettre à jour les informations de l'utilisateur en fonction des données du formulaire soumis
        user.username = request.form.get('username')
        user.email = request.form.get('email')
        user.password = request.form.get('password')
        user.confirm_password = request.form.get('confirm-password')
        if user.username and user.email and user.password and user.password == user.confirm_password:
            if not user.email.endswith('@dataraise.com'):
                flash('Invalid email!')
                return redirect(url_for('users.edit', userid=userid))
            
            if len(user.password) < 8:
                flash('The password must be 8 characters or more!')
                return redirect(url_for('users.edit', userid=userid))
            
            if user.password != user.confirm_password:
                flash('Les mots de passe ne correspondent pas')
                return redirect(url_for('users.edit', userid=userid))
            
            # Hasher le mot de passe avant de le stocker dans la base de données
            hashed_password = generate_password_hash(user.password, method='sha256')
            user.password = hashed_password

            # Valider les modifications dans la base de données
            db.session.commit()
            flash('User updated successfully.')
        else:
            flash('Les mots de passe ne correspondent pas', 'error')
            return redirect(url_for('users.show'))
    # Rediriger vers la page des utilisateurs
    return redirect(url_for('users.show'))


@users.route('/users/add', methods=['POST'])
@login_required
def add():
    # Récupérer les données du formulaire
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('passwordE')
    confirm_password = request.form.get('confirm-password')
    # Vérifier si toutes les informations requises du formulaire sont présentes
    if not username or not email or not password :
        flash('Veuillez remplir tous les champs.')
        return redirect(url_for('users.show'))

    existing_email = Users.query.filter_by(email=email).first()
    if existing_email:
        flash('Email existe déja !')
        return redirect(url_for('users.show'))
    if username and email and password and password == confirm_password:
            if not email.endswith('@dataraise.com'):
                flash('Invalid email!')
                return redirect(url_for('users.show'))
            
            if len(password) < 8:
                flash('The password must be 8 characters or more!')
                return redirect(url_for('users.show'))
            else:
             flash('Les mots de passe ne correspondent pas', 'error')
             return redirect(url_for('users.show'))
            # Hasher le mot de passe avant de le stocker dans la base de données
    hashed_password = generate_password_hash(password, method='sha256')
    password = hashed_password
    
    # Créer un nouvel objet utilisateur
    user = Users(username=username, email=email, password=password)
    
    # Hasher le mot de passe avant de le stocker dans la base de données
    hashed_password = generate_password_hash(password, method='sha256')
    user.password = hashed_password

    # Ajouter le nouvel utilisateur à la base de données
    db.session.add(user)
    db.session.commit()

    flash('User added successfully.')

    # Rediriger vers la page des utilisateurs
    return redirect(url_for('users.show'))
