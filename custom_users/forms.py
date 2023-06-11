from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models


GENDER = (("M", "M"), ("Ж", "Ж"), ("Другой", "Другой"))

LANGUAGE = (
    ("Кыргызча", "Кыргызча"),
    ("Русский", "Русский"),
    ("English", "English"),
)
COUNTY = (
    ("Кыргызстан", "Кыргызстан"),
    ("Россия", "Россия"),
    ("Казахстан", "Казахстан"),
)


class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    avatar = forms.ImageField(required=True)
    language = forms.ChoiceField(choices=LANGUAGE, required=True)
    country = forms.ChoiceField(choices=COUNTY, required=True)
    about_me = forms.CharField(required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            "username",
            "password1",
            "password2",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "age",
            "gender",
            "avatar",
            "language",
            "about_me",
            "country",
        )

    def save(self, commit=True):
        user = super(CustomRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
