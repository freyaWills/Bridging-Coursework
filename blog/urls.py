from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), #post_list is name of the URL to identify the view
]