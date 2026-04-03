from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#from .models import testModel
#from .forms import testForm

@login_required(login_url='users:login')
def home(request):
    return render(request, "subhub/home.html", {"current_app": "subhub"}) # Current app added to return so we can determine what page we are on

@login_required
def signinmessage():
    return 
