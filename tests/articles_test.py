import unittest
from app.models import Articles

class articlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_articles = articles()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles,articles))
