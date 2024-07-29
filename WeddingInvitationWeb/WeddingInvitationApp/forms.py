from django import forms
from .models import GuestAttendence, GuestsPlusOne

class GuestsPlusOneForm(forms.ModelForm):
    class Meta:
        model = GuestsPlusOne
        fields = ['plus_one_name', 'plus_one_surname', 'plus_one_relation']
        labels = {
            'plus_one_name': 'Plus One Name',
            'plus_one_surname': 'Plus One Surname',
            'plus_one_relation': 'Relation to Plus One'
        }
        widgets = {
            'plus_one_name': forms.TextInput(attrs={'placeholder': 'e.g., Jane'}),
            'plus_one_surname': forms.TextInput(attrs={'placeholder': 'e.g., Smith'}),
            'plus_one_relation': forms.TextInput(attrs={'placeholder': 'e.g., Friend'}),
        }

class GuestAttendenceForm(forms.ModelForm):
    plus_one_name = forms.CharField(max_length=50, required=False, label="Plus One Name")
    plus_one_surname = forms.CharField(max_length=25, required=False, label="Plus One Surname")
    plus_one_relation = forms.CharField(max_length=25, required=False, label="Relation to Plus One")

    class Meta:
        model = GuestAttendence
        fields = ['cell', 'name', 'surname', 'church_attendence', 'home_attendence', 'song_request']
        labels = {
            'cell': 'Cellphone Number',
            'name': 'First Name',
            'surname': 'Last Name',
            'church_attendence': 'Attending Church Ceremony',
            'home_attendence': 'Attending Home Ceremony',
            'song_request': 'Song Request'
        }
        widgets = {
            'cell': forms.TextInput(attrs={'placeholder': 'e.g., 0612345678'}),
            'name': forms.TextInput(attrs={'placeholder': 'e.g., Tshepo Steve'}),
            'surname': forms.TextInput(attrs={'placeholder': 'e.g., Kekana'}),
            'song_request': forms.TextInput(attrs={'placeholder': 'e.g., Your favorite song'}),
        }
