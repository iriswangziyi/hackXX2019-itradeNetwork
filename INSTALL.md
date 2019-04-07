# Installation/Running

Install required libraries

    pip install flask flask-wtf imbalanced-learn

Calculate features from "LAHacks Deidentified.csv"

    python features.py

Run app (fit model, etc)

    FLASK_APP=backend.py flask run

Go to <http://127.0.0.1:5000/> to view
