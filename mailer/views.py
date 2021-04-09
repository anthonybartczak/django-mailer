from django.http import HttpResponse
from django.shortcuts import render
from django import forms


class Form(forms.Form):
    address = forms.CharField()
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    hour = forms.CharField()
    date = forms.DateField()
    

def index(request):
    return render(request, 'views/index.html')

def success(request):
    return render(request, 'views/success.html')