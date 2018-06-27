from django import forms

class login(forms.Form) :

    Name = forms.CharField(max_length=100)
    Password = forms.CharField(max_length=100,widget=forms.PasswordInput)

class signup(forms.Form):
    Name = forms.CharField(max_length=100)
    First_Name = forms.CharField(max_length=100)
    Last_Name = forms.CharField(max_length=100)
    Email = forms.EmailField(widget=forms.EmailInput)
    Password = forms.CharField(max_length=100,widget=forms.PasswordInput)

class reset_form(forms.Form):
    email = forms.EmailField()



