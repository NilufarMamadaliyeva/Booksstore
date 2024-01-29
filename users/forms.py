from .models import CustomUser
# from django.forms import Form
from django.forms import ModelForm
from django import forms


# class CUstomUserCreateForm(forms.Form):
#   username = forms.CharField(max_lenght = 120)

class CustomUserCreateForm(ModelForm):
  class Meta:
    model = CustomUser
    fields = ['username', 'first_name', 'last_name', 'password', 'image_user']
    
    
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email','phone_number','image_user')
