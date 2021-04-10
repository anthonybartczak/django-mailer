from django import forms
from mailer.models import EmailModel

class EmailForm(forms.ModelForm):
    class Meta:
        model = EmailModel
        fields = ('address',
                  'title',
                  'content',
                  'image',
                  'hour',
                  'date',)