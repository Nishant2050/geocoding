from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    title = forms.CharField(max_length=30, required = True)
    docfile = forms.FileField(required = True)

    class Meta:
        model = Document
        fields = ('title', 'docfile',)

