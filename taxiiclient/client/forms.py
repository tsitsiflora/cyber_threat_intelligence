from django import forms

from .models import Indicator

class IndicatorForm(forms.ModelForm):

    class Meta:
        model = Indicator
        fields = ('name', 'pattern','labels')
