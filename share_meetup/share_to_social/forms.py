from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class UserForm(ModelForm):

	email = forms.EmailField(widget=forms.TextInput, label='Email')
	password = forms.CharField(widget=forms.PasswordInput, label='Password')

	class Meta:
		model = User
		fields = ['username', 'email', 'password']
