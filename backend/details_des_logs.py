from flask import Blueprint, render_template
from flask_login import LoginManager, login_required, current_user

from models import db, Users

details_des_logs = Blueprint('details_des_logs', __name__, template_folder='../frontend')
login_manager = LoginManager()
login_manager.init_app(details_des_logs)

@details_des_logs.route('/details_des_logs', methods=['GET'])
@login_required
def show():
    return render_template('details_des_logs.html')
