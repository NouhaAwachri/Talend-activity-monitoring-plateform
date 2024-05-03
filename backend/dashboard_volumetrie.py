from flask import Blueprint, render_template
from flask_login import LoginManager, login_required, current_user

from models import db, Users

dashboard_volumetrie= Blueprint('dashboard_volumetrie', __name__, template_folder='../frontend')
login_manager = LoginManager()
login_manager.init_app(dashboard_volumetrie)

@dashboard_volumetrie.route('/dashboard_volumetrie', methods=['GET'])
@login_required
def show():
    return render_template('dashboard_volumetrie.html')
