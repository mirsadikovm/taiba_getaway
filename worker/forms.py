from django import forms


class LoginForm(forms.Form):

    uid = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

