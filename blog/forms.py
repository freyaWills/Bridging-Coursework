from django import forms

from .models import Post #Creating a form for the post model

class PostForm(forms.ModelForm): #PostForm is the name of the form, forms.ModelForm shows it's a model form

    class Meta: #Class that shows which model should be used to create the form
        model = Post
        fields = ('title', 'text',)