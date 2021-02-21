from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class ProfileForm(UserCreationForm):
    UNIS = (
            ("USYD", "The University of Sydney"),
            ("UNSW", "University of New South Wales"),
            ("Monash", "Monash University"),
        )

    uni = forms.ChoiceField(choices=UNIS)
    email = forms.EmailField()

    class Meta:
        model = User 
        fields = ("username","email","uni","password1","password2")