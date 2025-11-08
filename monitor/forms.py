from django import forms
from .models import LogEntry

class LogEntryForm(forms.ModelForm):
    class Meta:
        model = LogEntry
        fields = ['device', 'message']
        widgets = {
            'device': forms.Select(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
