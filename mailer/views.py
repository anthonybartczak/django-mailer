from django.shortcuts import render, redirect
from .forms import EmailForm
from .models import EmailModel
from django.contrib.auth import authenticate
from .send_mail import mailgun_init

def index(request):
    #mailgun_init()
    if request.user.is_authenticated:
        mails = EmailModel.objects.filter(user_id=request.user)
        return render(request, 'views/index.html', {'mails': mails})
    return render(request, 'views/index.html')

def your_emails(request):
    if request.user.is_authenticated:
        mails = EmailModel.objects.filter(user_id=request.user)
        return render(request, 'views/your-emails.html', {'mails': mails})
    return redirect("index")

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