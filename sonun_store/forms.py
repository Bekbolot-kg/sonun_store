from django import forms
from . import models


class StoreForm(forms.ModelForm):

    class Meta:
        model = models.Sonun_Store
        fields = '__all__'
        # fields = 'name image ...'

class ReviewForm(forms.ModelForm):

    class Meta:
        model = models.Reviews
        fields = ('__all__')