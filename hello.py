from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, EmailField
from wtforms.validators import DataRequired, Email
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'IcaNnOTCoMeUpWiThSoMeThInGbEtTeR1'

bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(FlaskForm):
    name = StringField('What is your name?' , validators=[DataRequired()])
    email = EmailField('What is your UofT Email Address?' , validators = [DataRequired() , Email() ])
    submit = SubmitField('Submit')

@app.route('/', methods =['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        old_email = session.get('email')
        if old_name != None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        if old_email != None and old_email != form.email.data:
            flash('Looks like you have changed your email!')
        session['name'] = form.name.data
        session['email'] = form.email.data
        return redirect(url_for('index'))
    return render_template('index.html' , form = form , name = session.get('name'), email = session.get('email'))


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)