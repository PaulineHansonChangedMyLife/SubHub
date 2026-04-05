from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import createbudgetform, editbudgetform
from django.shortcuts import get_object_or_404
from .models import Profile

def login_view(request):
    if request.user.is_authenticated:
        return redirect('subhub:home')
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', reverse("subhub:home"))
            messages.success(request, f"Successfully signed in as {username}.") # Sign in success message added, this brings parity to allauth libary included success message
            return HttpResponseRedirect(next_url)
        else:
            messages.error(request, "Invalid Credentials.")
    return render(request, "users/login.html", {"current_app": "users"})

def logout_view(request):
    logout(request)
    messages.success(request, "Successfully logged out.")
    return redirect('users:login')

@login_required
def create_budget(request):
    if request.method == 'POST':
        form = createbudgetform(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['balance']
            profile = request.user.profile
            profile.balance = amount
            profile.save()
            messages.success(request, "Your budget has been created!")
            return redirect('subhub:home')
    else: # This is the GET request
        form = createbudgetform() # Create a blank form
    return render(request, 'users/create-budget.html', {'form': form, "current_app": "createbudget"}) # Send the blank form to the template

@login_required
def edit_budget(request):
    if request.method == 'POST':
        form = editbudgetform(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['balance']
            profile = request.user.profile
            profile.balance = amount
            profile.save()
            messages.success(request, "Your budget has been successfully edited!")
            return redirect('subhub:home')
    else: # This is the GET request
        form = editbudgetform()#instance=request.user.profilebalance)#initial={'balance': request.user.profile.balance}) # Initial causes the form to have the 'initial' field contain the pre-existing balance amount
    return render(request, 'users/edit-budget.html', {'form': form, "current_app": "editbudget"}) # Send the blank form to the template