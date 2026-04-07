from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Subscription, timeConversions
from .forms import addsubscriptionform
from users.models import Profile





from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.forms import createbudgetform, editbudgetform
from django.utils import timezone # Timezone allows us to get the current time
from datetime import timedelta # Allows us to find the difference between times. We need this in order to calculate relevant subscriptions
from dateutil.relativedelta import relativedelta



ReocurranceDict = {  # This allows me to map each string data attribute to an actual time
    'Daily': relativedelta(days=1), # Dictionary eastablished
    'Weekly': relativedelta(weeks=1),
    'Biweekly': relativedelta(weeks=2),
    'Monthly': relativedelta(months=1),
    'Trimonthly': relativedelta(months=3),
    'Biyearly': relativedelta(months=6),
    'Anually': relativedelta(years=1),
}



@login_required(login_url='users:login')
def home(request):
    now = timezone.now()
    current_app = "subhub"
    delta = ReocurranceDict.get(request.user.profile.reocurrance)
    end = now + delta
    upcoming = Subscription.objects.filter(
        user=request.user,
        due_date__gte=now,
        due_date__lte=end,
    )
    subscriptions = Subscription.objects.filter(
        user=request.user
    ).order_by('-due_date')
    #balance = request.user.profile.balance
    #budget_form = editbudgetform(initial={'balance': balance}) if balance else createbudgetform()
    context = {        # Context system means less clutter in the return render
        'current_app' : current_app,
        'subscriptions' : subscriptions,
        #'budget_form': budget_form,
        #'time' : time,
        "upcoming" : upcoming,
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
    return render(request, "subhub/add-subscription.html", {"form": form, "current_app": "addsub"})
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


def SD(request):
    if request.method == 'GET':
        subscriptionPRE = get_object_or_404(Subscription)
        subscription = subscriptionPRE
        balance = get_object_or_404(Profile.balance)
        reocurrance = get_object_or_404(Profile.reocurrance)
        now = timezone.now()
        next_day = now + relativedelta(days=1)
        next_week = now + relativedelta(weeks=1)
        next_2weeks = now + relativedelta(weeks=2)
        next_month = now + relativedelta(months=1)
        next_3months = now + relativedelta(months=3)
        next_halfyear = now + relativedelta(years=0.5)
        next_year = now + relativedelta(years=1)
        print(f"HELLO {next_year}")
        upcoming = Subscription.objects.filter(due_date__gte=now, due_date__lte=next_year) # gte means greater than or equal to, lte means less than or equal to.
    
    return render(request, 'subhub/home.html', {'upcoming': upcoming})