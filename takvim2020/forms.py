from django import forms
from  django.forms import ImageField
from .models import  siparis


class SiparisForm(forms.Form):
    class Meta:
        model = siparis
        fields = ['design1','design2']
