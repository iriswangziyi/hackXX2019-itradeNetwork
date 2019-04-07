# FLASK_APP=backend.py flask run
from flask import Flask, render_template, flash, redirect
import pandas as pd
import os

from model import model, enc

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    category_name = StringField('Category Name', validators=[DataRequired()], default="White Cabbages")
    vendor_name  = StringField('Vendor Name', validators=[DataRequired()], default="Vendor  63b9d36c")
    shipping_warehouse  = StringField('Shipping Warehouse', validators=[DataRequired()], default="Warehouse  e5847f7c")
    inspector  = StringField('Inspector', validators=[DataRequired()], default="Inspector  4bb23bf2")
    shipping_time  = StringField('Shipping Duration (days)', validators=[DataRequired()], default=3)
    seasons  = SelectField('Season when shipped', choices=[("spring","spring"), ("summer","summer"), ("fall","fall"), ("winter","winter")], default="spring", validators=[DataRequired()])

    submit = SubmitField('Send')

app = Flask(__name__)
app.config.from_object(Config)

# @app.route("/")
# def hello():
#     return "Hello World!"

@app.route('/', methods=['GET', 'POST'])
def main_form():
    form = LoginForm()
    if form.validate_on_submit():
        row = { "Category Name": form.category_name.data, \
                "Vendor Name": form.vendor_name.data, \
                "Shipping Warehouse": form.shipping_warehouse.data, \
                "Inspector": form.inspector.data, \
                "Shipping Time": form.shipping_time.data, \
                "Season": form.seasons.data }
        row = pd.DataFrame({k: [v] for k, v in row.items()})
        row_one_hot = enc.transform(row)
        result = model.predict(row_one_hot)
        print(row_one_hot)
        print(result)
        # flash a string
        flash(str(result[0]))
        return redirect('/')
    return render_template('form.html', title='Sign In', form=form)

if __name__ == '__main__':
    app.run()