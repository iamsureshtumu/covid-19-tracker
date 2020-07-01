from app.models import *
from django import forms
class User_Form(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username',"email",'password')
        
class User_data_form(forms.ModelForm):
    class Meta:
        model=User_data
        # fields=('webpage',"profile_pic")
        fields=("profile_pic",)