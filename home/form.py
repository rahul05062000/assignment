from django import forms
from .models import bill
from django.forms import ModelForm


class billForm(ModelForm):
    class Meta:
        model=bill
        fields=('s_no','item_quantity')
        labels={
            's_no':'',
            'item_quantity':'',
            }
        widgets = {
             's_no': forms.TextInput(attrs={'class': 'form-control'}),
             'item_quantity': forms.TextInput(attrs={'class': 'form-control'}),       
        }    