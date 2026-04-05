from django.urls import path
from . import views


urlpatterns = [
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path('create-budget/', views.create_budget, name='create_budget'),
    path('edit-budget/', views.edit_budget, name='edit_budget'),
]