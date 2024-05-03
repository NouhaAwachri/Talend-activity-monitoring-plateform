from flask import Blueprint, render_template
from flask_login import LoginManager, login_required, current_user

from models import db, Users

details_volumetrie = Blueprint('details_volumetrie', __name__, template_folder='../frontend')
login_manager = LoginManager()
login_manager.init_app(details_volumetrie)

@details_volumetrie.route('/details_volumetrie', methods=['GET'])
@login_required
def show():
    return render_template('details_volumetrie.html')
