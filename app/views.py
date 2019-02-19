from flask import render_template
from app import app
from .request import get_sources, get_article
  

 

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
    








@app.route('/article/<id>')
def article(id):

    '''
    View article page function that returns the article details page and its data
    '''
    articles = get_article(id)

    return render_template('article.html',articles = articles)



# @app.route('/sources/<id>')
    

 

# #from .request import get_movies

# # @app.route('/')
# # def index():

# #     '''
# #     View root page function that returns the index page and its data
# #     '''

# #     # Getting popular movie
# #     popular_movies = get_movies('popular')
# #     print(popular_movies)
# #     title = 'Home - Welcome to The best Movie Review Website Online'
# #     return render_template('index.html', title = title,popular = popular_movies)