from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

#from django.http import HttpResponse
#from django.template.loader import render_to_string

from blog.views import welcome_page  
from blog.models import Item

class WelcomePageTest(TestCase):

    def test_uses_welcome_template(self):
        response = self.client.get('/cv/edit/')
        self.assertTemplateUsed(response, 'blog/cv_edit.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/cv/edit/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'blog/cv_edit.html')

    """def test_welcome_page_returns_correct_html(self):
        response = self.client.get('/')
        html = response.content.decode('utf8')
        self.assertTrue(html.strip().startswith('<html>'))
        self.assertIn("<title>Freya's Blog</title>", html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'blog/welcome_page.html')"""

class ItemModelTest(TestCase):
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
        self.assertEqual(second_saved_item.text, 'Second item')