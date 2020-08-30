from django import forms

from .models import Post #Creating a form for the post model
from .models import Item
from django.utils.translation import ugettext_lazy as _

class PostForm(forms.ModelForm): #PostForm is the name of the form, forms.ModelForm shows it's a model form

    class Meta: #Class that shows which model should be used to create the form
        model = Post
        fields = ('title', 'text',)

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('company','role','startDate','endDate','text')
        labels = {
            'company': _('Company Name'),
            'role': _('Job Title'),
            'startDate': _('Start Date'),
            'endDate': _('End Date'),
            'text': _('Additional Information'),
        }