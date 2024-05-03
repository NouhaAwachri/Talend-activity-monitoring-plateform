from flask import Blueprint, render_template
from flask_login import LoginManager, login_required, current_user
from flask import Flask, request, render_template
from flask_cors import cross_origin
from models import db, Users
import joblib

prediction = Blueprint('prediction', __name__, template_folder='../frontend')
login_manager = LoginManager()
login_manager.init_app(prediction)
model = joblib.load(open("prédiction_Statut.joblib", "rb"))
@prediction.route('/prediction', methods=['GET'])
@login_required
def show():
    return render_template('prediction.html')


@prediction.route("/predict", methods=["POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        
        Version = float(request.form["versions"])
        Duration = int(request.form["duration"])
        Frequence= int(request.form["frequence"])
        Context = str(request.form["context"])
        if(Context=="default" or "Default"):
            Context=0
        else:
            Context=1    

        prediction = model.predict([[Duration,Version,Frequence,Context]])
        output = prediction[0]
        return render_template('prediction.html', prediction_text=format(output))
    return render_template("prediction.html")