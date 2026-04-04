from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subscription(models.Model): # Subscription model | Needed to track every users subscriptions
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name='Subscriptions', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits =10, decimal_places=2)

    class reocurrance(models.TextChoices):
        daily = 'daily', 'daily'
        weekly = 'weekly', 'weekly'
        biweekly = 'biweekly', 'biweekly'
        monthly = 'monthly', 'monthly'
        trimonthly = 'trimonthly', 'trimonthly'
        biyearly = 'biyearly', 'biyearly'
        anually = 'anually', 'anually'

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
