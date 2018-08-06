__author__ = 'sachin yadav'
from django import forms

class myData(forms.Form) :
    image = forms.ImageField()
    english = forms.BooleanField(required=False)
    hindi = forms.BooleanField(required=False)



class signup_form(forms.Form):
    Name = forms.CharField()
    FName = forms.CharField()
    LName = forms.CharField()
    Password=forms.CharField(widget=forms.PasswordInput)
    Email = forms.EmailField()

class login_form(forms.Form):

    Email = forms.EmailField()
    Password = forms.CharField(widget=forms.PasswordInput)


class reset_form(forms.Form):

    email = forms.EmailField()

class password(forms.Form):

    new_password = forms.CharField(widget=forms.PasswordInput)
    OTP = forms.IntegerField()

class userprofile_form(forms.Form):

    profile_pic = forms.ImageField()
    birth_day = forms.DateField()
    bio = forms.CharField(max_length=2000)
    mob_no = forms.IntegerField()

