from django.shortcuts import render
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from .forms import UserRegisterForm,UserLoginForm

def register(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/login')
    context = {
		'form': form
	}
    return render(request, "inventoryapp/register.html", context)


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        user_obj = form.cleaned_data.get('user_obj')
        login(request, user_obj)
        return HttpResponseRedirect("/")
    return render(request, "registration/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return render(request,"registration/logout.html")