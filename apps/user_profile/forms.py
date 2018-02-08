from django import forms
from apps.user_profile.models import Child


class RegisterChildForm(forms.ModelForm):
        class Meta:
            model = Child
            fields = ('__all__')
