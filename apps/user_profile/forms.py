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
from apps.user_profile.models import Child


class RegisterChildForm(forms.ModelForm):
    class Meta:
        model = Child
        # fields = '__all__'
        exclude = ['privilege', 'privilege_series', 'privilege_number']

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            self.fields['parents'].initial = user
