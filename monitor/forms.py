from django import forms
from .models import LogEntry

class LogEntryForm(forms.ModelForm):
    class Meta:
        model = LogEntry
        fields = ['sender', 'receiver', 'message']
        widgets = {
            'sender': forms.Select(attrs={'class': 'form-control'}),
            'receiver': forms.Select(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def clean(self):
        cleaned_data = super().clean()
        sender = cleaned_data.get("sender")
        receiver = cleaned_data.get("receiver")
        if sender == receiver:
            raise forms.ValidationError("El sensor emisor y receptor no pueden ser el mismo.")
        return cleaned_data
