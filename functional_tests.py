from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
import unittest
from django.test import TestCase
from blog.models import Item

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()
        #self.entry = Item.objects.create(company = "Tesco", role = "Manager", startDate = datetime.datetime(2020,5,17), endDate = datetime.datetime(2020,6,25), text = "Worked in a shop")

    def tearDown(self):  
        self.browser.quit()

    """def create_item(self, company, role, startDate, endDate, text):
        return Item.objects.create(company=company, role=role, startDate=startDate, endDate=endDate, text=text)"""

    def test_entering_data_accepted_and_saved(self):
        form_data = {"comapany" : "Tesco", "role" : "Manager", "startDate" : datetime.datetime(2020, 5, 17), "endDate" : datetime.datetime(2020, 6, 25), "text" : "Worked in a shop"}
        form = Item(data=form_data)
        self.assertTrue(form.is_valid())

    """def test_entering_data_accepted_and_saved(self):
        form = create_item(self, "Tesco", "Manager", datetime.datetime(2020, 5, 17), datetime.datetime(2020, 6, 25), "Worked in a shop")
        self.assertTrue(form.is_valid())"""

    """def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])"""

    """def test_can_start_a_list_and_retrieve_it_later(self):  
        self.browser.get('http://127.0.0.1:8000/cv/edit')

        self.assertIn("Freya's Blog", self.browser.title)  
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('Freya', header_text)

        inputbox = self.browser.find_element_by_tag_name
        inputbox = self.browser.find_element_by_id('id_new_item')  
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter new experience'
        )

        inputbox.send_keys('Buy peacock feathers')  
        inputbox.send_keys(Keys.ENTER)  
        time.sleep(1)

        self.check_for_row_in_list_table('1: Buy peacock feathers')

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('27: Use peacock feathers to make a fly')"""


if __name__ == '__main__':  
    unittest.main(warnings='ignore') 

