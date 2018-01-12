from django import forms


class LoginFormMap(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
