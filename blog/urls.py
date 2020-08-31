from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_page, name='welcome_page'),
    path('cv/edit/', views.cv_edit, name='cv_edit'),
    path('cv/view/', views.cv_view, name='cv_view'),
    path('post/posts/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]