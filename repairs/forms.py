from django import forms
from .models import RepairWork

class RepairWorkForm(forms.ModelForm):
    class Meta:
        model = RepairWork
        fields = ['title', 'description']