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


@app.route('/check/<check_id>')
def check_details(check_id):
    check_mapping = {
        '1': [
            ('Проверка документа 1 по критерию 1', True),
            ('Проверка документа 1 по критерию 2', True),
            ('Проверка документа 1 по критерию 3', False),
            ('Проверка документа 1 по критерию 4', False),
            ('Проверка документа 1 по критерию 5', True),
        ],
        '2': [
            ('Проверка документа 2 по критерию 1', True),
            ('Проверка документа 2 по критерию 2', True),
            ('Проверка документа 2 по критерию 3', False),
            ('Проверка документа 2 по критерию 4', False),
            ('Проверка документа 2 по критерию 5', True),
        ],
        '3': [
            ('Проверка документа 3 по критерию 1', True),
            ('Проверка документа 3 по критерию 2', True),
            ('Проверка документа 3 по критерию 3', False),
            ('Проверка документа 3 по критерию 4', False),
            ('Проверка документа 3 по критерию 5', True),
        ],
        '4': [
            ('Проверка документа 4 по критерию 1', True),
            ('Проверка документа 4 по критерию 2', True),
            ('Проверка документа 4 по критерию 3', False),
            ('Проверка документа 4 по критерию 4', False),
            ('Проверка документа 4 по критерию 5', True),
        ],
        '5': [
            ('Проверка документа 5 по критерию 1', True),
            ('Проверка документа 5 по критерию 2', True),
            ('Проверка документа 5 по критерию 3', False),
            ('Проверка документа 5 по критерию 4', False),
            ('Проверка документа 5 по критерию 5', True),
        ],
    }

    return render_template('check-details.html', check=check_mapping[check_id])


@app.route('/check/new')
def new_check():
    added_check = [
        'Новая проверка 1',
        'Новая проверка 2',
        'Новая проверка 3',
        'Новая проверка 4',
        'Новая проверка 5',
    ]
    return render_template('new-check.html', added_check=added_check)


@app.route('/documents')
def documents():
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
