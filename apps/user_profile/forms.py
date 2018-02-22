from django import forms

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
