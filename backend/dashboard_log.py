from flask import Blueprint, render_template
from flask_login import LoginManager, login_required, current_user

from models import db, Users

dashboard_log= Blueprint('dashboard_log', __name__, template_folder='../frontend')
login_manager = LoginManager()
login_manager.init_app(dashboard_log)

@dashboard_log.route('/dashboard_log', methods=['GET'])
@login_required
def show():
    return render_template('dashboard_log.html')
