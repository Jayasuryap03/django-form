from django import forms
from .models import UserData

class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['name', 'email', 'phone_number', 'address', 'gender', 'date_of_birth', 'about_me', 'photo']

    # Add client-side email validation using JavaScript
    def __init__(self, *args, **kwargs):
        super(UserDataForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['oninput'] = 'validateEmail()'
