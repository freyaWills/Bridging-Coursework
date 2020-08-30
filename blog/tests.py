from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
import datetime

#from django.http import HttpResponse
#from django.template.loader import render_to_string

from blog.views import welcome_page  
from blog.views import cv_edit
from blog.models import Item

"""class WelcomePageTest(TestCase):

    def test_uses_welcome_template(self):
        response = self.client.get('/cv/edit/')
        self.assertTemplateUsed(response, 'blog/cv_edit.html')

    def test_can_save_a_POST_request(self):
        self.client.post('/cv/edit/', data={'company': "Tesco", 'role': "Manager", 'text': 'Worked in a shop'})
        #self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        #self.assertEqual(new_item.text, 'Worked in a shop')

    def test_redirects_after_POST(self):
        response = self.client.post('/cv/edit/', data={'company': "Tesco", 'role': "Manager", 'text': "Worked in a shop"})
        #self.assertEqual(response.status_code, 302)
        #self.assertEqual(response['location'],'/')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/cv/edit/')
        #self.assertEqual(Item.objects.count(), 0)

    def test_displays_all_list_items(self):
        Item.objects.create(company='Tesco', role='cashier', text='Worked in a shop')
        Item.objects.create(company='Waitrose', role='Manager', text='Worked in another shop')

        response = self.client.get('/cv/edit/')

        self.assertIn('Tesco', response.content.decode())
        self.assertIn('Waitrose', response.content.decode())"""

"""class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Second item'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Second item')"""