__author__ = 'sachin yadav'
from django import forms

class signup_form(forms.Form):

    name = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

class login_form(forms.Form):

    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class reset_form(forms.Form):

    email = forms.EmailField()

class password(forms.Form):

    new_password = forms.CharField(widget=forms.PasswordInput)
    OTP = forms.IntegerField()

