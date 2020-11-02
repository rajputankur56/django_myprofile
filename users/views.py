from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.urls import reverse
from users.forms import CustomUserCreationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
    return render(request,"users/dashboard.html")

def register(request):
    import os
    print(os.environ.get("SOCIAL_AUTH_GITHUB_KEY"))
    if request.method == "GET":
        return render(request,"users/register.html",{'form' : CustomUserCreationForm()})
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = "djnago.contrib.admin.backends.ModelBackend"
            user.save()
            login(request,user)
            return redirect(reverse("login"))
    
    return HttpResponse("Hello not valid request")


from django.contrib import messages

@login_required
def add_messages(request):
    username = request.user.username
    messages.add_message(request, messages.INFO, f"Hello {username}")
    messages.add_message(request, messages.WARNING, "DANGER WILL ROBINSON")

    return HttpResponse("Messages added", content_type="text/plain")