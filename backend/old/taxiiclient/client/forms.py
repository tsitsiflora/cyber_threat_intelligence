from django import forms
from .models import Indicator

class IndicatorForm(forms.ModelForm):
    
    type = forms.CharField(required=False)
    id = forms.CharField(required=False)
    created = forms.DateTimeField(required=False)
    modified = forms.DateTimeField(required=False)
    valid_from = forms.DateTimeField(required=False)
    
    
    class Meta:
        model = Indicator
        fields = ['type', 'id', 'created', 'modified', 'name', 'pattern', 'valid_from', 'labels']
    