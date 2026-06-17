from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


# Create your models here.
class Subscription(models.Model): # Subscription model | Needed to track every users subscriptions
    name = models.CharField(max_length=40)
    user = models.ForeignKey(User, related_name='Subscriptions', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits =10, decimal_places=2, validators=[MinValueValidator(0.01)]) # MinValueValidator added to ensure negative subscription prices arent possible
    created_on = models.DateTimeField(auto_now_add=True)

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

    link = models.CharField(max_length=2000, blank=True, null=True) # Set the link that your subscription points to

    def __str__(self):
        return self.name


