from django.urls import path
from . import views

urlpatterns = [
   path("", views.home, name="home"),
   path('add-subscription/', views.add_subscription, name='add_subscription')
]