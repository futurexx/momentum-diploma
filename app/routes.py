from flask import render_template, redirect, url_for
from app import app


@app.route('/')
def index():
    return redirect(url_for('check'))


@app.route('/check')
def check():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('check.html', title='Home', user=user, posts=posts)


@app.route('/documents')
def documents():

    return render_template('documents.html', title='Home', user=user, posts=posts)


@app.route('/staff')
def staff():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('staff.html', title='Home', user=user, posts=posts)


@app.route('/partners')
def partners():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('partners.html', title='Home', user=user, posts=posts)


@app.route('/login')
def login():
    return "Log In!"


@app.route('/logout')
def logout():
    return 'Log Out!'
