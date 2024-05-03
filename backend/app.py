
from flask import Flask, url_for

from flask import Flask
from flask_login import LoginManager
from models import db, Users
from index import index
from login import login
from logout import logout
from register import register
from home import home
from prediction import prediction
from prediction_flux import prediction_flux
from dashboard_execution import dashboard_execution
from details_execution import details_execution
from dashboard_volumetrie import dashboard_volumetrie
from details_volumetrie import details_volumetrie
from dashboard_log import dashboard_log
from details_logs import details_logs
from details_des_logs import details_des_logs
from overview import overview
from users import users
from access_denied import access_denied

app = Flask(__name__, static_folder='../frontend')
app.secret_key = '1a2b3c4d5e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:stagePFE2023@localhost/activity_monitoring_database'



# Initialize Flask-Mail
login_manager = LoginManager()
login_manager.init_app(app)
db.init_app(app)
app.app_context().push()

app.register_blueprint(index)
app.register_blueprint(login)
app.register_blueprint(logout)
app.register_blueprint(register)
app.register_blueprint(home)
app.register_blueprint(prediction)
app.register_blueprint(prediction_flux)
app.register_blueprint(dashboard_execution)
app.register_blueprint(details_execution)
app.register_blueprint(dashboard_volumetrie)
app.register_blueprint(details_volumetrie)
app.register_blueprint(dashboard_log)
app.register_blueprint(details_logs)
app.register_blueprint(details_des_logs)
app.register_blueprint(overview)
app.register_blueprint(users)
app.register_blueprint(access_denied)


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

