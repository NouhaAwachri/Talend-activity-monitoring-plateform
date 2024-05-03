from flask import Blueprint, render_template
from flask_login import LoginManager, login_required, current_user

from models import db, Users

overview = Blueprint('overview', __name__, template_folder='../frontend')
login_manager = LoginManager()
login_manager.init_app(overview)

@overview.route('/overview', methods=['GET'])
@login_required
def show():
    return render_template('overview.html')
