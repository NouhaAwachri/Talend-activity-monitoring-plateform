from flask import Blueprint, render_template
from flask_login import LoginManager, login_required, current_user

from models import db, Users

details_execution = Blueprint('details_execution', __name__, template_folder='../frontend')
login_manager = LoginManager()
login_manager.init_app(details_execution)

@details_execution.route('/details_execution', methods=['GET'])
@login_required
def show():
    return render_template('details_execution.html')
