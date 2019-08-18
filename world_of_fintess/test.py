from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from django.test import TestCase
import unittest


#class NewVisitorTest(unittest.TestCase): 
    #def setUp(self): 
        #self.browser = webdriver.Chrome(ChromeDriverManager().install())
       # self.browser.implicitly_wait(3)
    
    #def tearDown(self): 
        #self.browser.quit()
    
    #def test_start(self): 
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        #self.browser.get('http://localhost:8080')
    
        # She notices the page title and header mention to-do lists
        #self.assertIn('Fitness World', self.browser.title) 
        #self.fail('Finish the test!') 
        
    #def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        #self.browser.get('http://localhost:8080')
        # She notices the page title and header mention to-do lists
       # self.assertIn('Fitness World', self.browser.title)
       # header_text = self.browser.find_element_by_tag_name('h1').text
        #self.assertIn('Fitness World', header_text)
        # She is invited to enter a to-do item straight away
        #inputbox = self.browser.find_element_by_id('id_new_item')
        
       # self.assertIn('Fitness world', self.browser.title)
        #header_text = self.browser.find_element_by_tag_name('h1').text
        #self.assertIn('Fitness world', header_text)
    