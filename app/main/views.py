from flask import render_template

from . import main
from ..requests import get_articles,get_sources

# Views 
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular sources
    sports_sources = get_sources('sports')
    health_sources = get_sources('health')
    technology_sources = get_sources('technology')

    title = 'News Highlights'

    return render_template('index.html', title = title, sports_sources = sports_sources, health_sources = health_sources, technology_sources = technology_sources )

@main.route('/articles/<id>')
def articles(id):
    '''
    View source page function that returns the source details page and its data
    '''
    articles = get_articles(id)
    title = f'NH{id}'

    return render_template('articles.html',title = title, articles = articles)