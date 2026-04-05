from django.urls import path
from . import views

urlpatterns = [
   path("", views.home, name="home"),
   path('add-subscription/', views.add_subscription, name='add_subscription'),
   path('edit-subscription/<int:subscription_id>', views.edit_subscription, name='edit_subscription'),
   path('delete-subscription/<int:subscription_id>', views.delete_subscription, name='delete_subscription'),

   path('create-budget/', views.create_budget, name='create_budget'),
   path('edit-budget/', views.edit_budget, name='edit_budget'),
]