from flask import render_template
from app import app

 

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to The best News Highlight Online'
    return render_template('index.html', title = title)

 

@app.route('/article/<int:article_id>')
def article(article_id):

    '''
    View news page function that returns the article details page and its data
    '''
    return render_template('article.html',id = article_id)