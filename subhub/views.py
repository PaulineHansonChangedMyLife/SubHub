from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Subscription
from .forms import addsubscriptionform






from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='users:login')
def home(request):
    current_app = "subhub"
    subscriptions = Subscription.objects.filter(
        user=request.user
    ).order_by('-due_date')

    context = {        # Context system means less clutter in the return render
        'current_app' : current_app,
        'subscriptions' : subscriptions,
    }
    return render(request, "subhub/home.html", context) # Current app added to return so we can determine what page we are on

@login_required
def signinmessage():
    return 


@login_required
def add_subscription(request):
    if request.method == "POST":
        form = addsubscriptionform(request.POST)
        if form.is_valid():
            subscription = form.save(commit=False) # The false commit means we save the form but do not update the database yet. This allows us to add in the User id afterwards.
            subscription.user = request.user
            subscription.save()
            messages.success(request, "Your subscription has been successfully added!")
            return redirect('subhub:home')
    else:
        form = addsubscriptionform()
    return render(request, "subhub/home.html", {"form": form, "current_app": "addsub"})
             # CHANGE RENDER TO add-subscription.html when I want more customisation

def edit_subscription(request, subscription_id):
    subscription = get_object_or_404(Subscription, id=subscription_id)
    if subscription.user != request.user:  # Ensure only the subscription owner can edit
        return redirect('subhub:home')
    if request.method == 'POST': 
        form = addsubscriptionform(request.POST, instance=subscription)
        if form.is_valid():
            form.save()
            return redirect('subhub:home')
    else:
        form = addsubscriptionform(instance=subscription)
    return render(request, 'subhub/edit-subscription.html', {'form': form, 'subscription': subscription, "current_app": "editsub"})

def delete_subscription(request, subscription_id):
    subscription = get_object_or_404(Subscription, id=subscription_id)
    if subscription.user == request.user:
        subscription.delete()
        messages.success(request, "Your subscription has been successfully deleted!")
    return redirect('subhub:home')

 