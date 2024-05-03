from flask import Blueprint, render_template
from flask_login import LoginManager, login_required, current_user

from models import db, Users

dashboard_execution= Blueprint('dashboard_execution', __name__, template_folder='../frontend')
login_manager = LoginManager()
login_manager.init_app(dashboard_execution)

@dashboard_execution.route('/dashboard_execution', methods=['GET'])
@login_required
def show():
    return render_template('dashboard_execution.html')
