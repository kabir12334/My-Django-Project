from django import forms
from movieapp.models import Movie

class MovieForm(forms.Form):
    class Meta:
            model =Movie
            fields ='__all__'
