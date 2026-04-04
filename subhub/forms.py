from django import forms
from django.contrib.auth.models import User
from .models import Subscription


class addsubscriptionform(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['name', 'price', 'reocurrance', 'category', 'due_date']


    