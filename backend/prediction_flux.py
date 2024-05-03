from flask import Blueprint, render_template
from flask_login import LoginManager, login_required, current_user
from flask import Flask, request, render_template
from flask_cors import cross_origin
from models import db, Users
import joblib

from models import db, Users

prediction_flux = Blueprint('prédiction_flux', __name__, template_folder='../frontend')
login_manager = LoginManager()
login_manager.init_app(prediction_flux)
modelFlow = joblib.load(open("prediction_Flux.joblib", "rb"))
@prediction_flux.route('/prédiction_flux', methods=['GET'])
@login_required
def show():
    return render_template('prédiction_flux.html')



@prediction_flux.route("/predict_flux", methods=["POST"])
@cross_origin()
def predictFlow():
    if request.method == "POST":
        Version = float(request.form["versions"])
        Context = str(request.form["context"])
        Duration = int(request.form["duration"])

        if Context.lower() == "default":
            Context = 0
        else:
            Context = 1    

        predictionFlow = modelFlow.predict([[Version, Context, Duration]])
        outputFlow = predictionFlow[0].round().astype(int)

        return render_template('prédiction_flux.html', prediction_text_Flow=format(outputFlow))

    return render_template("prédiction_flux.html")