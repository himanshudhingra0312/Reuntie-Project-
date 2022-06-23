from django import forms
from .models import User

class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=20,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=20,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['first_name','last_name']


