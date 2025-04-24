from flask import Blueprint, render_template, redirect, url_for, flash
from app import db
from app.model import User
from app.form import LoginForm

bp = Blueprint('routes', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data, message=form.message.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for your message!')
        return redirect(url_for('routes.index'))
    return render_template('index.html', form=form)
    