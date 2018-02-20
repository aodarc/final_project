from django import forms

from apps.kindergarten.models import Kindergarten
from apps.user_profile.models import Child


class RegisterChild(forms.Form):
    kindergarten = forms.ModelChoiceField(
        queryset=Kindergarten.objects.all(),
        required=True,
        widget=forms.HiddenInput()
    )

    child = forms.ModelChoiceField(
        queryset=Child.objects.all(),
        required=True
    )
