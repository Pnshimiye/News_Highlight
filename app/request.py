from app import app
import urllib.request,json
from .models import source

source = source.Source

#Getting api key
api_key = app.config['SOURCE_API_KEY']


#Getting the source base url
base_url = app.config["SOURCE_API_BASE_URL"]


def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

 

      
        sources_results = None

        if get_sources_response['results']:
           sources_results_list = get_sources_response['results']
           sources_results = process_results(sources_results_list)


    return sources_results



def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
         source_list: A list of dictionaries that contain source details

    Returns :
         source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        category = source_item.get('category')
       

        if  name:
            source_object = Source(id,name,description,category)
            source_results.append(source_object)

    return source_results