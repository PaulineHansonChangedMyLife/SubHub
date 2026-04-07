from django import forms
from .models import Profile

#class createbudgetform(forms.ModelForm):
    #class Meta:
        #model = Profile
        #fields = ['balance']

#class editbudgetform(forms.ModelForm):
    #class Meta:
        #model = Profile
        #fields = ['balance']
REOCURRANCE_CHOICES = [
     
    ('Daily', 'Daily'),
    ('Weekly', 'Weekly'),
    ('Biweekly', 'Biweekly'),
    ('Monthly', 'Monthly'),
    ('Trimonthly', 'Trimonthly'),
    ('Biyearly', 'Biyearly'),
    ('Anually', 'Anually'),
]

class createbudgetform(forms.Form): # Form to store top up information like amounts and error messages
    balance = forms.DecimalField(min_value=0.01, decimal_places=2, max_digits=10)
    reocurrance = forms.ChoiceField(choices=REOCURRANCE_CHOICES)
    label="Budget Amount"
    error_messages={
    'min_value': "Please enter an amount greater than $0.00.",
    'invalid': "Enter a valid amount in dollars and cents.",
}
    
class editbudgetform(forms.Form): # Form to store top up information like amounts and error messages
    balance = forms.DecimalField(min_value=0.01, decimal_places=2, max_digits=10)
    reocurrance = forms.ChoiceField(choices=REOCURRANCE_CHOICES)
    label="Budget Amount"
    error_messages={
    'min_value': "Please enter an amount greater than $0.00.",
    'invalid': "Enter a valid amount in dollars and cents.",
}