from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

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
    ('Anual', 'Anual'),
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
    
class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=10, required=True)

    class Meta:
        model = User
    #we use username password1 and password 2 as confirmation in field
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        username = self.cleaned_data['username'].strip().lower()
        user.username = username            # username in data mirrors username

        if commit:
            user.save()
            # ensure profile & nickname
            profile, _ = Profile.objects.get_or_create(user=user)
            profile.user = user
            profile.save(update_fields=['user'])
        return user

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"autofocus": True})
    )