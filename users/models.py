from django.db import models
from django.contrib.auth.models import User
#from subhub.models import Subscription
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

@receiver(post_save, sender=User)     # Used to ensure a profile is created for the user
def ensure_profile(sender, instance: User, created, **kwargs):
    profile, made = Profile.objects.get_or_create(user=instance)
    if (made or not profile.user):
        profile.save(update_fields=["user"])


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    #subscription = models.ManyToManyField(Subscription, related_name='subscriptions', blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True)  # User's current balance
    #financestatus = models.CharField(max_length=10, blank=True)
    #financesd = models.DecimalField(max)

    class reocurrance(models.TextChoices):
        Daily = 'Daily', 'Daily'
        Weekly = 'Weekly', 'Weekly'
        Biweekly = 'Biweekly', 'Biweekly'
        Monthly = 'Monthly', 'Monthly'
        Trimonthly = 'Trimonthly', 'Trimonthly'
        Biyearly = 'Biyearly', 'Biyearly'
        Anually = 'Anually', 'Anually'

    reocurrance = models.CharField(
        max_length=20,
        choices=reocurrance.choices,
        db_index=True,
    )
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs) 

    def __str__(self):
        return self.user.balance
