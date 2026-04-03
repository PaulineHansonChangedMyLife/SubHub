from django.urls import path
from . import views
from django.contrib import admin # Imported libaries for google oAuth
from django.urls import path, include

urlpatterns = [
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path('accounts/', include('allauth.urls')), # oAuth for google login method
]