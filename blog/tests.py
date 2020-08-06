from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

#from django.http import HttpResponse
#from django.template.loader import render_to_string

from blog.views import welcome_page  

class WelcomePageTest(TestCase):

    def test_uses_welcome_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/welcome_page.html')

    """def test_welcome_page_returns_correct_html(self):
        response = self.client.get('/')
        html = response.content.decode('utf8')
        self.assertTrue(html.strip().startswith('<html>'))
        self.assertIn("<title>Freya's Blog</title>", html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'blog/welcome_page.html')"""