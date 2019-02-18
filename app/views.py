from flask import render_template
from app import app
from .request import get_sources

 

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting sources

    general_sources = get_sources('general')
    business_sources = get_sources('business')
    entertainment_sources = get_sources('entertainment')
    sports_sources = get_sources('sports')


    

    title = 'Home - Welcome to The best News Highlight Online'
    return render_template('index.html', title = title,general = general_sources, business= business_sources,entertainment = entertainment_sources,sports=sports_sources)
    print(general_sources,business_sources,entertainment_sources,sports_sources,)



    

 

# @app.route('/source/<source_id>')
# def source(source_id):

#     '''
#     View news page function that returns the source details page and its data
#     '''
#     return render_template('source.html',id = source_id)


