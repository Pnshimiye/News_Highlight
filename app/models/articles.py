class Article:
    '''
     Article class to define article  Objects
    '''

    def __init__(self,source,title,description,url,urlToImage,publishedAt):

         
        self.source = source
        self.title = title
        self.description = description
        self.url= url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        