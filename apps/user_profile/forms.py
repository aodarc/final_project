from django import forms
from django.contrib.auth.models import User

from apps.location.models import City
from apps.user_profile.models import Child
from django.db import models


class RegisterChildForm(forms.ModelForm):
    parents = forms.ModelChoiceField(queryset=User.objects.all(), required=False)
    class Meta:
            model = Child
            #fields = '__all__'
            exclude = ['privilege', 'privilege_series', 'privilege_number']

