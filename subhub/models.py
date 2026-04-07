from django.db import models
from django.contrib.auth.models import User


from django.utils import timezone # Timezone allows us to get the current time
from datetime import timedelta # Allows us to find the difference between times. We need this in order to calculate relevant subscriptions
from dateutil.relativedelta import relativedelta

# Create your models here.
class Subscription(models.Model): # Subscription model | Needed to track every users subscriptions
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name='Subscriptions', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits =10, decimal_places=2)

    class reocurrance(models.TextChoices):
        Daily = 'Daily', 'Daily'
        Weekly = 'Weekly', 'Weekly'
        Biweekly = 'Biweekly', 'Biweekly'
        Monthly = 'Monthly', 'Monthly'
        Trimonthly = 'Trimonthly', 'Trimonthly'
        Biyearly = 'Biyearly', 'Biyearly'
        Anually = 'Anually', 'Anually'


    class category(models.TextChoices):
        fixed = 'fixed', 'fixed'
        entertainment = 'entertainment', 'entertainment'
        groceries = 'groceries', 'groceries'
        AI = 'AI', 'AI'
        education = 'education', 'education'
        loans = 'loans', 'loans'
        other = 'other', 'other'

    due_date = models.DateField()
    reocurrance = models.CharField(
        max_length=20,
        choices=reocurrance.choices,
        db_index=True,
    )


    category = models.CharField(
        max_length=20,
        choices=category.choices,
        db_index=True,
    )

    def __str__(self):
        return self.name


def timeConversions():
    now = timezone.now()
    next_day = now + relativedelta(days=1)
    next_week = now + relativedelta(weeks=1)
    next_2weeks = now + relativedelta(weeks=2)
    next_month = now + relativedelta(months=1)
    next_3months = now + relativedelta(months=3)
    next_halfyear = now + relativedelta(months=6)
    next_year = now + relativedelta(years=1)
