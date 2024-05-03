from flask import Blueprint, render_template
from flask_login import LoginManager, login_required, current_user

from models import db, Users

details_logs = Blueprint('details_logs', __name__, template_folder='../frontend')
login_manager = LoginManager()
login_manager.init_app(details_logs)

@details_logs.route('/details_logs', methods=['GET'])
@login_required
def show():
    return render_template('details_logs.html')
