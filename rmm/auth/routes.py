from datetime import datetime
from flask import abort
from rmm.auth.forms import RegistrationForm, LoginForm, EditProfileForm
from flask import (
    flash, redirect, render_template, request, url_for
)
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from rmm import db
from rmm.models import User
from rmm.auth import bp


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now registered.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title='Register', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password.')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(url_for('main.index'))
    return render_template('auth/login.html', title='Login', form=form)


@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@login_required
@bp.route('/profile/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('auth/profile.html', user=user)


@login_required
@bp.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    form = EditProfileForm(current_user.username, current_user.email)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.experience = form.experience.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('auth.edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.experience.data = current_user.experience
        form.email.data = current_user.email
    return render_template('auth/edit_profile.html',
                           title='Edit Profile',
                           form=form)


@login_required
@bp.route('/history/<page>')
def history(page):
    try:
        page = int(page)
    except:
        abort(404)
    pg_length = 100
    last_page = 1 if int(len(current_user.scores)/100) == 0 \
        else int(len(current_user.scores)/pg_length)+1
    scores = sorted(current_user.scores, key=lambda score: score.sco,
                    reverse=True)
    scores = scores[(page-1)*pg_length:(page-1)*pg_length+pg_length]
    return render_template('auth/history.html', page=page, scores=scores,
                           last_page=last_page)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
