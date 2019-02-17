import unittest
from models import articles
Article = articles.Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('Fox News''Pauline','Python ','Python is getting Crazy','http://www.abc.net.au/news/2019-02-16/eight-vale-sa-employees-arrested-over-deadly-brazil-dam-collapse/10818196','https://www.python.org/download/other/','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQz3kgLAKC-0TnddU-w0bcF0eveIHmQZCnTPTXCT4Pu748xk3rOYQ' ,'2019-02-15T09:35:16Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

    def test_init(self)
        '''
        test case  to test if the Articles object is being properly instantiated
        '''
        self.assertEqual(self.new_article.source,"Fox News")
        self.assertEqual(self.new_article.author,"Pauline")
        self.assertEqual(self.new_article.title,"Python")
        self.assertEqual(self.new_article.description,'Python is getting Crazy')
        self.assertEqual(self.new_article.source,"Fox News")
if __name__ == '__main__':
    unittest.main()