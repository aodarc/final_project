from django import forms

from apps.location.models import City
from apps.user_profile.models import Child
from django.db import models


class RegisterChildForm(forms.ModelForm):
        class Meta:
            model = Child
            #fields = '__all__'
            exclude = ['parents', 'privilege', 'privilege_series', 'privilege_number']
