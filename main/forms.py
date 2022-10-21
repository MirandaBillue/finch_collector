from django.forms import ModelForm
from .models import Lifestyle

class LifestyleForm(ModelForm):

  class Meta:
    model = Lifestyle
    fields = ['migrates', 'lifestyle']
