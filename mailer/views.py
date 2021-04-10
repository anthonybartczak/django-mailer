from django.shortcuts import render, redirect
from .forms import EmailForm
from .models import EmailModel
from django.contrib.auth import authenticate

def index(request):
    if request.user.is_authenticated:
        mails = EmailModel.objects.filter(user_id=request.user)
        return render(request, 'views/index.html', {'mails': mails})
    return render(request, 'views/index.html')

def success(response):
    if response.method == "POST":
        form = EmailForm(response.POST, response.FILES)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = response.user
            form.save()
            return render(response, "views/success.html")
            
    else:
        form = EmailForm()

    return render(response, "views/index.html", {"form":form})