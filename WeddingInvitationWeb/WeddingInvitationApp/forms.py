from django import forms
from .models import GuestAttendence

class GuestAttendenceForm(forms.ModelForm):
    class Meta:
        model = GuestAttendence
        fields = ['name', 'surname', 'cell', 'church_attendence', 'home_attendence', 'song_request']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your first name'}),
            'surname': forms.TextInput(attrs={'placeholder': 'Enter your last name'}),
            'cell': forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
            'church_attendence': forms.CheckboxInput(attrs={'title': 'Will you attend the church ceremony?'}),
            'home_attendence': forms.CheckboxInput(attrs={'title': 'Will you attend the home reception?'}),
            'song_request': forms.TextInput(attrs={'placeholder': 'Enter your song request (optional)'}),
        }