from flask import render_template
from app import app
from .request import get_sources

 

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting general sources
    general_sources = get_sources('general')
    print(general_sources)

    title = 'Home - Welcome to The best News Highlight Online'
    return render_template('index.html', title = title)

    

 

@app.route('/source/<int:source_id>')
def source(source_id):

    '''
    View news page function that returns the source details page and its data
    '''
    return render_template('source.html',id = source_id)


